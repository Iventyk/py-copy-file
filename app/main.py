def copy_file(command: str) -> None:
    split_command = command.strip().split(" ")

    if len(split_command) != 3 or split_command[0] != "cp":
        return False

    file_name = split_command[1]
    new_file_name = split_command[2]

    if file_name == new_file_name:
        return False

    try:
        with open(file_name, "r") as file:
            file_data = file.read()
    except FileNotFoundError:
        return False

    try:
        with open(new_file_name, "w") as new_file:
            new_file.write(file_data)
    except FileNotFoundError:
        return False
