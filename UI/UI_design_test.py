from tkinter import *
import tkinter as tk
import subprocess


root_one = Tk()
#root_one.attributes('-topmost',True)
root_one.geometry("800x800")

frame = Frame(root_one, bg="dark green")
frame.place(relheight=1, relwidth=1)


ans_var = tk.StringVar()


label4 = Label(text=">", bg="dark green", fg="green")
label4.grid(column=0, row=0)
label5 = Label(text=">", bg="dark green", fg="green")
label5.grid(column=0, row=1)
label6 = Label(text=">", bg="dark green", fg="green")
label6.grid(column=0, row=2)
label1 = Label(frame, text="    Hello welcome to the game", bg="dark green", fg="green")
label1.grid(column=1, row=0)
label2 = Label(frame, text="    please type load or new       ", bg="dark green", fg="green")
label2.grid(column=1, row=1)
label3 = Label(frame, text=">", bg="dark green", fg="green", justify="left")
label3.grid(column=1, row=2)


entry1 = Entry(frame, textvariable=ans_var, bg="green", fg="green", bd=0)
entry1.grid(column=1, row=2)
entry1.bind("<Return>")
#button = Button(text="exit", command=root_one.destroy, bg="dark green", fg="green")
#button.grid(column=0, row=5)


root_one.title("1")
root_one.mainloop()
