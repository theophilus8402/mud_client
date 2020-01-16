
from achaea import Achaea
import json

def replay(log_path):

    achaea = Achaea()

    with open(log_path) as f:
        for line in f.readlines():
            timestamp, msg_type, msg = json.loads(line)

            try:
                if msg_type == "server_text" and msg.strip() != "":
                    print(f"> {msg}")
                    yield achaea.handle_triggers(msg)
                elif msg_type == "gmcp_data":
                    print(f"> {msg}")
                    yield achaea.handle_gmcp_data(msg)
                elif msg_type in ["data_sent", "user_input"]:
                    print(f"< {msg}")
                    yield achaea.handle_aliases(msg)
            except Exception as e:
                print(f"Don't know what this msg type is: {msg_type}.")
                print(f"Or!  There's a problem with the msg: {msg}.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="replay a log file")
    parser.add_argument("log_path", help="path to log file")
    args = parser.parse_args()

    player = replay(args.log_path)

