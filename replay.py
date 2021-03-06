import json

import achaea.basic
from achaea import *
from client import Brain, c
from telnet_manager import strip_ansi

achaea.basic.handle_login_info({"name": "veredus"})


def handle_server_text(client, msg):
    c.current_chunk = msg
    for msg_line in msg.split("\n"):
        c.current_line = msg_line
        print(f"> {msg_line}")
        stripped_line = strip_ansi(msg_line).strip()
        client.handle_triggers(stripped_line)


def replay(log_path):

    client = Brain(c)

    with open(log_path) as f:
        for line in f:
            if line.strip() == "":
                continue

            timestamp, msg_type, msg = json.loads(line)

            try:
                if msg_type == "server_text" and msg.strip() != "":
                    handle_server_text(client, msg)
                elif msg_type == "server_text" and msg.strip() == "":
                    pass
                elif msg_type == "gmcp_data":
                    # print(f"> {msg}")
                    gmcp_blob = json.loads(msg)
                    gmcp_type = gmcp_blob["type"]
                    gmcp_data = gmcp_blob["data"]
                    yield client.handle_gmcp(gmcp_type, gmcp_data)
                elif msg_type in ["data_sent", "user_input"]:
                    # print(f"< {msg}")
                    yield client.handle_aliases(msg)
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
        player = replay(args.l)
        for i in player:
            pass
    elif args.t:
        client = Brain(c)
        handle_server_text(client, args.t)
