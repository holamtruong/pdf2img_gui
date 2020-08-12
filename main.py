from pathlib import Path

from tkinter import messagebox

# import all components
from tkinter import *

from tkinter.ttk import Combobox

# import filedialog module
from tkinter import filedialog

# import pdf2image module
from pdf2image import convert_from_path


# Function definitions

def browseFiles():
    label_app_status.configure(text="")
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
    label_app_status.configure(text="")
    folder_name = filedialog.askdirectory()
    # Change label contents
    label_output_path.configure(text=folder_name)
    # Set root variable
    window.path_output_folder = folder_name


def pdf2img():
    if window.path_file_pdf == 'None' or len(window.path_file_pdf) == 0:
        label_input_path.configure(text="Please choice your file!")
    elif window.path_output_folder == 'None' or len(window.path_output_folder) == 0:
        label_output_path.configure(text="Please choice your folder!")
    else:
        print('Start pdf2img ...')

        # Get dpi value in combo box:
        value_dpi = combo.get()

        # Get type value in combo box:
        value_type = combo_type.get()

        # cover pdf to img:
        images = convert_from_path(window.path_file_pdf, value_dpi, poppler_path='poppler/bin')
        i = 1
        for image in images:
            image.save(window.path_output_folder + '/' + window.file_name + '_' + str(i) + '.' + value_type)
            i = i + 1
        label_app_status.configure(text="Successful, " + str(len(images)) + " pages.")

        # Stop run
        print('Done!')


def msg_about():
    messagebox.showinfo("About", "Author: Truong Ho \nEmail: truong360@gmail.com")


# Create the root window
window = Tk()
# Set window title
window.title('PDF to IMAGE')
# Set window size
window.geometry("370x250")

# Set root variable
window.path_file_pdf = 'None'
window.path_output_folder = 'None'
window.file_name = 'None'

# Create UI widgets

canvas = Canvas(window, width=120, height=60)
img = PhotoImage(file="media\panel.png")
canvas.create_image(20, 0, anchor=NW, image=img)

label_input = Label(window, text="Input:")
label_input_path = Label(window, text="Select your PDF file", width=30, relief="groove", fg="gray")
button_browse_input = Button(window, text="Browse", command=browseFiles)

label_output = Label(window, text="Output:")
label_output_path = Label(window, text="Select your output folder", width=30, relief="groove", fg="gray")
button_browse_output = Button(window, text="Browse", command=browseFolder)

button_run = Button(window, text="Run", padx=30, pady=10, command=pdf2img)
button_about = Button(window, text="About", padx=10, pady=5, command=msg_about)
button_exit = Button(window, text="Exit", padx=17, pady=5, command=exit)

label_type = Label(window, text="Type: ")
combo_type = Combobox(window)
combo_type['values'] = ('jpeg', 'png', 'tiff', 'bmp')
combo_type.current(1)  # set the selected item

label_dpi = Label(window, text="DPI: ")
combo = Combobox(window)
combo['values'] = (100, 200, 300, 400, 500, 700, 1000)
combo.current(1)  # set the selected item

label_author = Label(window, text='  Ⓒ Truong Ho', fg="gray")
label_app_status = Label(window, text='Welcome!', fg="green")

# Grid layout setting

canvas.grid(column=1, row=0, padx=5, pady=5)

label_input.grid(column=0, row=1)
label_input_path.grid(column=1, row=1)
button_browse_input.grid(column=2, row=1)

label_output.grid(column=0, row=2)
label_output_path.grid(column=1, row=2)
button_browse_output.grid(column=2, row=2)

label_dpi.grid(column=0, row=3)
combo.grid(column=1, row=3)

label_type.grid(column=0, row=4)
combo_type.grid(column=1, row=4)

button_run.grid(column=1, row=5, pady=5)
button_about.grid(column=2, row=5)
button_exit.grid(column=2, row=5)

label_author.grid(column=0, row=6)
label_app_status.grid(column=1, row=6)

# Let the window wait for any events
window.mainloop()
