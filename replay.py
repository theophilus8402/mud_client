
from achaea import Achaea
from achaea.client import c
import json

def replay(log_path):

    achaea = Achaea()

    with open(log_path) as f:
        for line in f.readlines():
            if line.strip() == "":
                continue

            timestamp, msg_type, msg = json.loads(line)

            try:
                if msg_type == "server_text" and msg.strip() != "":
                    c.current_chunk = msg
                    for msg_line in msg:
                        print(f"> {msg_line}")
                        yield achaea.handle_triggers(msg_line)
                elif msg_type == "gmcp_data":
                    print(f"> {msg}")
                    gmcp_blob = json.loads(msg)
                    gmcp_type = gmcp_blob["type"]
                    gmcp_data = gmcp_blob["data"]
                    yield achaea.handle_gmcp(gmcp_type, gmcp_data)
                elif msg_type in ["data_sent", "user_input"]:
                    print(f"< {msg}")
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
    parser.add_argument("log_path", help="path to log file")
    args = parser.parse_args()

    player = replay(args.log_path)

