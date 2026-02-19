from tkinter import *
import tkinter as tk
import subprocess
from Items import chestia
from rn import skinrandom
from rn import clawrandom
from rn import clawsharpnessrandom
from rn import creaturerandom
from descrypters import skin
from descrypters import teeth
from descrypters import clawsharpness
from descrypters import claws
from Items import chestia2
from Items import chestia3


def two(event):
    label1.config(text="do you want to enter the room")
    label2.config(text=" ")
    bind1 = entry1.bind("<Return>", three)


def three(event):
    label1.config(text="you see a chest do you want to open the chest")
    bind1 = entry1.bind("<Return>", four)


def four(event):
    label1.config(text=f"inside the chest is {chestia}")
    bind1 = entry1.bind("<Return>", five)


def five(event):
    label1.config(text="you come back the next day")
    label2.config(text="do you want to enter again?")
    bind1 = entry1.bind("<Return>", six)


def six(event):
    label1.config(text="inside you see a creature")
    label2.config(text="do you want to get a closer look at it?")
    bind1 = entry1.bind("<Return>", seven)


def seven(event):
    label1.config(text=f"you approach the creature and look closer its got {skin[skinrandom]} skin")
    label2.config(text=f"and {teeth[skinrandom]} teeth and {claws[clawrandom]} {clawsharpness[clawsharpnessrandom]} claws")
    label3.config(text="do you want to attack?")
    bind1 = entry1.bind("<Return>", eight)


def eight(event):
    label1.config(text="you killed it")
    label2.config(text="the floor disapears do you want to jump down?")
    label3.config(text=" ")
    bind1 = entry1.bind("<Return>", nine)


def nine(event):
    label1.config(text="you see a chest")
    label2.config(text="do you want to open the chest?")
    bind1 = entry1.bind("<Return>", ten)


def ten(event):
    label1.config(text=f"inside the chest is {chestia2}")
    label2.config(text=" ")
    bind1 = entry1.bind("<Return>", eleven)


def eleven(event):
    label1.config(text="there is a door do you want to enter?")
    bind1 = entry1.bind("<Return>", twelve)


# needs work
def twelve(event):
    label1.config(text="inside is a sleeping arachnid and a chest")
    label2.config(text="do you want to fight the arachnid, open the chest or leave?")
    bind1 = entry1.bind("<Return>", thirteen)


def thirteen(event):
    label1.config(text="you killed it")
    label2.config(text="do you want to open the chest?")
    bind1 = entry1.bind("<Return>", fourteen)


def fourteen(event):
    label1.config(text=f"inside the chest is {chestia3}")
    label2.config(text=" ")
    bind1 = entry1.bind("<Return>", fifteen)


def fifteen(event):
    label1.config(text="the floor colapses you fall to the next floor")
    label2.config(text="WORK IN PROGRESS")
    bind1 = entry1.bind("<Return>", )


root_one = Tk()
root_one.geometry("800x800")
frame = Frame(root_one, bg="grey15")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label1 = Label(frame, text="Hello welcome to the game", bg="grey15", fg="white", justify="left")
label1.grid(column=0, row=0)
label2 = Label(frame, text="do you want to open the door", bg="grey15", fg="white", justify="left")
label2.grid(column=0, row=1)
label3 = Label(frame, text=" ", bg="grey15", fg="white", justify="left")
label3.grid(column=0, row=2)
entry1 = Entry(frame, textvariable=ans_var, bg="grey12", fg="white", bd=0)
entry1.grid(column=0, row=3)
entry1.bind("<Return>", two)

root_one.title("1")
root_one.mainloop()
