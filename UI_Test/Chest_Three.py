from tkinter import *
import subprocess
from Items import chestia3


def a(): 
    root.destroy()
    subprocess.run("python UI_Test/Floor_Three.py", shell=True)
def b(): 
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


label1 = Label(frame, text=f"inside the chest is {chestia3}", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
button1 = Button(frame, text="YES", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=1)
button2 = Button(frame, text="NO", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=2)


root.title("Chest_Three")
root.mainloop()