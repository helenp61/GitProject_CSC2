from tkinter import *  # imports everything from TK - tkinter is a module
from tkinter import ttk  # ttk is a sub module of tkinter

root = Tk()  # top level window

# Create a Label Widget
label = Label(root, text="Hello Python")  # what you see
# on screen

# font colour, config is for properties
label.config(text="Hello Python",borderwidth=1,relief="solid",font="Times 32")
label.config(bg="yellow")  # background colour
#label.config(font='Times 20')

label.config(text='Python is a great program and we can do lots with it')
label.config(wraplength='150')  # wrap text if long label
label.config(justify="right")

# Showing it on the screen
label.pack()
root.geometry("300x250")

root.mainloop()  # GUI is always looping -
# when you run your mouse over and you can click on
# #any buttons/labels
