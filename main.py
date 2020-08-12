from pathlib import Path

import tempfile

import sys

# import all components
from tkinter import *

from tkinter.ttk import Combobox

# import filedialog module
from tkinter import filedialog

# import pdf2image module
from pdf2image import convert_from_path


# Function for opening the
# file explorer window
def browseFiles():
    input_path = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("PDF files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    # Change label contents
    label_input_path.configure(text=input_path)
    # Set root variable
    window.path_file_pdf = input_path
    window.file_name = Path(input_path).stem


def browseFolder():
    folder_name = filedialog.askdirectory()
    # Change label contents
    label_output_path.configure(text=folder_name)
    # Set root variable
    window.path_output_folder = folder_name


# Function for cover pdf to image
def pdf2img():
    if window.path_file_pdf == 'None' or len(window.path_file_pdf) == 0:
        label_input_path.configure(text="Please choice your file!")
    elif window.path_output_folder == 'None' or len(window.path_output_folder) == 0:
        label_output_path.configure(text="Please choice your folder!")
    else:
        print('Start pdf2img ...')

        # Get dpi value in combo box:
        value = combo.get()

        # cover pdf to img:
        images = convert_from_path(window.path_file_pdf, value, poppler_path='poppler/bin')
        i = 1
        for image in images:
            image.save(window.path_output_folder + '/' + window.file_name + '_' + str(i) + '.jpeg', 'JPEG')
            i = i + 1
        label_app_status.configure(text="Successful!")

        # Stop run
        print('Done!')


# Create the root window
window = Tk()
# Set window title
window.title('PDF to IMAGE')
# Set window size
window.geometry("320x150")

# Set root variable
window.path_file_pdf = 'None'
window.path_output_folder = 'None'
window.file_name = 'None'

# Create widgets

label_app_status = Label(window,
                         text='Welcome!',
                         fg="green",
                         height=2)
label_input = Label(window,
                    text="Input:")

label_input_path = Label(window,
                         text="Select your PDF file",
                         width=30,
                         relief="groove",
                         fg="blue")

button_browse_input = Button(window,
                             text="Browse",
                             command=browseFiles)

label_output = Label(window,
                     text="Output:")

label_output_path = Label(window,
                          text="Select your output folder",
                          width=30,
                          relief="groove",
                          fg="blue")

button_browse_output = Button(window,
                              text="Browse",
                              command=browseFolder)

button_run = Button(window,
                    text="Run",
                    padx=30,
                    pady=10,
                    command=pdf2img)

button_exit = Button(window,
                     text="Exit",
                     padx=10,
                     pady=10,
                     command=exit)

label_dpi = Label(window,
                  text="DPI: ")

combo = Combobox(window)
combo['values'] = (100, 200, 500, 700, 1000)
combo.current(1)  # set the selected item

# Grid layout
label_input.grid(column=0, row=0)

label_input_path.grid(column=1, row=0)

button_browse_input.grid(column=2, row=0)

label_output.grid(column=0, row=1)

label_output_path.grid(column=1, row=1)

button_browse_output.grid(column=2, row=1)

label_dpi.grid(column=0, row=2)
combo.grid(column=1, row=2)

button_run.grid(column=1, row=3, padx=3, pady=3)

button_exit.grid(column=2, row=3)

label_app_status.grid(column=1, row=4)

# Let the window wait for any events
window.mainloop()
