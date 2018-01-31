"""
WebWriter allows for easier web development for beginners (such as myself). Currently only works through terminal
commands but will most likely extend to a GUI format as well.

Creates 3 object handlers: FileManager, HtmlBrowser and HtmlEditor.
    FileManager handles the creation of files
    HtmlBrowser searches through html files and can select data or get the position of it in the file.
    HtmlEditor actually writes to the html file to add, delete or replace elements.
"""
import os.path
import re

html_path = "html_test.html"

# Debug Switch for print statements
debug = False
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


def dprint(str):
    """
    Only prints when not in Debug mode (debug=True/False)
    :param str: string
    :return:
    """
    if debug:
        print("-----> " + str)


dprint("Debug Messages On")


class FileManager(object):
    """
    Manages files. Ideally the only part that will actually interact with files but currently the other handlers
    also and read and write directly to files.
    """
    def __init__(self):
        self.file = None
        self.file_dict = {}
        dprint("FileManager Initialized.")

    @staticmethod
    def create_file(path):
        """
        Creates a file at the given path.
        :param path: string
        :return:
        """
        dprint("Attempting to create a new file " + path)
        if get_file_exist(path):
            print("Unexpected! File", path, "already exists.")
            return
        file = open(path, "w+")
        file.close()

    def open_file(self, path):
        """
        Opens file for appended writing at the given path. Saves the file object to self.file.
        :param path: string
        :return:
        """
        dprint("Attempting to open file " + path)
        if get_file_exist(path):
            self.file = open(path, "w+")
            print("File " + path + " is open")
        else:
            print("File", path, "does not exist.")

    def close_file(self):
        """
        Closes the file found in self.file.
        :return:
        """
        dprint("Attempting to close file.")
        try:
            self.file.close()
            dprint("File successfully closed.")
        except AttributeError:
            print("No file currently open with this object.")

    def write_from_template(self, type):
        """
        Writes the basic template to self.file given its type.
        :param type: string
        :return:
        """
        dprint("Attempting to write template to file")
        try:
            if type is "html":
                with open("basic_html.txt", "r") as template:
                    data = template.read()
                self.file.write(data)
                dprint("Template written.")
        except AttributeError:
            print("No file loaded.")

    def add_file_to_dict(self, path, key):
        """
        Adds a file to the dictionary for human readability and potential future functionality. Still not implemented.
        :param path: string
        :param key: string
        :return:
        """
        self.file_dict[key] = path

    def smart_create_blank_html(self, path, name):
        """
        Condensed function to create a basic html file.
        :param path: string
        :param name: string
        :return:
        """
        dprint(" ----- SMART PROCESS BEGIN ----- ")

        if get_file_type(path) == "html":
            if get_file_exist(path):
                t = input("File " + str(path) + " already exists. Revert to basic template? (Y/N) ").capitalize()
                if t == "Y":
                    self.open_file(path)
                    self.write_from_template("html")
                    self.add_file_to_dict(path, name)
                    self.close_file()
                    dprint("File " + str(path) + " reverted to basic html template")
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
            print("File type give is " + get_file_type(path))


class HtmlBrowser(object):
    """
    Handles the search queries and acquisition of data from the html.
    """
    def __init__(self):
        dprint("HtmlBrowser Initialized.")

    @staticmethod
    def get_element(path, tag, text_only=True, pos=False):
        """
        Searches for a given html element given its tag. text_only removes the brackets '< >' if on and pos changes the
        return to be the starting and ending position of the element in the file.

        :param path: string
        :param tag: string
        :param text_only: bool
        :param pos: bool
        :return: string/ [int, int]
        """
        with open(path, "r") as file:
            data = file.read()
        m = re.search("<" + tag + ">.*</" + tag + ">", data)
        if m:
            if pos:
                # Only grab the span of the element
                return m.span()
            else:
                # Grab the content included within the tag
                span = m.span()
                tag_size = len(tag)
                if text_only:
                    return data[span[0]+tag_size:span[1]-(tag_size+1)]
                else:
                    return data[span[0]:span[1]]
        else:
            print("Unexpected!: No html element with give tag <" + tag + "> found in file " + path)


class Scribe(object):
    """
    Parent object for all types of editors. Currently only HTML editor.
    Handles the basic functions that should be the same for every type of file.
    """
    def __init__(self):
        super().__init__()
        self.file = None
        self.pos = 0

    def overwrite(self, text, span):
        """
        Replace text over the given range.
        :param text: string
        :param span: [int, int]
        :return:
        """
        with open(self.file, "r") as file:
            data = file.read()
        front = data[:span[0]]
        back = data[span[1]:]
        data = front + text + back
        with open(self.file, "w+") as file:
            file.write(data)

    def write_add(self, text):
        """
        Adds text at the object's current position in the file.
        :param text: string
        :return:
        """
        with open(self.file, "r") as file:
            data = file.read()
        data = data[:self.pos] + text + data[self.pos:]
        with open(self.file, "w+") as file:
            file.write(data)


class HtmlEditor(Scribe):
    """
    Only edits HTML files and has HTML specific functions.
    """
    def __init__(self):

        super().__init__()
        dprint("HtmlEditor Initialized.")

    def replace_element(self, tag, **kwargs):
        """
        Finds the given html element via its tag and replaces it. Currently only works with the <title> tag.
        :param tag: string
        :param kwargs: string/int/float
        :return:
        """
        if tag is "title":
            span = html_browser.get_element(self.file, tag, pos=True)
            self.overwrite("<title>This title was written in python</title>", span)


# Workspace

file_manager = FileManager()
html_browser = HtmlBrowser()
html_editor = HtmlEditor()
dprint("Objects Finished Initializing. \n")

# html_editor.file = html_path
# html_editor.replace_element("title")
