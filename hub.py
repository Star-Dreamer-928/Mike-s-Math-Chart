import subprocess
import tkinter as tk

root = tk.Tk()
root.title("Hub Window")

bg = PhotoImage(Background_Images = "orange_bg.jpg")

header_label = tk.Label(root, text="Mike's Maginificent Math Mechanics")
header_label.pack

def runscript1():
    subprocess(["python", "path/to/addition.py"])

def runscript2():
    subprocess(["python", "path/to/subtraction.py"])

def runscript3():
    subprocess(["python", "path/to/multiplication.py"])

def runscript4():
    subprocess(["python", "path/to/divide.py"])

def runscript5():
    subprocess(["python", "path/to/table.py"])

button1 = tk.Button(root, text="Addition", command=runscript1)
button1.pack()

button2 = tk.Button(root, text="Subtraction", command=runscript2)
button2.pack()

button3 = tk.Button(root, text="Multiplication", command=runscript3)
button3.pack()

button4 = tk.Button(root, text="Division", command=runscript4)
button4.pack()

button5 = tk.Button(root, text="Math Table", command=runscript5)
button5.pack()

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)

root.mainloop()
