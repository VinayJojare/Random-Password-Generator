
import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    elif special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_num = False
    has_special = False

    while not meet_criteria or len(pwd) < length:
        new_chr = random.choice(characters)
        pwd += new_chr

        if new_chr in digits:
            has_num = True
        elif new_chr in special:
            has_special = True

        meet_criteria = True

        if numbers:
            meet_criteria = has_num
        elif special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd

def generate_password_click():
    length = int(length_entry.get())
    has_num = numbers_var.get()
    has_special = special_var.get()

    password = generate_password(length, has_num, has_special)
    password_display.config(text="Generated Password: " + password)
    messagebox.showinfo("Password Generated", "Password has been generated and displayed below.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create widgets
length_label = tk.Label(app, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(app, text="Include Special Characters", variable=special_var)
special_check.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password_click)
generate_button.pack()

password_display = tk.Label(app, text="Generated Password: ")
password_display.pack()

# Start the GUI main loop
app.mainloop()