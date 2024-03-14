import os

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        except PermissionError:
            print(f"You don't have permission to delete the file '{file_path}'.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
    else:
        print(f"File '{file_path}' does not exist.")
file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)
