import tkinter as tk
from random import choice

root = tk.Tk()
# root.geometry("400x250")
root.title("Images in Tkinter")

heading = tk.Label(text="Image Button Demo", font=("Roboto", 28), pady=15)
heading.pack()

# import the image using PhotoImage function
sunset3_jpg = tk.PhotoImage(file='sunset3.jpg')

# button function


def play():
    msg.config(text="button pressed")


# create buttons and pass the image in
button_r = tk.Button(root, image=sunset3_jpg, command=play)
button_r.pack()

# message label
msg = tk.Label(root, text="Beautiful end of day?",
               font=("Roboto", 22), pady=25)
msg.pack()

root.mainloop()
