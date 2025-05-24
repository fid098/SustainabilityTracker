
# logins
import tkinter
from tkinter import *
from createnew import create_account
from forgotpass import forgot_pass
from foottrack import foot_track
from adminpage import admin  # allows me to call the admin function from the admin page
from progress import progress2  # allows me to call the progress2 function from the progress page
import sqlite3
import re  # allows me to rearrange text or replace text


# this function checks if the input from the admin login page is in the admin text document
# if the input is in the admin text document, it takes the user to the admin page
def acc_check2():
    global acc_check2
    login_check = 0
    cred_file2 = open("admin.txt", "r")  # opens the admin text document
    credentials2 = username2.get() + password2.get()

    file = cred_file2.read().splitlines()
    for l in file:
        if credentials2 == l:
            login_check = 1
            break

        elif credentials2 != l:
            login_check = 0
    if login_check == 1:
        admin()  # calls the admin function
    else:
        print("invalid login")
        invalid_message2()



#these are error box messages
#these are displayed when there is an error somewhere
def invalid_message1():
    global pop
    pop = Toplevel(user_login_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid input "
                                    )
    pop_label.pack()

def invalid_message2():
    global pop
    pop = Toplevel(admin_login_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid input "
                                    )
    pop_label.pack()

# this function checks if the input from the user login page is in the user login database
# if it is in the database, it will allow the user to either the progress or footprint tracking pages
def check():
    login_check_1 = 0
    login_check_2 = 0
    conn = sqlite3.connect("user_login_details.db")  # opens the user login database
    c = conn.cursor()

    for row1 in c.execute('''   SELECT username FROM details'''):  # this highlights all the usernames from the database

        newrow1 = re.sub("[^a-zA-Z0-9]",  # Search for all non-letters
                              "",  # Replace all non-letters with black spaces
                              str(row1))
        if username1.get() == newrow1:
            login_check_1 = 1
            break
        else:
            login_check_1 = 0

    for row2 in c.execute('''   SELECT password FROM details'''):
        newrow2 = re.sub("[^a-zA-Z0-9]",  # Search for all non-letters
                         "",  # Replace all non-letters with spaces
                         str(row2))
        if password1.get() == newrow2:
            login_check_2 = 1
            break
        else:
            login_check_2 = 0

    if login_check_1 == 1 and login_check_2 == 1:
       foot_track()
       print("valid input")
    elif login_check_1 == 0 and login_check_2 == 0:
       invalid_message1()
    elif login_check_1 == 1 and login_check_2 == 0:
        invalid_message1()
    elif login_check_1 == 0 and login_check_2 == 1:
        invalid_message1()


# this function checks if the input from the user login page is in the user login database
# if it is in the database, it will allow the user to either the progress or footprint tracking pages
def check2():
    login_check_1 = 0
    login_check_2 = 0
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    for row1 in c.execute('''   SELECT username FROM details'''):
        newrow1 = re.sub("[^a-zA-Z0-9]",  # Search for all non-letters
                              "",  # Replace all non-letters with black spaces
                              str(row1))
        if username1.get() == newrow1:
            login_check_1 = 1
            break
        else:
            login_check_1 = 0

    for row2 in c.execute('''   SELECT password FROM details  '''):
        newrow2 = re.sub("[^a-zA-Z0-9]",  # Search for all non-letters
                         "",  # Replace all non-letters with spaces
                         str(row2))
        if password1.get() == newrow2:
            login_check_2 = 1
            break

        else:
            login_check_2 = 0

    if login_check_1 == 1 and login_check_2 == 1:
       progress2()
    elif login_check_1 == 0 and login_check_2 == 0:
       invalid_message1()
    elif login_check_1 == 1 and login_check_2 == 0:
        invalid_message1()
    elif login_check_1 == 0 and login_check_2 == 1:
        invalid_message1()

#this function displays the user login page where the user inputs details in order to access progress or footprint pages
global user_login
def user_login():
    global user_login
    global user_login_window
    user_login_window = Tk()
    user_login_window.title("User Login")
    user_login_window.geometry("400x400")
    user_login_window.config(bg="white")


    def click(event):
        username1.config(state=NORMAL)
        username1.delete(0, END)

    def click1(event):
        password1.config(state=NORMAL)
        password1.delete(0, END)

#this label shows that it is a user login
    login1 = tkinter.Label(user_login_window, bg="white", fg="#4EB168", text="User Login", font=("Arial", 20))
    login1.pack(pady=5)
    login1.place(x=90, y=20)

    global username1
    username1 = tkinter.Entry(user_login_window, borderwidth=2)
    username1.insert(0, "Enter your username")
    username1.config(state=DISABLED)
    username1.bind("<Button-1>", click)
    username1.pack()
    username1.place(x=90, y=70)

    global password1
    password1 = tkinter.Entry(user_login_window, borderwidth=2)
    password1.insert(9, "Enter your password")
    password1.config(state=DISABLED)
    password1.bind("<Button-1>", click1)
    password1.pack()
    password1.place(x=90, y=110)

    login_button1 = tkinter.Button(user_login_window, fg="white", bg="#4EB168", text="footprint tracking", height=1,
                                   width=15, command=check)
    login_button1.pack(pady=25)
    login_button1.place(x=230, y=110)

    login_button2 = tkinter.Button(user_login_window, fg="white", bg="#4EB168", text="progress tracking", height=1,
                                   width=15, command=check2)
    login_button2.pack(pady=25)
    login_button2.place(x=230, y=70)

    create_button1 = tkinter.Button(user_login_window, fg="white", bg="#4EB168", text="Create new account", height=1,
                                    command=create_account)
    create_button1.pack()
    create_button1.place(x=90, y=150)

    exit_button1 = tkinter.Button(user_login_window, fg="white", bg="#4EB168", text="Exit", height=1, width=12,
                                  command=user_login_window.destroy)
    exit_button1.pack()
    exit_button1.place(x=230, y=150)

    forgotten_password = tkinter.Label(user_login_window, text="Forgotten password? ", bg="white", fg="black",
                                       font=('Open Sans', 10))
    forgotten_password.pack()
    forgotten_password.place(x=90, y=190)

    forgot_button = tkinter.Button(user_login_window, fg="white", bg="#4EB168", text="click here", height=1,
                                   command=forgot_pass)
    forgot_button.pack()
    forgot_button.place(x=230, y=190)

    special_characters = tkinter.Label(user_login_window, text="Pls don't use special characters like * and _", bg="white", fg="black",
                                       font=('Open Sans', 8))
    special_characters.pack()
    special_characters.place(x=90, y=280)

    user_login_window.mainloop()

#this function displays the admin login page where the admin can view all the user details
def admin_login():
    global admin_login
    global admin_login_window
    admin_login_window = Tk()
    admin_login_window.title("Admin login")
    admin_login_window.geometry("400x400")
    admin_login_window.config(bg="White")

    def click(event):
        username2.config(state=NORMAL)
        username2.delete(0, END)

    def click1(event):
        password2.config(state=NORMAL)
        password2.delete(0, END)

    # this label shows that it is a admin login
    login1 = tkinter.Label(admin_login_window, bg="white", fg="#4EB168", text="Admin Login", font=("Arial", 20))
    login1.pack(pady=5)
    login1.place(x=90, y=20)

    global username2
    username2 = tkinter.Entry(admin_login_window, borderwidth=2)
    username2.insert(0, "Enter your username")
    username2.config(state=DISABLED)
    username2.bind("<Button-1>", click)
    username2.pack()
    username2.place(x=90, y=70)

    global password2
    password2 = tkinter.Entry(admin_login_window, borderwidth=2)
    password2.insert(9, "Enter your password")
    password2.config(state=DISABLED)
    password2.bind("<Button-1>", click1)
    password2.pack()
    password2.place(x=90, y=110)

    login_button3 = tkinter.Button(admin_login_window, fg="white", bg="#4EB168", text="Ok", height=1,
                                   width=3, command=acc_check2)
    login_button3.pack(pady=25)
    login_button3.place(x=230, y=110)

    exit_button2 = tkinter.Button(admin_login_window, fg="white", bg="#4EB168", text="Exit", height=1, width=12,
                                  command=admin_login_window.destroy)
    exit_button2.pack()
    exit_button2.place(x=90, y=150)


    admin_login_window.mainloop()