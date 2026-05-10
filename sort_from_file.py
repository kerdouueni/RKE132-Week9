def sort_data_alph(file_path):

    data_from_file = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data_from_file.append(line.strip())

    data_from_file.sort()

    with open(file_path, "w", encoding="utf-8") as f:
        for element in data_from_file:
            f.write(element + "\n")

    return data_from_file

data = sort_data_alph(r"data/todo.txt")
print(data)
