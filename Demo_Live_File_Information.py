#!/usr/bin/env python
import PySimpleGUI as sg


def demonstrate_file_preview():
    first_line = ""

    layout = [
        [sg.Text("Interactive File Selection Demonstrator", size=(30, 1))],
        [sg.Text("Input File")],
        [sg.Input(key="IN_FILE"),
         sg.RFileBrowse(file_types=(("Python", "*.py"),), key="IN_FILE_BUTTON")],
        [sg.Text("Output File")],
        [sg.Input(key="OUT_FILE"), sg.FileBrowse()],
        [sg.Text("_"*80)],
        [sg.Text("", key="MSG"), sg.Input(first_line, key="LINE")],
        [sg.RButton("Display File", key="DISPLAY"), sg.Quit()],
        [sg.Text("_"*80)],
        [sg.Multiline(size=(72, 5), key="DATA")],
    ]

    window = sg.Window("IFSD").Layout(layout)

    while True:
        event, values = window.Read()
        if event is None or event == "Exit":
            break
        if event == "IN_FILE_BUTTON":
            msg, line = get_first_line(values["IN_FILE"])
            window.FindElement("MSG").Update(msg)
            window.FindElement("LINE").Update(line)
        if event == "DISPLAY":
            data = get_10_lines(values["IN_FILE"])
            window.FindElement("DATA").Update(data)
        # Below is needed to keep the "IN_FILE" populated. Why does it get deleted?
        # Similarly, every input field seems to reset upon read. I assume this
        # is deliberate to allow simple data entry via form?
        window.FindElement("IN_FILE").Update(values["IN_FILE"])
            

def get_10_lines(filename):
    multiline = ""
    try:
        with open(filename) as file:
            for i in range(10):
                multiline += file.readline()
            file.close()
    except:
        print("I'll find the pop-up error widget one day.")
        multiline = "Something went wrong."
    finally:
        return multiline


def get_first_line(filename):
    firstline = ""
    try:
        with open(filename) as file:
            firstline = file.readline()
            file.close()
        message = "First line of file:"
    except:
        print("I bet there's a pop-up error hiding somewhere in this fabulous library.")
        message = "Error!"
    finally:
        return message, firstline


if __name__ == '__main__':
    demonstrate_file_preview()
