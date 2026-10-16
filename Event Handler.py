from tkinter import *

window = Tk()
window.geometry("100x100")

window.configure(bg = "lightpink")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

Button = Button(text = "Click me ")
Button.pack()

Button.bind("<Button-1>", handle_click)

window.mainloop()