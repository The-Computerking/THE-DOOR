from tkinter import *
import subprocess

def d(): root.destroy()
def n(): 
    root.destroy()
    subprocess.run("python UI_Test/Open_Chest.py", shell=True)

root = Tk()
root.geometry("1300x500")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

doortxt = Label(frame, text="do you want to enter the room").grid(column=0, row=0)
button1 = Button(leftframe, text="YES", command=n).grid(column=0, row=1)
button3 = Button(leftframe, text="NO", command=d).grid(column=0, row=2)



root.title("Test")
root.mainloop()
print("works")
