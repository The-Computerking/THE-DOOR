from tkinter import *
import subprocess



def a(): 
    root.destroy()
    subprocess.run("python UI_Test/Arachnid_Fight.py", shell=True)
def b(): 
    root.destroy()
    subprocess.run("python UI_Test/Death_Screen.py", shell=True)
def c(): 
    root.destroy()


root = Tk()
root.geometry("800x800")
frame = Frame(root, bg="grey15")
frame.place(relheight=1, relwidth=1)


label1 = Label(frame, text="inside is a sleeping arachnid and a chest", bg="grey15", fg="white", justify="left").grid(column=0, row=0)
laebl2 = Label(frame, text="do you want to fight the arachnid, open the chest or leave?", bg="grey15", fg="white", justify="left").grid(column=0, row=1)
button1 = Button(frame, text="fight", command=a, bg="grey15", fg="white", bd=0).grid(column=0, row=2)
button2 = Button(frame, text="chest", command=b, bg="grey15", fg="white", bd=0).grid(column=0, row=3)
button3 = Button(frame, text="leave", command=c, bg="grey15", fg="white", bd=0).grid(column=0, row=4)

root.title("Door_One")
root.mainloop()