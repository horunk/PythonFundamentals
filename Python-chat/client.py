from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import messagebox
import tkinter
import time
import sys


def receive():
    while True:
        time.sleep(0.3)
        try:
            msg = client_socket.recv(SIZE).decode("utf8")
            message_list.insert(tkinter.END, msg)
            message_list.see("end")
        except:
            break


def send(event=None): 
    msg = message_box.get()
    message_box.set("")
    client_socket.send(bytes(msg, "utf8"))


def exitProgram():
    if messagebox.askyesno("Are you sure?", "Are you sure you wish to close the program?"):
        message_box.set("$closeconnection")
        time.sleep(0.1)
        send()
        time.sleep(0.5)
        client_socket.close()
        time.sleep(0.5)
        top.quit()
        quit()
    else:
        return


def on_closing(event=None):
    exitProgram()

def showAbout():
    infoText = """
This is a simple Python based client-server chat application.

Done as a school classproject in Python Fundamentals class in year 2018 by horunk.
http://github.com/horunk 
"""

    #show infoText as a message box
    messagebox.showinfo("About this program", infoText)

################# BEGININNG OF GUI ################
# Create GUI
top = tkinter.Tk()
top.title("Python chat")
top.minsize(400, 400)

# Create Frame to contain GUI
main_frame = tkinter.Frame(top)
main_frame.pack(padx=3, pady=3, fill=BOTH, expand=True)

# Message list
message_box = tkinter.StringVar() 

scrollbar = tkinter.Scrollbar(main_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

message_list = tkinter.Listbox(main_frame, height=15, width=50, yscrollcommand=scrollbar.set)
message_list.pack(padx=3, pady=3, fill=BOTH, expand=True)

# Controls in bottom
entry_label=StringVar()
entry_label.set("Insert message here: ")
label1=Label(top,textvariable=entry_label, height=4)
label1.pack(side="left", padx=10)

entry_field = tkinter.Entry(top, textvariable=message_box)
entry_field.bind("<Return>", send)
entry_field.pack(side="left", expand=True, fill=X, padx=10)

send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack(side="left", padx=10)

# Create menu bar
menuBar = Menu(top)
top.config(menu = menuBar)

# Create file menu structure
fileMenu = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_command(label = 'Exit', command = exitProgram)

# Create help menu structure
helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label = 'About', command = showAbout)
menuBar.add_cascade(label = 'Help', menu = helpMenu)

top.protocol("WM_DELETE_WINDOW", on_closing)
################# END OF GUI ################

# Connection parameters
HOST = "localhost"
PORT = 6666
SIZE = 4096
ADDRESS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)

receive_thread = Thread(target=receive)
receive_thread.start()

# Start GUI
tkinter.mainloop()