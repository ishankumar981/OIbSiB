import random
import string
from tkinter import *

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for i in range(length))

    output.delete(0, END)
    output.insert(0, password)

root = Tk()
root.title("Random Password Generator")
root.geometry("350x220")

Label(root, text="Password Length").pack(pady=10)

length_entry = Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

Button(root, text="Generate Password", command=generate_password).pack(pady=10)

output = Entry(root, width=35)
output.pack()

root.mainloop()
