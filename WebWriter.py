"""
Attempting to write a web-page in python. This involves writing Javascript, html and css via python as well.

"""
import os.path

html_path = "html_test.html"


class Foo:
    def __init__(self):
        """

        """
        self.file = None
        self.file_dict = {}

    @staticmethod
    def get_file_exist(path):
        """
        Checks if the file at the given path exists.
        :param path: string
        :return: True/False
        """
        return os.path.isfile(path)

    @staticmethod
    def get_file_type(path):
        """
        Checks the file at the given path's type via string manipulation.
        :param path: string
        :return: string
        """
        return path[path.find(".")+1:]

    def create_file(self, path):
        """
        Creates a file at the given path.
        :param path: string
        :return:
        """
        print("Attempting to create a new file", path)
        if self.get_file_exist(path):
            print("File", path, "already exists.")
            return
        file = open(path, "w+")
        file.close()

    def open_file(self, path):
        """
        Opens file for appended writing at the given path. Saves the file object to self.file.
        :param path: string
        :return:
        """
        print("Attempting to open file", path)
        if self.get_file_exist(path):
            self.file = open(path, "w+")
            print("File", path, "is open")
        else:
            print("File", path, "does not exist.")

    def close_file(self):
        """
        Closes the file found in self.file.
        :return:
        """
        print("Attempting to close file.")
        try:
            self.file.close()
            print("File successfully closed.")
        except AttributeError:
            print("No file currently open with this object.")

    def write_from_template(self, type):
        """
        Writes the basic template to self.file given its type.
        :param type: string
        :return:
        """
        print("Attempting to write template to file")
        try:
            if type is "html":
                with open("basic_html.txt", "r") as template:
                    data = template.read()
                self.file.write(data)
                print("Template written.")
        except AttributeError:
            print("No file loaded.")

    def add_file_to_dict(self, path, key):
        """
        Adds a file to the dictionary for human readability and potential future functionality.
        :param path: string
        :param key: string
        :return:
        """
        self.file_dict[key] = path

    def smart_create_blank_html(self, path, name):
        print(" ----- SMART PROCESS BEGIN ----- ")

        if self.get_file_type(path) == "html":
            if self.get_file_exist(path):
                t = input("File " + str(path) + " already exists. Revert to basic template? (Y/N)").capitalize()
                if t == "Y":
                    self.open_file(path)
                    self.write_from_template("html")
                    self.add_file_to_dict(path, name)
                    self.close_file()
                    print("File " + str(path) + " reverted to basic html template")
                else:
                    print("Aborting process. No changes made.")
            else:
                self.create_file(path)
                self.open_file(path)
                self.write_from_template("html")
                self.add_file_to_dict(path, name)
                self.close_file()
                print("File " + str(path) + " created as a basic html template")
        else:
            print(self.get_file_type(path))


Bar = Foo()

Bar.smart_create_blank_html(html_path, "Main")
print("\n\n" + str(Bar.file_dict))
