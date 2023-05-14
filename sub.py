import tkinter as tk

root = tk.Tk()
root.title("Subtraction Window")

header_label = tk.Label(root, text="Subtraction")
header_label.pack

bg = PhotoImage(Background_Images="yellow_bg.jpg")

def sub_numbers():
    num1 = int(input(entry1.get())
    num2 = int(input(entry2.get())
    result = num1 - num2
    
rem_label.config(text="remainder:" + str(result))

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

sub_button = tk.Button(root, text="Subtract", command=add_numbers)
add_button.pack

rem_label = tk.Label(root, text="Subtract: ")
rem_label.pack()

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)

root.mainloop()
