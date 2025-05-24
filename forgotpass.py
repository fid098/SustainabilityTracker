
# forgot password
import tkinter
from tkinter import *
import sqlite3
import re  # allows me to use the re module

#this function allows the user to update their password in the case where they forget their password
global update
def update():
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    for row in c.execute('''SELECT username FROM details WHERE username = "%s"''' % (username3.get())):
        newrow = re.sub("[^a-zA-Z0-9]",  # Search for all non-letters
                         "",  # Replace all non-letters with black spaces
                         str(row))

        #this changes the old password to the new one
        c.execute(''' UPDATE details SET password = "%s" WHERE username = "%s"''' % (re_newpass1.get(), username3.get()))
        c.execute(''' UPDATE details SET re_password =  "%s" WHERE username = "%s"''' % (re_newpass1.get(), username3.get()))

    conn.commit()

    c.close()

#these are error box messages
#these are displayed when there is an error somewhere
def invalid_message1():
    global pop
    pop = Toplevel(forgot_pass_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid Username "
                                    )
    pop_label.pack()

def missing_entry():
    global pop2
    pop2 = Toplevel(forgot_pass_window)
    pop2.title("Error")
    pop2.geometry("200x150")
    pop2.config(bg="#4EB168")

    pop2_label = Label(pop2, text=" Entry missing "
                                    )
    pop2_label.pack()

def max_char():
    global pop3
    pop3 = Toplevel(forgot_pass_window)
    pop3.title("Error")
    pop3.geometry("200x150")
    pop3.config(bg="#4EB168")

    pop3_label = Label(pop3, text="The max character length is 10 "
                                    )
    pop3_label.pack()

def select():
    global pop4
    pop4 = Toplevel(forgot_pass_window)
    pop4.title("Error")
    pop4.geometry("200x150")
    pop4.config(bg="#4EB168")

    pop4_label = Label(pop4, text="Please select an option"
                                    )
    pop4_label.pack()

def password_match():
    global pop5
    pop5 = Toplevel(forgot_pass_window)
    pop5.title("Error")
    pop5.geometry("200x150")
    pop5.config(bg="#4EB168")

    pop5_label = Label(pop5, text="The passwords do not match"
                                    )
    pop5_label.pack()

def Digit_error():
    global pop6
    pop6 = Toplevel(forgot_pass_window)
    pop6.title("Error")
    pop6.geometry("200x150")
    pop6.config(bg="#4EB168")

    pop6_label = Label(pop6, text="Invalid input type: Integer"
                                    )
    pop6_label.pack()

def invalid_message2():
    global pop7
    pop7 = Toplevel(forgot_pass_window)
    pop7.title("Error")
    pop7.geometry("200x150")
    pop7.config(bg="#4EB168")

    pop7_label = Label(pop7, text="Wrong security question"
                                    )
    pop7_label.pack()

def invalid_message3():
    global pop8
    pop8 = Toplevel(forgot_pass_window)
    pop8.title("Error")
    pop8.geometry("200x150")
    pop8.config(bg="#4EB168")

    pop8_label = Label(pop8, text="Wrong security answer"
                                    )
    pop8_label.pack()

#this is the validation function
#this checks the inputs them and regulates them based on certain criteria
#if they do not meet the criteria there is an error message
#if they meet the criteria the password changes
def check():
    if username3.get() == " " or username3.get() == "":
        print("empty field")
        missing_entry()
    elif clicked7.get() == "--select--":
        print("please select an option")
        select()
    elif security_question_answer.get() == "" or security_question_answer.get() == " ":
        print("empty field")
        missing_entry()
    elif newpass1.get() == "" or newpass1.get() == " ":
        print("empty field")
        missing_entry()
    elif re_newpass1.get() == "" or re_newpass1.get() == " ":
        print("empty field")
        missing_entry()
    elif re_newpass1.get() != newpass1.get():
        print("the passwords do not match")
        password_match()
    elif username3.get().isdigit == True:
        Digit_error()
    elif security_question_answer.get().isdigit == True:
        Digit_error()
    elif newpass1.get().isdigit == True:
        Digit_error()
    elif re_newpass1.get().isdigit == True:
        Digit_error()
    else:
        input_check()

#this checks if the inputs entered are in the the database
#before the password is changed
def input_check():
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    for row2 in c.execute('''   SELECT username, security_question, answer
             FROM details   '''):

        if username3.get() == row2[0] and clicked7.get() == row2[1] and security_question_answer.get() == row2[2]:
            a = 1
        elif username3.get() != row2[0] and clicked7.get() == row2[1] and security_question_answer.get() == row2[2]:
            b = 1
        elif username3.get() == row2[0] and clicked7.get() != row2[1] and security_question_answer.get() == row2[2]:
            c = 1
        elif username3.get() == row2[0] and clicked7.get() == row2[1] and security_question_answer.get() != row2[2]:
            d = 1
        elif username3.get() != row2[0] and clicked7.get() != row2[1] and security_question_answer.get() == row2[2]:
            e = 1
        elif username3.get() == row2[0] and clicked7.get() != row2[1] and security_question_answer.get() != row2[2]:
            f = 1
        elif username3.get() != row2[0] and clicked7.get() == row2[1] and security_question_answer.get() != row2[2]:
            g = 1


    if a == 1:
        update()
    if b == 1:
        invalid_message1()
    if c == 1:
        invalid_message2()
    if d == 1:
        invalid_message3()
    if e == 1:
        invalid_message1()
    if f == 1:
        invalid_message2()
    if g == 1:
        invalid_message1()

#this page is accessed when the "forgot password?" button is clicked on from the user login page
def forgot_pass():
    global forgot_pass
    global forgot_pass_window
    forgot_pass_window = tkinter.Tk()
    forgot_pass_window.geometry("400x400")
    forgot_pass_window.title("Forgot password")
    forgot_pass_window.config(bg="white")

    forg = tkinter.Label(forgot_pass_window, fg="white", bg="#4EB168", text=("Forgot Password"), font=("Arial", 15))
    forg.pack(pady=5)
    forg.place(x=90, y=20)

    def click(event):
        username3.config(state=NORMAL)
        username3.delete(0, END)

    def click1(event):
        security_question_answer.config(state=NORMAL)
        security_question_answer.delete(0, END)

    global username3
    username3 = tkinter.Entry(forgot_pass_window, borderwidth=2)
    username3.insert(0, "Enter your username")
    username3.config(state=DISABLED)
    username3.bind("<Button-1>", click)
    username3.pack()
    username3.place(x=90, y=80)

    #this shows the question options displayed in the create new account window
    def show():
        global drop_down
        global options
        drop_down.config(text=clicked7.get())

    options = [
        "--select--",
        "Where was your first job?",
        "What was your first pets name?",
        "What was your top uni choice?"
    ]

    global clicked7
    clicked7 = StringVar(forgot_pass_window)
    clicked7.set("--select--")

    global drop_down
    drop = OptionMenu(forgot_pass_window, clicked7, *options)
    drop.pack()
    drop.place(x=90, y=110)

    #this answer is checked with the one placed in the database to ensure that they are equal
    global security_question_answer
    security_question_answer = tkinter.Entry(forgot_pass_window, borderwidth=3)
    security_question_answer.insert(0, "Answer")
    security_question_answer.config(state=DISABLED)
    security_question_answer.bind("<Button-1>", click1)
    security_question_answer.pack()
    security_question_answer.place(x=90, y=150)

    change_pass = tkinter.Label(forgot_pass_window, text="To change your password", bg="white", fg= "black", font=('Open Sans', 8))
    change_pass.place(x=90, y= 180)

    #these entry boxes would allow the user to enter new passwords to replace the old ones
    def click2(event):
        newpass1.config(state=NORMAL)
        newpass1.delete(0, END)

    global newpass1
    newpass1 = tkinter.Entry(forgot_pass_window, borderwidth=3)
    newpass1 .insert(0, "Enter new password")
    newpass1 .config(state=DISABLED)
    newpass1 .bind("<Button-1>", click2)
    newpass1 .pack()
    newpass1 .place(x=90, y=210)

    def click3(event):
        re_newpass1.config(state=NORMAL)
        re_newpass1.delete(0, END)

    global re_newpass1
    re_newpass1 = tkinter.Entry(forgot_pass_window, borderwidth=3)
    re_newpass1 .insert(0, "Re-enter new password")
    re_newpass1 .config(state=DISABLED)
    re_newpass1 .bind("<Button-1>", click3)
    re_newpass1 .pack()
    re_newpass1 .place(x=90, y=240)

    #to save the new password, this save button calls the "new" function
    save = tkinter.Button(forgot_pass_window, fg="white", bg="#4EB168", text="Save", height=1, command=check)
    save.place(x=90, y=270)

    exit2 = tkinter.Button(forgot_pass_window, fg="white", bg="#4EB168", text="Exit", height=1, width=5, command=forgot_pass_window.destroy)
    exit2.pack()
    exit2.place(x=150, y=270)

    forgot_pass_window.mainloop()
