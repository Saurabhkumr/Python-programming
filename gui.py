# from tkinter import *
# root=Tk()
# root.geometry('500x500')
# root.minsize(100,200)
# root.maxsize(1200,1200)

# # photo = PhotoImage(file="img.jpg")
# # l=Label(image=photo)
# l1 =Label(text="hello world", bg="blue",fg="white",font="Timesroman 50 bold",borderwidth=5, relief=SUNKEN, padx=50,pady=20)
# l1.pack()
# # l.pack()
# mainloop()


import tkinter as tk

def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Addition Calculator")

# Create entry fields
entry1_label = tk.Label(root, text="Enter first number:")
entry1_label.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2_label = tk.Label(root, text="Enter second number:")
entry2_label.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create a button to trigger addition
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=2, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
