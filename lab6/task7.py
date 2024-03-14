import os

def check_path_access(path):
    access_info = {
        'existence': os.path.exists(path),
        'readability': os.access(path, os.R_OK),
        'writability': os.access(path, os.W_OK),
        'executability': os.access(path, os.X_OK)
    }
    return access_info
path = input("Введите путь: ")
access_info = check_path_access(path)
print(f"Путь '{path}':")
print(f"Существует: {access_info['existence']}")
print(f"Доступен для чтения: {access_info['readability']}")
print(f"Доступен для записи: {access_info['writability']}")
print(f"Доступен для выполнения: {access_info['executability']}")

