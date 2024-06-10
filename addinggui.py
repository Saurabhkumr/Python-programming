import tkinter as tk
from tkinter import messagebox

# Function to add two numbers and display the result
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Add Two Numbers")
window.geometry("300x200")

# Create and place the first entry
label1 = tk.Label(window, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Create and place the second entry
label2 = tk.Label(window, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Create and place the button
add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=5)

# Run the main event loop
window.mainloop()
