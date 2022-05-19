from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

import pyperclip
from pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_passwords():
    pass_field.delete(0, 'end')

    password_seed = []
    password_seed.extend([choice(LETTERS) for n in range(randint(6, 10))])
    password_seed.extend([choice(NUMBERS) for n in range(randint(2, 3))])
    password_seed.extend([choice(SYMBOLS) for n in range(randint(2, 4))])
    shuffle(password_seed)

    password = ''.join(password_seed)
    pyperclip.copy(password)
    pass_field.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website_name = web_field.get()
    email = email_field.get()
    password = pass_field.get()

    if not (website_name != '' and email != '' and password != ''):
        messagebox.showerror(title='Error!', message="Couldn't get all the infos.")

    else:
        is_ok = messagebox.askyesno(title=website_name, message=f"User: {email}\n Password: {password}\n"
                                                            f"Can I save it for you?")
        if is_ok:
            with open('data.txt', mode='a') as file:

                entry = f'{website_name} | {email} | {password}\n'
                file.write(entry)
            web_field.delete(0, 'end')
            pass_field.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
# Gui
gui = Tk()
gui.title("Password Manager")
gui.config(pady=40, padx=40)

# Canvas
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

# Labels
website_label = Label(text='Website:', padx=10, pady=2)
email_user_label = Label(text='Email/Username:', padx=10, pady=2)
password_label = Label(text='Password:', padx=10)

# Entry Fields
web_field = Entry(width=51)
web_field.focus()
email_field = Entry(width=51)
pass_field = Entry(width=30)

# Buttons
generate_pass_bt = Button(text='Generate Password', font=('Arial', 8, 'normal'), command=generate_passwords)
add_bt = Button(text='Add', width=43, command=save)

# Grid
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
email_user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

web_field.grid(row=1, column=1, columnspan=2)
email_field.grid(row=2, column=1, columnspan=2)
pass_field.grid(row=3, column=1, sticky='w')

generate_pass_bt.grid(row=3, column=2)
add_bt.grid(row=4, column=1, columnspan=2)


gui.mainloop()