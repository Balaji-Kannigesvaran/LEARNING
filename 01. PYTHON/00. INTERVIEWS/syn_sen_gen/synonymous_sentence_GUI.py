# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfile
import os
import sentence_validator


class gui:
  """
  
  This class will render the GUI of the Application.
  GUI would consit of two input fields - "Enter the string" & "Input file"
  
  Fields:
  * "Enter the string" -  should be the sentence for which the synonymous sentence has to be found from the set of sentences.
  * "Input file" - should be the path of the text file which would be having multiple sentences and in which the most synonymous sentences should be found. This field can be initiated both using browse button or manually enter you can enter the path of the file.

  Both the input fields are mandatory. If empty, the warning would be shown in the  right end corresponding to the fields. 

  Buttons:
  * Browse - This button would open a dialog box to browse the path of the file from the local computer. The path would be the input for the "Input file" field.
  
  * Submit - On clicking the submit button, it will trigger the validation for the input fields and check if the inputs are entered. upon validation and all inputs in place. It would check for the most synonymous sentences validation.
  If there is any runtime error it would be shown on the message box as well.

  The validated output would be shown in the space below the buttons.

  """
  def __init__ (self,win):
    self.window=win
    self.filepath_browse=""

    # Title 
    self.label = Label(self.window, text="          Synonymous Sentence Finder", font=('Georgia 13'))
    self.label.grid(row=0, column=0, columnspan=5, pady=20)

    # Render and getting input for the field "Enter the string"
    self.ip_str_label = Label(self.window, text = "Enter the string", font=('Aerial 11'), width=20, height=5, justify="right")
    self.ip_str_label.grid(row=1, column=0)

    
    self.ip_str = Entry(self.window, width=20)
    self.ip_str.grid(row=1, column=1)

    # Render and getting input for the field "Input file"
    self.filepath_label = Label(self.window, text = "Input file", font=('Aerial 11'), width=20, height=2, justify="right")
    self.filepath_label.grid(row=2, column=0)

    self.filepath_manual = Entry(self.window, width=20)
    self.filepath_manual.grid(row=2, column=1)

    self.ip_str_label = Label(self.window, text = " or ", width=10, height=2)
    self.ip_str_label.grid(row=2, column=2)

    # Render the GUI Buttons and on click event definition
    self.browse_button = ttk.Button(self.window, text="Browse", command=self.file_path, width=20)
    self.browse_button.grid(row=2,column=3)

    self.Submit_button = ttk.Button(self.window, text="Submit", command=self.submit, width=20)
    self.Submit_button.grid(row=3,column=3)


  # On click event for Browse button
  def file_path(self):
      self.file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
      if self.file:
        global filepath_browse
        self.filepath_browse = os.path.abspath(self.file.name)
        self.filepath_manual = Entry(self.window, width=20)
        self.filepath_manual.grid(row=2, column=1)
        self.filepath_manual.insert(0,self.filepath_browse)

  # On click event for Submit button
  def submit(self):
    global filepath_browse
    self.ip1 = self.ip_str.get()
    self.ip2 = self.filepath_manual.get()
    if self.filepath_browse != "":
      self.ip2 = self.filepath_browse
      self.filepath_browse=""

    #GUI validation for empty input fields 
    self.ip1_case = "Enter the string" if (self.ip1 == "") else ""
    Label(self.window, text=self.ip1_case, font=('Aerial 11'),fg="red", width=20, height=1).grid(row=1,column=5)

    self.ip2_case = "Enter the input file" if (self.ip2 == "") else ""
    Label(self.window, text=self.ip2_case, font=('Aerial 11'),fg="red", width=20, height=1).grid(row=2,column=5)

    if ((self.ip1_case == "") and (self.ip2_case == "")):
      try:
        
        #The data from the fields are being passed to the class "synonym_sentence_generator"
        self.cons = sentence_validator.synonym_sentence_generator(self.ip1,self.ip2)
        
        # Validate method is being called by the object and the result is returned to the below variable.
        self.op = self.cons.validate()
        
        # The result is converted to a message and rendered in the GUI at the mentioned grid position.
        self.op_diplay = Label (self.window, text="Most Synonomical Sentence : " + str(self.op), wraplength=500, font=('Aerial 11'), width=60, justify=LEFT)
        self.op_diplay.grid(row=4,column=0, columnspan = 6, padx=10, pady=20)
     
      #To catch the runtime error and display in a messagebox
      except Exception as e:
        messagebox.showerror('Python Error', e)


# Creation and render of the GUI frame
root = Tk()
root.title('Synonymous Sentence Finder')
root.geometry("700x350")
root.resizable(False, False)
clacal = gui(root)

root.mainloop()