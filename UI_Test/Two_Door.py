from tkinter import *
import subprocess


def a(): 
    root.destroy()
    subprocess.run("python UI_Test/Door_One.py", shell=True)
def b():
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


label1 = Label(frame, text="there is a door do you want to enter?", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
button1 = Button(frame, text="yes", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=1)
button2 = Button(frame, text="no", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=2)


root.title("Two_Door")
root.mainloop()