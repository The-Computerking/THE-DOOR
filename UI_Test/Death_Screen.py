from tkinter import *
import subprocess


def a(): 
    root.destroy()
def b(): 
    root.destroy()
    subprocess.run("python UI_Test/", shell=True)
def c(): 
    root.destroy()
    subprocess.run("python UI_Test/", shell=True)

root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

text = Label(frame, text=f"YOU DIED").grid(column=0, row=0)
button1 = Button(leftframe, text="EXIT", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=1)



root.title("Test")
root.mainloop()