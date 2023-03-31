from tkinter import *
import tkinter.messagebox as msgbx
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import randint,choice, shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = (web_input.get()).title()
    email = email_input.get()
    pswrd = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pswrd,
        }
    }

    if len(website) == 0 or len(pswrd) == 0:
        msgbx.showinfo(title="Oops", message="Please don't leave any fields empty!")
    
    else:
        try:
            with open('29-Day-Password-Manager/data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("29-Day-Password-Manager/data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("29-Day-Password-Manager/data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    search_web = (web_input.get()).title()
    try:
        with open('29-Day-Password-Manager/data.json', 'r') as data_file:
            data = json.load(data_file)
    except:
        msgbx.showinfo(title="Error", message="No Data File Found")

    else:
        if search_web in data.keys(): 
            email = data[search_web]["email"]
            password = data[search_web]["password"]
            msgbx.showinfo(title=search_web, message=f"Email: {email} \n Password: {password}")

        else:
            msgbx.showinfo(title="Error", message=f"No details for {search_web} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="29-Day-Password-Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# LABELS
web_label = Label(text="Website", font=("Arial", 10))
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", font=("Arial", 10))
email_label.grid(column=0, row=2)
pass_label = Label(text="Password", font=("Arial", 10))
pass_label.grid(column=0, row=3)


# ENTRIES
web_input = Entry(width=30)
web_input.grid(column=1, row=1, columnspan=2, sticky='w')
web_input.focus()
email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "mk8898765@gmail.com" )
pass_input = Entry(width=30)
pass_input.grid(column=1, row=3, sticky='w')


# BUTTONS
search_button = Button(text="Search",width=14, command=find_password)
search_button.grid(column=2, row=1)
generate_pass = Button(text="Generate Password", command= generate_password)
generate_pass.grid(column=2, row=3)
add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()