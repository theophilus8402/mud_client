
import asyncio
import functools
import re

from select import select
from telnetlib import IAC, SB, SE, Telnet, DO, TTYPE, BINARY, DONT, WILL

GMCP = b'\xc9'


def strip_ansi(line):
    # TODO compile this
    return re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', '', line)

mud_encoding = 'iso-8859-1'

def gmcpOut(sock, msg):
    print("gmcpOut: {}".format(msg))
    sock.sendall(IAC + SB + GMCP + msg.encode(mud_encoding) + IAC + SE)

supportables = [
        'char 1',
        'char.base 1',
        'char.maxstats 1',
        'char.items 1',
        'char.status 1',
        'char.statusvars 1',
        'char.vitals 1',
        'char.worth 1',
        'comm 1',
        'comm.tick 1',
        'group 1',
        'room 1',
        'room.info 1',
        'redirect.window 1'
    ]

def handle_gmcp(data):
    #print("handle_gmcp: {}".format(data))
    pass

def iac_cb(telnet_session, sock, cmd, option):
    if cmd == WILL:
        if option == GMCP:
            print("Enabling GMCP")
            sock.sendall(IAC + DO + option)
            gmcpOut(sock, 'Core.Hello { "client": "Cizra", "version": "1" }')
            gmcpOut(sock, 'Core.Supports.Set ' + str(supportables).replace("'", '"'))
        elif option == TTYPE:
            log("Sending terminal type 'Cizra'")
            sock.sendall(IAC + DO + option +
                    IAC + SB + TTYPE + BINARY + b'Cizra' + IAC + SE)

        else:
            sock.sendall(IAC + DONT + option)

    elif cmd == SE:
        data = telnet_session.read_sb_data()
        if data and data[0] == ord(GMCP):
            # change it to a gmcp queue
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
            fds, _, _ = select([telnet_socket], [], [], .01)

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
                        print("sb_data: {}".format(sb_data))
                else:
                    from_server_queue.put_nowait(data)

            # handle sending stuff to the server
            if to_server_queue.qsize() > 0:
                data_to_send = await to_server_queue.get()
                session.write(data_to_send.encode(mud_encoding))
            await asyncio.sleep(.05)
    finally:
        session.close()

