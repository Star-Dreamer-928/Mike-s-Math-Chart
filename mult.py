import tkinter as tk

root = tk.Tk()
root.title("Division Window")

header_label = tk.Label(root, text="Multiplication")
header_label.pack

bg = PhotoImage(Background_Images="blue2_bg.jpg")

def mul_numbers():
    num1 = int(input(entry1.get())
    num2 = int(input(entry2.get())
    result = num1 * num2
    
pro_label.config(text="product:" + str(result))

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

mul_button = tk.Button(root, text="Multiplication", command=mul_numbers)
mul_button.pack

pro_label = tk.Label(root, text="Multiply: ")
pro_label.pack()

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)

root.mainloop()
