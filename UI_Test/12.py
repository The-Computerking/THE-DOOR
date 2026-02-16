from tkinter import *
import tkinter as tk
import subprocess


def a(event): 
    ans = ans_var.get()
    print(ans)
    if ans == "chest":
        root.destroy()
        subprocess.run("python UI_Test/Death_Screen.py", shell=True)
    elif ans == "leave":
        root.destroy()
    elif ans == "fight":
        root.destroy()
        subprocess.run("python UI_Test/13.py", shell=True)


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label1 = Label(frame, text="inside is a sleeping arachnid and a chest", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
label2 = Label(frame, text="do you want to fight the arachnid, open the chest or leave?", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
entry1 = Entry(frame, textvariable=ans_var, bg="grey12", fg="white", bd=0)
entry1.grid(column=0, row=2)
entry1.bind("<Return>", a)

root.title("12")
root.mainloop()