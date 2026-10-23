from tkinter import *
root = Tk()
root.geometry('400x400')
root.configure(bg = 'orange')

def top():
    top = Toplevel()
    top.geometry('150x150')
    top.configure(bg = "cyan")
    Label1 = Label(top,text = ' Top level window')
    Label1.place(x =20,y = 20)

button1 = Button(root,text = 'Top level window' , width = 20, command = top )
button1.place(x = 150,y = 200)

root.mainloop()