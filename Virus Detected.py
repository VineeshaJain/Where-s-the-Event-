from tkinter import *
from tkinter import messagebox 
root = Tk()
root.geometry("200x200")
def mesg():
    messagebox.showwarning("Alert ⚠️","Stop the Virus!! 🦠")

button = Button(root, text = "Scan for Virus 👾", command = mesg)
button.place(x=40, y=80)
root.mainloop()
