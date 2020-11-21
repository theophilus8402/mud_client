import asyncio
import functools
import json
import logging
import re
from select import select
from telnetlib import BINARY, DO, DONT, IAC, SB, SE, TTYPE, WILL, Telnet

GMCP = b"\xc9"
mud_encoding = "iso-8859-1"


def strip_ansi(line):
    # TODO compile this
    return re.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", line)


def gmcpOut(sock, msg):
    logging.debug(f"gmcpOut: {msg}")
    if isinstance(msg, str):
        sock.sendall(IAC + SB + GMCP + msg.encode(mud_encoding) + IAC + SE)
    else:
        sock.sendall(IAC + SB + GMCP + msg + IAC + SE)


supportables = [
    "char 1",
    "comm 1",
    "comm.channel 1",
    "char.base 1",
    "char.maxstats 1",
    "char.items 1",
    "char.status 1",
    "char.statusvars 1",
    "char.vitals 1",
    "char.worth 1",
    "comm.tick 1",
    "group 1",
    "room 1",
    "room.info 1",
    "redirect.window 1",
    "comm.channel.text 1",
]

compiled_gmcp_pat = re.compile("([.A-Za-z]+) (.*)")

gmcp_queue = asyncio.Queue()


def handle_gmcp(data):
    matches = compiled_gmcp_pat.match(data)
    gmcp_type, gmcp_data = matches.groups()
    gmcp_json = json.loads(gmcp_data)
    gmcp_queue.put_nowait((gmcp_type, gmcp_json))


def iac_cb(telnet_session, sock, cmd, option):
    if cmd == WILL:
        if option == GMCP:
            logging.debug("Enabling GMCP")
            sock.sendall(IAC + DO + option)
            gmcpOut(sock, 'Core.Hello { "client": "Cizra", "version": "1" }')
            supportables_str = str(supportables).replace("'", '"')
            gmcpOut(sock, "Core.Supports.Set " + supportables_str)
        elif option == TTYPE:
            logging.debug("Sending terminal type 'PyMudClient'")
            sock.sendall(
                IAC
                + DO
                + option
                + IAC
                + SB
                + TTYPE
                + BINARY
                + b"PyMudClient"
                + IAC
                + SE
            )

        else:
            sock.sendall(IAC + DONT + option)

    elif cmd == SE:
        data = telnet_session.read_sb_data()
        if data and data[0] == ord(GMCP):
            # change it to a emcp queue
            handle_gmcp(data[1:].decode(mud_encoding))


def telnet_connect(host, port):
    t = Telnet()
    new_iac_cb = functools.partial(iac_cb, t)
    t.set_option_negotiation_callback(new_iac_cb)
    t.open(host, port)
    return t


async def handle_telnet(host, port, from_server_queue, to_server_queue):

    session = telnet_connect(host, port)
    telnet_socket = session.get_socket()

    try:
        while True:
            fds, _, _ = select([telnet_socket], [], [], 0.01)

            # handle reading things from the server
            for fd in fds:
                try:
                    data = session.read_very_eager()
                except EOFError:
                    break
                data = data.decode(mud_encoding)

                if not data:
                    sb_data = session.read_sb_data()
                    if sb_data != b"":
                        logging.debug(f"sb_data: {sb_data}")
                else:
                    from_server_queue.put_nowait(data)

            # handle sending stuff to the server
            if to_server_queue.qsize() > 0:
                data_to_send = await to_server_queue.get()
                if isinstance(data_to_send, bytes):
                    gmcpOut(telnet_socket, data_to_send)
                else:
                    session.write(data_to_send.encode(mud_encoding))
            await asyncio.sleep(0.05)
    finally:
        session.close()
