from tkinter import *
from tkinter import ttk
import MessageProssesing

##### VARS #####
WIN_TITLE = 'Twitch Chat'

name1 = 'Kamui_Kazi'
mesg1 = 'Hi'
name2 = 'Kamui_Kazi'
mesg2 = 'Bye'

# Creating the Window vars
root = Tk()
root.title(WIN_TITLE)
root.grid()
    
nameLabel1 = ttk.Label(root, text=MessageProssesing.name_queue[0]).grid(column=0, row=0)
mesgLabel1 = ttk.Label(root, text=MessageProssesing.message_queue[0]).grid(column=1, row=0)
nameLabel2 = ttk.Label(root, text=MessageProssesing.name_queue[1]).grid(column=0, row=1)
mesgLabel2 = ttk.Label(root, text=MessageProssesing.message_queue[1]).grid(column=1, row=1)

""" nameLabel1 = ttk.Label(root, text=name1).grid(column=0, row=0)
mesgLabel1 = ttk.Label(root, text=mesg1).grid(column=1, row=0)
nameLabel2 = ttk.Label(root, text=name2).grid(column=0, row=1)
mesgLabel2 = ttk.Label(root, text=mesg2).grid(column=1, row=1) """

go = ttk.Button(root, text="Update", command=lambda: MessageProssesing.handle_message()).grid(column=0, row=2)

root.mainloop()