import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return None, None
path = input("Enter the path: ")
filename, directory = path_info(path)
if filename and directory:
    print("Path exists.")
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist.")
