import json


def parse_log(input_log):
    log_lines = []
    with open(input_log) as f:
        for line in f.readlines():
            print(line)
            [timestamp, msg_type, msg] = json.loads(line)
            log_lines.append((timestamp, msg_type, msg))
    return log_lines


def filter_by_msg_type(input_lines, wanted_msg_types):
    return [
        (timestamp, msg_type, msg)
        for timestamp, msg_type, msg in input_lines
        if msg_type in wanted_msg_types
    ]


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Parsing logs!")
    parser.add_argument("-t", action="store_true", help="display timestamps")
    parser.add_argument("-g", action="store_true", help="display only gmcp data")
    parser.add_argument("input_log", help="path to log file")
    parser.add_argument("output_file", help="path to output file")
    args = parser.parse_args()

    if args.t:
        print("You want timestamps!")
    if args.g:
        print("You want gmcp data!")

    lines = parse_log(args.input_log)

    for line in lines[:20]:
        print(line)

    filtered_lines = filter_by_msg_type(lines, ["data_sent", "server_text"])

    stuff_to_write = [
        msg if mt != "data_sent" else f">>> {msg}" for ts, mt, msg in filtered_lines
    ]

    with open(args.output_file, "w") as f:
        f.write("\n".join(stuff_to_write))

    for line in filtered_lines[:20]:
        print(line)
