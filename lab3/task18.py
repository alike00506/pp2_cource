class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string_uppercase(self):
        print("Uppercase String:", self.input_string.upper())


string_manipulator = StringManipulator()

string_manipulator.get_string()

string_manipulator.print_string_uppercase()
