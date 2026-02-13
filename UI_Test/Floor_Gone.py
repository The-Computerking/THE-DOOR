from tkinter import *
import subprocess


def d(): root.destroy()
def n(): 
    root.destroy()
    subprocess.run("python UI_Test/Second_Floor", shell=True)

root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

doortxt = Label(frame, text=f"you killed it").grid(column=0, row=0)
label = Label(frame, text="the floor disapears do you want to jump down?",).grid(column=0, row=1)
button1 = Button(leftframe, text="YES", command=n, bg="grey15", fg="white", bd=0).grid(column=0, row=2)
button2 = Button(leftframe, text="NO", command=d, bg="grey15", fg="white", bd=0).grid(column=0, row=3)



root.title("Test")
root.mainloop()