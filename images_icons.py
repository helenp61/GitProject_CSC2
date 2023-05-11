"""Tkinter has a built in system for using images and to use
real images like .jpg & .png. 
To do this we have to import another module called PIL (Python Image Library)
which is now old and does not work anymore. But has been improved and called
PILLOW(but still the PIL Module) """

from tkinter import *
from PIL import Image, ImageTk  # this is how we reference this
# We have to install pip from the terminal: pip install Pillow

root = Tk()
root.title('Images on GUI')
root.iconbitmap("Images/Apps-Python.png")

image1 = Image.open("robot.jpg")  # Define the image
my_label = Label(image=image1)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
