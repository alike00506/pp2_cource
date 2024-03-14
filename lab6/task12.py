def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")
copy_file(source_file, destination_file)
