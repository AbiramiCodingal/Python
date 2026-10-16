from tkinter import *

window = Tk()
window.title("My first window")
window.geometry('450x350')
def login():
    name = entry1.get()
    text1.insert(END, "welcome  " + name + "you have sep a pin")

frame1 = Frame(window, width = 400, height = 250,bd = 2,relief = 'sunken',bg = 'skyblue')
frame1.place (x = 10,y = 10)
Label1 = Label(window,text= "Name", bg="navy", fg="white")
Label1.place(x= 100,y = 20)
entry1 = Entry(show = "*")
entry1.place(x= 200,y = 20)
Button1 = Button(window,text= 'Start', bg="navy", fg='white' , command=login)
Button1.place(x= 150,y = 50)
text1 = Text(frame1, width = 25 , height=7, fg= 'navy',bg= 'beige')
text1.place(x= 100,y = 70)
window.mainloop()