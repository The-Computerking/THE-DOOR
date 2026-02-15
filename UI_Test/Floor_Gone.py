from tkinter import *
import subprocess


def a(): 
    root.destroy()
    subprocess.run("python UI_Test/Second_Floor.py", shell=True)
def b(): 
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


laebl1 = Label(frame, text="you killed it", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
label2 = Label(frame, text="the floor disapears do you want to jump down?", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
button1 = Button(frame, text="YES", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=2)
button2 = Button(frame, text="NO", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=3)


root.title("Floor_Gone")
root.mainloop()