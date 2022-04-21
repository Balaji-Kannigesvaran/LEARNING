# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import Final
import re 
from tkinter import messagebox

filepath_browse=""
filepath_manual=""

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
    if file:
      global filepath_browse
      filepath_browse = os.path.abspath(file.name)
      filepath_manual = Entry(win, width=20)
      filepath_manual.grid(row=2, column=1)
      filepath_manual.insert(0,filepath_browse)

# Create an instance of tkinter frame
win = Tk()
sv = StringVar()
ip1=""
ip2=""
def callback():
    global ip2
    ip2 = (sv.get())
    return TRUE

# return filepath_browse
def submit():
  global filepath_browse
  print("-------------------------------------------------------")
  # print(filepath_browse)
  
  global ip2
  # filepath_manual.grid(row=2, column=1)
  # print( "fpminst",filepath_manual.insert(0,filepath_browse))

  ip1 = ip_str.get()
  # ip2=filepath_manual.get()
  if filepath_browse != "":
    ip2 = filepath_browse
    filepath_browse = ""
    filepath_manual = Entry(win, width=20)
    filepath_manual.grid(row=2, column=1)

  else:
    filepath_manual = Entry(win, width=20)
    filepath_manual.grid(row=2, column=1)
    ip2=filepath_manual.get()
    print("else: " , ip2, sep ="\n")
  print (ip1)
  print (ip2)

  ip1_case = "Enter the string" if (ip1 == "") else ""
  Label(win, text=ip1_case, font=('Aerial 11'),fg="red", width=20, height=1).grid(row=1,column=5)

  ip2_case = "Enter the input file" if (ip2 == "") else ""
  Label(win, text=ip2_case, font=('Aerial 11'),fg="red", width=20, height=1).grid(row=2,column=5)

  if ((ip1_case == "") and (ip2_case == "")):
    # try:
      op = Final.validate (ip1,ip2)
      op_diplay = Label (win, text="Most Synonomical Sentence : " + str(op), wraplength=500, font=('Aerial 11'), width=60, justify=LEFT)
      op_diplay.grid(row=4,column=0, columnspan = 6, padx=10, pady=20)
    # except Exception as e:
      # messagebox.showerror('Python Error', e)

# F:\DETECT\data_set.txt

# Set the geometry of tkinter frame
win.title('Synonymous Sentence Finder')
win.geometry("700x350")
# win.resizable(False, False)

# Add a Label widget
label = Label(win, text="          Synonymous Sentence Finder", font=('Georgia 13'))
label.grid(row=0, column=0, columnspan=5, pady=20)

# Getting input string
ip_str_label = Label(win, text = "Enter the string", font=('Aerial 11'), width=20, height=5, justify="right")
ip_str_label.grid(row=1, column=0)

ip_str = Entry(win, width=20)
ip_str.grid(row=1, column=1)

# Getting filepath Manually
filepath_label = Label(win, text = "Input file", font=('Aerial 11'), width=20, height=2, justify="right")
filepath_label.grid(row=2, column=0)

filepath_manual = Entry(win, width=20)
filepath_manual.grid(row=2, column=1)

ip_str_label = Label(win, text = " or ", width=10, height=2)
ip_str_label.grid(row=2, column=2)

browse_button = ttk.Button(win, text="Browse", command=open_file, width=20)
browse_button.grid(row=2,column=3)

Submit_button = ttk.Button(win, text="Submit", command=submit, width=20)
Submit_button.grid(row=3,column=3)

win.mainloop()