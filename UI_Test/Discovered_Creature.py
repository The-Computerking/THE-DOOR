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


def a(): 
    root.destroy()
    subprocess.run("python UI_Test/Floor_Gone.py", shell=True)
def b(): 
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


label1 = Label(frame, text=f"you approach the creature and look closer its got {skin[skinrandom]} skin").grid(column=0, row=0)
label2 = Label(frame, text=f"and {teeth[skinrandom]} teeth and {claws[clawrandom]} {clawsharpness[clawsharpnessrandom]} claws").grid(column=0, row=1)
label3 = Label(frame, text="do you want to attack?",).grid(column=0, row=2)
button1 = Button(frame, text="YES", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=3)
button2 = Button(frame, text="NO", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=4)


root.title("Discovered_Creature")
root.mainloop()