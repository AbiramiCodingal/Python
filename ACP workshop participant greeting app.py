from tkinter import *

window = Tk()
window.title("Workshop participant greeting app")
window.geometry('400x400')

def login():
    name = entry1.get()
    text1.insert(END, "welcome to the Workshop " + name + " Hi, welcome to the Workshop participant Greeting app!!!") 

window.configure(bg="lightblue")
font = ("Arial",20,'bold')
lbl = Label(window,text= "Name", bg="lightpink", fg="black")
lbl.pack(pady=10)
entry1 = Entry()
entry1.pack(pady=10)
Button1 = Button(window,text= 'Start', bg="lightpink", fg='black' , command=login)
Button1.pack(pady=10)
text1 = Text(window, width = 25 , height=7, fg= 'white',bg= 'black')
text1.pack(padx=10)

window.mainloop()