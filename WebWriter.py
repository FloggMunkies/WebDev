"""
Attempting to write a web-page in python. This involves writing Javascript, html and css via python as well.

"""
import os.path
import re

html_path = "html_test.html"

# Functions


def get_file_exist(path):
    """
    Checks if the file at the given path exists.
    :param path: string
    :return: True/False
    """
    return os.path.isfile(path)


def get_file_type(path):
        """
        Checks the file at the given path's type via string manipulation.
        :param path: string
        :return: string
        """
        return path[path.find(".")+1:]


class FileManager(object):
    def __init__(self):
        super().__init__()
        self.file = None
        self.file_dict = {}

    @staticmethod
    def create_file(path):
        """
        Creates a file at the given path.
        :param path: string
        :return:
        """
        print("Attempting to create a new file", path)
        if get_file_exist(path):
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
        if get_file_exist(path):
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

        if get_file_type(path) == "html":
            if get_file_exist(path):
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
            print(get_file_type(path))


class HtmlBrowser(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_title(path, text_only=True):
        with open(path, "r") as file:
            data = file.read()
        m = re.search("<title>.*</title>", data)
        if m:
            span = m.span()
            if text_only:
                print(data[span[0]+7:span[1]-8])
            else:
                print(data[span[0]:span[1]])


class Scribe(object):
    def __init__(self):
        super().__init__()
        self.file = None
        self.pos = 0

    def write_add(self, text):
        with open(self.file, "r") as file:
            data = file.read()
        data = data[:self.pos] + text + data[self.pos:]
        with open(self.file, "w+") as file:
            file.write(data)


class HtmlEditor(Scribe):
    def __init__(self):
        super().__init__()

    def add_element(self, tag, *kwargs):
        if tag is "title":
            h_browser.get_title(self.file, text_only=False)


# Workspace
file_manager = FileManager()
h_browser = HtmlBrowser()
h_editor = HtmlEditor()

h_editor.file = html_path
h_editor.add_element("title")

