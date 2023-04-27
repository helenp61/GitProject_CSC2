from tkinter import *


root = Tk()
root.title('Set Image as Background')
root.geometry("800x500")

# Define Image
bg = PhotoImage(file="Images/grass.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add something to the top of our image
my_text = Label(root, text="Welcome!", font=("Helvetica", 50), fg="black")
my_text.pack(pady=50)

# Add some buttons
my_button1 = Button(root, text="Exit")


root.mainloop()
