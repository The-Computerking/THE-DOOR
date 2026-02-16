from tkinter import *
import tkinter as tk
import subprocess


def a(event):
    ans = ans_var.get()
    print(ans)
    if ans == "yes":
        root.destroy()
        subprocess.run("python UI_Test/2.py", shell=True)
    elif ans == "exit":
        root.destroy()



root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label1 = Label(frame, text="Hello welcome to the game", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
label2 = Label(frame, text="do you want to open the door", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
entry1 = Entry(frame, textvariable=ans_var, bg="grey12", fg="white", bd=0)
entry1.grid(column=0, row=2)
entry1.bind("<Return>", a)

root.title("1")
root.mainloop()