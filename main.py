import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

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
    messagebox.showinfo(title="Password", message='Password copied to clipboard')


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        file = open('data.json')
    except FileNotFoundError:
        messagebox.showerror(title='DataBase not Found', message="There is no information to be found.")
    else:
        data = json.load(file)
        to_search = web_field.get().title()
        try:
            user = data[to_search]['email']
            password = data[to_search]['password']
        except KeyError:
            messagebox.showinfo(title='Site not Found', message='Check if the site name is correct.')
        else:
            hide_password = messagebox.askyesnocancel(title='Show info?', message='Do you want to show Password?',
                                                      detail='Your password will be copied to clipboard')
            if hide_password == None:
                pass
            elif hide_password == True:
                pyperclip.copy(password)
                email_field.insert(0, user)
                messagebox.showinfo(title=f'{to_search} informations.', message=f"Login: {user}\n"
                                                                                f"Password: {password}\n"
                                                                                f"\n Password copied to clipboard")
            elif hide_password == False:
                pyperclip.copy(password)
                email_field.insert(0, user)
                messagebox.showinfo(title=f'{to_search} informations.', message=f"Login: {user}\n"
                                                                                f"Password: Copied to clipboard")
    finally:
        file.close()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = web_field.get().title()
    email = email_field.get().lower()
    password = pass_field.get()
    new_data = {
        website_name: {
            'email': email,
            'password': password,
        }
    }

    if not (website_name != '' and email != '' and password != ''):
        messagebox.showerror(title='Error!', message="Couldn't get all the infos.")
    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_field.delete(0, 'end')
            pass_field.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# Gui
gui = Tk()
gui.title("Password Manager")
gui.config(pady=35, padx=35)
gui.resizable(FALSE, FALSE)
gui.geometry('460x380-300+200')

# Canvas
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)

# Labels
website_label = Label(text='Website:', padx=10, pady=3)
email_user_label = Label(text='Email/Username:', padx=10, pady=3)
password_label = Label(text='Password:', padx=10, pady=3)

# Entry Fields
web_field = Entry(width=25)
web_field.focus()
email_field = Entry(width=43)
pass_field = Entry(width=25)

# Buttons
generate_pass_bt = Button(text='Generate Password', font=('Arial', 8, 'normal'),
                          command=generate_passwords, width=16)
add_bt = Button(text='Add', width=36, command=save)
search = Button(text='Search', font=('Arial', 8, 'normal'), width=16, command=find_password)

# Grid
canvas.grid(row=0, column=0, columnspan=3)
website_label.grid(row=1, column=0)
email_user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

web_field.grid(row=1, column=1)
email_field.grid(row=2, column=1, columnspan=2)
pass_field.grid(row=3, column=1)

search.grid(row=1, column=2)
generate_pass_bt.grid(row=3, column=2)
add_bt.grid(row=4, column=1, columnspan=2)


gui.mainloop()
