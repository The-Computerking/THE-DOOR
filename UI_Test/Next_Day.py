from tkinter import *
import subprocess


def d(): root.destroy()
def n(): 
    root.destroy()
    subprocess.run("python UI_Test/Found_Creature.py", shell=True)

root = Tk()
root.geometry("800x800")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

doortxt = Label(frame, text=f"you come back the next day").grid(column=0, row=0)
doortxt = Label(frame, text=f"do you want to enter again?").grid(column=0, row=1)
button1 = Button(leftframe, text="YES", command=n).grid(column=0, row=2)
button3 = Button(leftframe, text="NO", command=d).grid(column=0, row=3)



root.title("Test")
root.mainloop()