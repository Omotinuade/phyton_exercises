from pathlib import Path


def assignment():
    list_one = []
    file = Path.cwd() / "new_folder" / ""
    file.mkdir(exist_ok=True)
    open_file = file / "Hello.txt"
    open_file.touch()
    open_file.write_text("Hello there!")
    for line in open_file.read_text():
        list_one.append(line)

    return list_one


print(assignment())
