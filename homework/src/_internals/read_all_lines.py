import os


def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        with open(f"data/input/{filename}", "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines
