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


label1 = Label(frame, text=f"you killed it").grid(column=0, row=0)
label2 = Label(frame, text=f"do you want to open the chest?").grid(column=0, row=1)
button1 = Button(frame, text="yes", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=2)
button2 = Button(frame, text="no", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=3)


root.title("Arachnid_Fight")
root.mainloop()