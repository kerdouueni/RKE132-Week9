def read_from_file(file_path):
    """
    Reads a text file and returns its content as a list of lines.
    Rekoves empty lines and extra spaces.
    """
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            lines.append(text)
    return lines

data_from_file = read_from_file(r"data/todo.txt")

for item in data_from_file:
    print(item)
