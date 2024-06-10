from tkinter import *
from tkinter import messagebox

# Create main window
window = Tk()
window.geometry('400x600')
window.title("Tkinter Example with Menus and Dialogs")

# Add labels
l1 = Label(window, text="First label", background='red')
l2 = Label(window, text="Second label", background='blue')
l3 = Label(window, text="Third label", background='green')

# Create buttons
button = Button(window, text="Click Me")

# Create checkboxes
cb1 = Checkbutton(window, text="Option 1", onvalue="Option 1", offvalue="")
cb2 = Checkbutton(window, text="Option 2", onvalue="Option 2", offvalue="")

# Create radio buttons
radio_var = StringVar()
rb1 = Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
rb2 = Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")

# Create a list box
listbox = Listbox(window, selectmode=MULTIPLE)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(END, item)

# Position widgets
# l1.pack(side='top', fill='x')
# l2.pack(side='top', expand=True)
# l3.pack(side='top', expand=True, fill='both')
# button.pack(side='top')
cb1.pack()
cb2.pack()
rb1.pack()
rb2.pack()
listbox.pack()

# Define menu callback functions
def show_info():
    messagebox.showinfo("Information", "This is an info message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    response = messagebox.askquestion("Question", "Do you like Python?")
    if response == 'yes':
        messagebox.showinfo("Response", "Great!")
    else:
        messagebox.showinfo("Response", "Too bad!")

# Create menu bar
menu_bar = Menu(window)

# Create File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Info", command=show_info)
file_menu.add_command(label="Warning", command=show_warning)
file_menu.add_command(label="Error", command=show_error)
file_menu.add_command(label="Question", command=ask_question)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Add File menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Set the menu bar as the window's menu
window.config(menu=menu_bar)



#dialog

def show_info():
    messagebox.showinfo("Information", "This is an info message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    response = messagebox.askquestion("Question", "Do you like Python?")
    label.config(text="Response: " + response)

# Create buttons to trigger dialog boxes
Button(window, text="Show Info", command=show_info).pack()
Button(window, text="Show Warning", command=show_warning).pack()
Button(window, text="Show Error", command=show_error).pack()
Button(window, text="Ask Question", command=ask_question).pack()

label = Label(window, text="")
label.pack()



# Start main loop
window.mainloop()
