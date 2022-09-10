# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import Final

filepath_browse=""
def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
    if file:
      global filepath_browse
      filepath_browse = os.path.abspath(file.name)
      filepath_manual = Entry(win, width=20)
      filepath_manual.grid(row=2, column=1)
      filepath_manual.insert(0,filepath_browse)

# return filepath_browse
def submit():
  ip1 = ip_str.get()
  ip2 =filepath_browse
  op = Final.validate(ip1,ip2)
  Label(win, text="OP : " + str(op), font=('Aerial 11')).grid(row=7,column=0,pady=20)

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.title('ynonymous Sentence Finder')
win.geometry("700x350")
win.resizable(False, False)

# Add a Label widget
label = Label(win, text="Synonymous Sentence Finder", font=('Georgia 13'))
label.grid(row=0,column=0,pady=10)

# Getting input string
ip_str_label = Label(win, text = "Enter the string")
ip_str_label.grid(row=1, column=0)

ip_str = Entry(win, width=20)
ip_str.grid(row=1, column=1)

# Getting filepath Manually
filepath_label = Label(win, text = "Input file")
filepath_label.grid(row=2, column=0)

filepath_manual = Entry(win, width=20)
filepath_manual.grid(row=2, column=1)

ip_str_label = Label(win, text = " or ")
ip_str_label.grid(row=2, column=2)

browse_button = ttk.Button(win, text="Browse", command=open_file)
browse_button.grid(row=2,column=3,pady=20)

Submit_button = ttk.Button(win, text="Submit", command=submit)

Submit_button.grid(row=3,column=3,pady=20)


win.mainloop()