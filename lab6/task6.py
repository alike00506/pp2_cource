import os

def list_directories_files(path, mode='all'):
    if mode == 'directories':
        items = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    elif mode == 'files':
        items = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
    else:
        items = os.listdir(path)
    return items
path = input("Enter the path: ")
print("Directories:")
directories = list_directories_files(path, 'directories')
for directory in directories:
    print(directory)
print("\nFiles:")
files = list_directories_files(path, 'files')
for file in files:
    print(file)
print("\nAll directories and files:")
all_items = list_directories_files(path)
for item in all_items:
    print(item)
