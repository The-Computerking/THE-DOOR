from tkinter import *
import tkinter as tk
import subprocess
from Items import chestia2


def a(event): 
    ans = ans_var.get()
    print(ans)
    if ans == "yes":
        root.destroy()
        subprocess.run("python UI_Test/11.py", shell=True)
    elif ans == "exit":
        root.destroy()

root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label1 = Label(frame, text=f"inside the chest is {chestia2}", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
entry1 = Entry(frame, textvariable=ans_var, bg="grey12", fg="white", bd=0)
entry1.grid(column=0, row=1)
entry1.bind("<Return>", a)


root.title("10")
root.mainloop()