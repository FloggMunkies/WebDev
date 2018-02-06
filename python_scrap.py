import PyWeb.WebWriter as ww

# Do not run this file currently
run = True

if run:

    # Pre-constructed objects for handling files
    Files = ww.file_manager
    Browser = ww.html_browser
    Editor = ww.html_editor

    # Demonstration of function by creating a new html file
    html_name = "html_test.html"

    Files.smart_create_blank_html(html_name, "Main")

    # Editing this brand new file's title
    Editor.file = html_name
    Editor.replace_element("title")
