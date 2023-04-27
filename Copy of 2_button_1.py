from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x400")
# some widgets available only in ttk
# and some in Tkinter
# we will see the difference here
# with the buttons


button1 = Button(root, text="Click Me!")  # button created using tkinter
button2 = ttk.Button(root, text="Click Me!")  # button created using ttk
# if you run it now you will see an empty GUI -
# thebuttons do not show up
# have to use geometry manager to be able
# to see the buttons
# here we will use .pack to show our buttons

button1.pack()
button2.pack()

"""we can also define the size of the window
i.e. the x and y value for our window 
this will be added just below your root which 
is above"""
root.mainloop()
