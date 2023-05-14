import tkinter as tk

root = tk.Tk()
root.title("Addition Window")

header_label = tk.Label(root, text="Addition")
header_label.pack

bg = PhotoImage(Background_Images="green_bg.jpg")

def add_numbers():
    num1 = int(input(entry1.get())
    num2 = int(input(entry2.get())
    result = num1 + num2
    
sum_label.config(text="Sum:" + str(result))

root = tk.Tk()
root.title("Addition")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack

sum_label = tk.Label(root, text="Sum: ")
sum_label.pack()

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)
               
root.mainloop()
