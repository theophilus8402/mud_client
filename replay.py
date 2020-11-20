
from achaea import *
from client import c, Brain
from telnet_manager import strip_ansi
import json


import achaea.basic

achaea.basic.handle_login_info({"name": "sarmenti"})

def handle_server_text(msg):
    client = Brain(c)
    c.current_chunk = msg
    for msg_line in msg.split("\n"):
        c.current_line = msg_line
        print(f"> {msg_line}")
        stripped_line = strip_ansi(msg_line).strip()
        client.handle_triggers(stripped_line)


def replay(log_path):

    achaea = Achaea()

    with open(log_path) as f:
        for line in f:
            if line.strip() == "":
                continue

            timestamp, msg_type, msg = json.loads(line)

            try:
                if msg_type == "server_text" and msg.strip() != "":
                    handle_server_text(msg)
                elif msg_type == "server_text" and msg.strip() == "":
                    pass
                elif msg_type == "gmcp_data":
                    # print(f"> {msg}")
                    gmcp_blob = json.loads(msg)
                    gmcp_type = gmcp_blob["type"]
                    gmcp_data = gmcp_blob["data"]
                    yield achaea.handle_gmcp(gmcp_type, gmcp_data)
                elif msg_type in ["data_sent", "user_input"]:
                    # print(f"< {msg}")
                    yield achaea.handle_aliases(msg)
                else:
                    print(f"Don't know what this msg type is: {msg_type}.")
                    print(f"? {msg}")
            except Exception as e:
                print(f"There's a problem with the msg: {msg}.")
                print(e)
                break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="replay a log file")
    parser.add_argument("-t", help="test triggers on the string")
    parser.add_argument("-l", help="play the log file")
    args = parser.parse_args()

    if args.l:
        player = replay(args.log_path)
        for i in player:
            pass
    elif args.t:
        handle_server_text(args.t)
