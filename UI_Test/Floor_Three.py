from tkinter import *
import subprocess


def a(): 
    root.destroy()
    subprocess.run("python UI_Test/", shell=True)
def b(): 
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


label1 = Label(frame, text="the floor colapses you fall to the next floor", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
label2 = Label(frame, text="WORK IN PROGRESS", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
button1 = Button(frame, text="EXIT", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=2)


root.title("Test")
root.mainloop()