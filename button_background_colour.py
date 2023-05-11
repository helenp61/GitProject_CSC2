from tkinter import *

root = Tk()
root.geometry('400x150')
root.title('PythonExamples.org - Tkinter Example')

button = Button(root, text='Submit', bg='#4444ff',
                activebackground='red')
button.pack()

root.mainloop()
