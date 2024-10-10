from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle(event):
    print(event.char)

window.bind("<Key>", handle)

def click(event):
    print("The button has been clicked   🖱️")

button = Button(text="Click Me!   😊")
button.pack()
button.bind("<Button-1>", click)
window.mainloop()
