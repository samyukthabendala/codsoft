import random
import string
from tkinter import*

def generate_password():
    password =""
    length = int(length_input.get())
    if include_uppercase.get():
        password +=random.choice(string.ascii_uppercase)
    if include_lowercase.get():
        password +=random.choice(string.ascii_lowercase)
    if include_digits.get():
        password += random.choices(string.digits)
    if include_symbols.get():
        password +=random.choice(string.punctuation)
    while len(password)<length:
        password += random.choice(string.ascii_letters+string.digits+string.punctuation)
        password_display.delete(0,END)
        password_display.insert(0,password)

root = Tk()
root.title("Password Generator")

length_label = Label(root, text="Length:")
length_label.grid(row=0, column=0)

length_input = Entry(root, width=10)
length_input.grid(row=0, column=1)

include_uppercase = BooleanVar()
uppercase_check = Checkbutton(root, text="include uppercase",variable=include_uppercase)
uppercase_check.grid(row=1, column=0)

include_lowercase = BooleanVar()
lowercase_check = Checkbutton(root, text="include Lowercase", variable=include_lowercase)
lowercase_check.grid(row=2, column=0)

include_digits = BooleanVar()
digits_check = Checkbutton(root, text="include Digits", variable=include_digits)
digits_check.grid(row=3, column=0)

include_symbols = BooleanVar()
symbols_check = Checkbutton(root, text="include symbols", variable=include_symbols)
symbols_check.grid(row=4, column=0)

generate_button = Button(root, text="Generate Password",command=generate_password)
generate_button.grid(row=5, column=0)

password_display = Entry(root, width=20)
password_display.grid(row=6, column=0)

root.mainloop()