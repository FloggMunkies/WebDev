"""
Attempting to write a web-page in python. This involves writing Javascript, html and css via python as well.

"""
import os.path


class Foo:
    def __init__(self):
        self.html_path = "html_test.html"
        self.file = None

    @staticmethod
    def get_file_exist(path):
        return os.path.isfile(path)

    @staticmethod
    def get_file_type(path):
        return path[path.find("."):]

    def create_file(self, path):
        print("Attempting to create a new file", path)
        if self.get_file_exist(path):
            print("File", path, "already exists.")
            return
        file = open(path, "w+")
        file.close()

    def open_file(self, path):
        print("Attempting to open file", path)
        if self.get_file_exist(path):
            self.file = open(path, "w+")
            print("File", path, "is open")
        else:
            print("File", path, "does not exist.")

    def close_file(self):
        print("Attempting to close file")
        try:
            self.file.close()
            print("File successfully closed.")
        except AttributeError:
            print("No file currently open with this object.")

    def write_from_template(self, type):
        print("Attempting to write template to file")
        try:
            if type is "html":
                with open("basic_html.txt", "r") as template:
                    data = template.read()
                self.file.write(data)
                print("Template written.")
        except AttributeError:
            print("No file loaded.")


Bar = Foo()

Bar.open_file(Bar.html_path)
Bar.write_from_template("html")
Bar.close_file()
