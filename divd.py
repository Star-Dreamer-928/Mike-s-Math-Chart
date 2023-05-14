import tkinter as tk

root = tk.Tk()
root.title("Division Window")

header_label = tk.Label(root, text="Division")
header_label.pack

bg = PhotoImage(Background_Images="red_bg.jpg")

def div_numbers():
    num1 = int(input(entry1.get())
    num2 = int(input(entry2.get())
    result = num1 / num2
    
qot_label.config(text="qoutient:" + str(result))

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

div_button = tk.Button(root, text="Division", command=div_numbers)
div_button.pack

qot_label = tk.Label(root, text="Divide: ")
qot_label.pack()

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)

root.mainloop()
