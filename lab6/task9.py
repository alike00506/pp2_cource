def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return -1
file_path = input("enter path: ")
num_lines = count_lines(file_path)
if num_lines != -1:
    print(f"Amount of lines '{file_path}': {num_lines}")
