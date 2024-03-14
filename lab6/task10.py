def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(item + '\n')
        print(f"List has been written to '{file_path}' successfully.")
    except IOError:
        print(f"Error occurred while writing to '{file_path}'.")
my_list = ["apple", "banana", "orange", "grape", "pineapple"]
file_path = "output.txt"
write_list_to_file(file_path, my_list)
