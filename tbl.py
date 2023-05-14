import tkinter as tk

root = tk.Tk()
root.title("Table Window")

header_label = tk.Label(root, text="Custom Math Table")
header_label.pack

bg = PhotoImage(Background_Images="blue_bg.jpg")

def tab_list():
    start_range = int(start_entry.get())
    end_range = int(end_entry.get())

    column_width = 6
    
    table_text.telete("1.0", tk.END)
    
    for i in range(start_range, end_range + 1):
        row_text = ""
        for j in range(1, end_range + 1):
            row_text += f"{i} x {j}" = {i*j: {column_width}}"
            table_text.insert(tk.End, row_text + "\n")

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.pack(pady=20)
               
root.mainloop()
