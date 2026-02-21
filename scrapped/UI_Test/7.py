from tkinter import *
import tkinter as tk
import subprocess
from rn import skinrandom
from rn import clawrandom
from rn import clawsharpnessrandom
from rn import creaturerandom
from descrypters import skin
from descrypters import teeth
from descrypters import clawsharpness
from descrypters import claws


def a(event): 
    ans = ans_var.get()
    print(ans)
    if ans == "yes":
        root.destroy()
        subprocess.run("python UI_Test/8.py", shell=True)
    elif ans == "exit":
        root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label1 = Label(frame, text=f"you approach the creature and look closer its got {skin[skinrandom]} skin", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
label2 = Label(frame, text=f"and {teeth[skinrandom]} teeth and {claws[clawrandom]} {clawsharpness[clawsharpnessrandom]} claws", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
label3 = Label(frame, text="do you want to attack?", bg="grey15", fg="white", justify="left").grid(column=0, row=2)
entry1 = Entry(frame, textvariable=ans_var, bg="grey12", fg="white", bd=0)
entry1.grid(column=0, row=3)
entry1.bind("<Return>", a)



root.title("7")
root.mainloop()