from tkinter import *
import tkinter.scrolledtext as scrl
from tkinter import messagebox
import tkinter.filedialog as tkfd

################## BEGINNING OF FUNCTIONS ##################
def showAbout():
    infoText = """
This program is a simple example how to use Python 3 to mimic the basic functionality of Windows Notepad.

The program only implements the basic functions as inserting or editing text, together with options to save result to a file or open existing text file.

Done as a school classproject in Python Fundamentals class in year 2018 by horunk.
http://github.com/horunk 
"""

    #show infoText as a message box
    messagebox.showinfo("About this program", infoText)


# save file function
def saveAs():
    #get content of textarea
    fileContent = content.get(1.0, END)

    #get file path
    fileName = tkfd.asksaveasfile(mode='w', defaultextension=".txt", filetypes=(("Text file", "*.txt"),("All Files", "*.*") ))

    #save to file
    if fileName:
        fileName.write(fileContent)
        fileName.close()

# open file function
def openFile():
    #open file
    file = tkfd.askopenfile(mode='r')
    #read the contents of the file to var
    fileContent = file.read()

    #clear current content and load new content from var
    content.delete(1.0,END)
    content.insert(1.0,fileContent)
    # 1.0 means line one, character 0, which means the start

def exitProgram():
    if messagebox.askyesno("Are you sure?", "Are you sure you wish to close the program? \nALL UNSAVED CHANGES WILL BE LOST."):
        root.destroy()
    else:
        return


################## END OF FUNCTIONS ##################

################## BEGINNING OF GUI ##################
#Define root object and parameters
root = Tk()
root.title("Python Notepad")
root.geometry("640x480")

#create frame to hold content
frame1 = Frame(
    master = root
)
frame1.pack(fill='both', expand='yes')

#create ScrolledText object for text content
content = scrl.ScrolledText(master = frame1, wrap = WORD, width = 200, height  = 100)
content.pack(padx=3, pady=3, fill=BOTH, expand=True)

#create menu bar
menuBar = Menu(root)
root.config(menu = menuBar)

#create file menu structure
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'Open a file...', command = openFile)
fileMenu.add_command(label = 'Save to a file...', command = saveAs)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = exitProgram)

#create help menu structure
helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label = 'About', command = showAbout)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

################## END OF GUI ##################

#run GUI
root.mainloop()

