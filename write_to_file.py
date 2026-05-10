def use_write_mode(file_path):
    with open(file_path, "w", encoding="utf-8"):
        pass

use_write_mode(r"data/todo.txt")