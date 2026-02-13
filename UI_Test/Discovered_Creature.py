from tkinter import *
import subprocess
from rn import skinrandom
from rn import clawrandom
from rn import clawsharpnessrandom
from rn import creaturerandom
from descrypters import skin
from descrypters import teeth
from descrypters import clawsharpness
from descrypters import claws

def d(): root.destroy()
def n(): 
    root.destroy()
    subprocess.run("python UI_Test/Floor_Gone.py", shell=True)

root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

doortxt = Label(frame, text=f"you approach the creature and look closer its got {skin[skinrandom]} skin").grid(column=0, row=0)
doortxt = Label(frame, text=f"and {teeth[skinrandom]} teeth and {claws[clawrandom]} {clawsharpness[clawsharpnessrandom]} claws").grid(column=0, row=1)
label = Label(frame, text="do you want to attack?",).grid(column=0, row=2)
button1 = Button(leftframe, text="YES", command=n, bg="grey15", fg="white", bd=0).grid(column=0, row=3)
button2 = Button(leftframe, text="NO", command=d, bg="grey15", fg="white", bd=0).grid(column=0, row=4)



root.title("Test")
root.mainloop()