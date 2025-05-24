
#create new page
import tkinter
from tkinter import *
import sqlite3


#this creates a new database for the user logins
def create_new_account():
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

#all of these columns are added to the database
    c.execute('''  CREATE TABLE IF NOT EXISTS details
    (first_name VARCHAR(255), 
    last_name VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255),
    re_password VARCHAR(255),
    security_question VARCHAR(255),
    answer VARCHAR(255)
    )
    ''')
    conn.close()


create_new_account()

#below are several error box messages
#these would be displayed when there is an error anywhere
def invalid_message1():
    global pop
    pop = Toplevel(create_acc_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid input "
                                    )
    pop_label.pack()

def missing_entry():
    global pop2
    pop2 = Toplevel(create_acc_window)
    pop2.title("Error")
    pop2.geometry("200x150")
    pop2.config(bg="#4EB168")

    pop2_label = Label(pop2, text=" Entry missing "
                                    )
    pop2_label.pack()

def max_char():
    global pop3
    pop3 = Toplevel(create_acc_window)
    pop3.title("Error")
    pop3.geometry("200x150")
    pop3.config(bg="#4EB168")

    pop3_label = Label(pop3, text="The max character length is 10 "
                                    )
    pop3_label.pack()

def select():
    global pop4
    pop4 = Toplevel(create_acc_window)
    pop4.title("Error")
    pop4.geometry("200x150")
    pop4.config(bg="#4EB168")

    pop4_label = Label(pop4, text="Please select an option"
                                    )
    pop4_label.pack()

def password_match():
    global pop5
    pop5 = Toplevel(create_acc_window)
    pop5.title("Error")
    pop5.geometry("200x150")
    pop5.config(bg="#4EB168")

    pop5_label = Label(pop5, text="The passwords do not match"
                                    )
    pop5_label.pack()

def Digit_error():
    global pop6
    pop6 = Toplevel(create_acc_window)
    pop6.title("Error")
    pop6.geometry("200x150")
    pop6.config(bg="#4EB168")

    pop6_label = Label(pop6, text="Invalid input type: Integer"
                                    )
    pop6_label.pack()

def special_error():
    global pop7
    pop7 = Toplevel(create_acc_window)
    pop7.title("Error")
    pop7.geometry("200x150")
    pop7.config(bg="#4EB168")

    pop7_label = Label(pop7, text="Invalid input type: Special character"
                                    )
    pop7_label.pack()

#this is the validation function
#this checks the inputs them and regulates them based on certain criteria
#if they do not meet the criteria there is an error message
#if they meet the criteria the new account details are stored in the database
def check2():
    if first_name.get() == "" or first_name.get() == " ":
        missing_entry()
    elif last_name.get() == "" or last_name.get() == " ":
        missing_entry()
    elif new_username.get() == "" or new_username.get() == " ":
        missing_entry()
    elif new_password.get() == "" or new_password.get() == " ":
        missing_entry()
    elif re_enter_password.get() == "" or re_enter_password.get() == " ":
        missing_entry()
    elif security_answer.get() == "" or security_answer.get() == " ":
        missing_entry()
    elif len(first_name.get()) > 10:
        max_char()
    elif len(last_name.get()) > 10:
        max_char()
    elif len(new_username.get()) > 10:
        max_char()
    elif len(new_password.get()) > 10:
        max_char()
    elif len(re_enter_password.get()) > 10:
        max_char()
    elif len(security_answer.get()) > 10:
        max_char()
    elif clicked.get() == "--select--":
        select()
    elif re_enter_password.get() != new_password.get():
        password_match()
    elif first_name.get().isdigit() == True:
        Digit_error()
    elif last_name.get().isdigit() == True:
        Digit_error()
    elif new_username.get().isalnum() == False:
        special_error()
    elif new_password.get().isalnum() == False:
        special_error()
    elif re_enter_password.get().isalnum() == False:
        special_error()
    else:
        add_details(first_name.get(), last_name.get(), new_username.get(),
                    new_password.get(), re_enter_password.get(),
                    clicked.get(), security_answer.get())




#this allows the user to input their details into the user login database
global add_details
def add_details(p1, p2, p3, p4, p5, p6, p7):
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    c.execute('''    INSERT OR IGNORE INTO details
    (first_name, last_name,username ,password ,re_password ,security_question ,answer)
    VALUES(?,?,?,?,?,?,?)''', (p1, p2, p3, p4, p5, p6, p7))
    conn.commit()
    conn.close()



#this page is displayed when the user clicks the "create new account" button on the login page
def create_account():
    global create_account
    global create_acc_window
    create_acc_window = Tk()
    create_acc_window.title("Create new account")
    create_acc_window.geometry("450x500")
    create_acc_window.config(bg="White")

    #these entry boxes would allow the user to enter their information
    def click(event):
        first_name.config(state=NORMAL)
        first_name.delete(0, END)

    def click1(event):
        last_name.config(state=NORMAL)
        last_name.delete(0, END)

    def click2(event):
        new_username.config(state=NORMAL)
        new_username.delete(0, END)

    def click3(event):
        new_password.config(state=NORMAL)
        new_password.delete(0, END)

    def click4(event):
        re_enter_password.config(state=NORMAL)
        re_enter_password.delete(0, END)

    def click5(event):
        security_answer.config(state=NORMAL)
        security_answer.delete(0, END)

    new = tkinter.Label(create_acc_window, fg="white", bg="#4EB168", text=("New account"), font=("Arial", 15))
    new.pack(pady=5)
    new.place(x=120, y=20)

    global first_name
    first_name = tkinter.Entry(create_acc_window, borderwidth=3)
    first_name.insert(0, "Enter new First Name")
    first_name.config(state=DISABLED)
    first_name.bind("<Button-1>", click)
    first_name.pack()
    first_name.place(x=120, y=70)

    global last_name
    last_name = tkinter.Entry(create_acc_window, borderwidth=3)
    last_name.insert(0, "Enter new Last Name")
    last_name.config(state=DISABLED)
    last_name.bind("<Button-1>", click1)
    last_name.pack()
    last_name.place(x=120, y=110)

    global new_username
    new_username = tkinter.Entry(create_acc_window, borderwidth=3)
    new_username.insert(0, "Enter new Username")
    new_username.config(state=DISABLED)
    new_username.bind("<Button-1>", click2)
    new_username.pack()
    new_username.place(x=120, y=150)

    global new_password
    new_password = tkinter.Entry(create_acc_window, borderwidth=3)
    new_password.insert(0, "Enter new Password")
    new_password.config(state=DISABLED)
    new_password.bind("<Button-1>", click3)
    new_password.pack()
    new_password.place(x=120, y=190)

    global re_enter_password
    re_enter_password = tkinter.Entry(create_acc_window, borderwidth=3)
    re_enter_password.insert(0, "Re-enter new Password")
    re_enter_password.config(state=DISABLED)
    re_enter_password.bind("<Button-1>", click4)
    re_enter_password.pack()
    re_enter_password.place(x=120, y=230)

    #this create button calls the add_details function using lambda to allow the inputs to be enterred into the database
    new_acc_button = tkinter.Button(create_acc_window, fg="white", bg="#4EB168", text="Create", height=1, width=5,
                                    command=check2)
    new_acc_button.pack(pady=25)
    new_acc_button.place(x=120, y=370)

    security = tkinter.Label(create_acc_window, text="For security reasons, and when password is forgotten", bg="white",
                             fg="black", font=('Open Sans', 8))
    security.place(x=120, y=260)

    #this gives a dropdown box that would allows the user several options to chose from
    def show():
        global drop_down
        global options
        drop_down.config(text=clicked.get())

    options = [
        "--select--",
        "Where was your first job?",
        "What was your first pets name?",
        "What was your top uni choice?"
    ]

    global clicked
    clicked = StringVar(create_acc_window)
    clicked.set("--select--")

    global drop_down
    drop = OptionMenu(create_acc_window, clicked, *options)
    drop.pack()
    drop.place(x=120, y=290)

    #this would hold the answer to whatever question the user selected above
    global security_answer
    security_answer = tkinter.Entry(create_acc_window, borderwidth=3)
    security_answer.insert(0, "Answer")
    security_answer.config(state=DISABLED)
    security_answer.bind("<Button-1>", click5)
    security_answer.pack()
    security_answer.place(x=120, y=330)

    #allows the user to exit the page by destroying the page
    exit1 = tkinter.Button(create_acc_window, fg="white", bg="#4EB168", text="Exit", height=1, width=5,
                           command=create_acc_window.destroy)
    exit1.pack()
    exit1.place(x=180, y=370)

    #the user is not allowed to use special characters as it would disrupt it saving to the database and the login
    # process
    special_characters = tkinter.Label(create_acc_window, text="Pls don't use special characters like * and _",
                                       bg="white", fg="black",
                                       font=('Open Sans', 8))
    special_characters.pack()
    special_characters.place(x=90, y=410)


    create_acc_window.mainloop()
