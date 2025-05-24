#admin page
import tkinter
from tkinter import *
import sqlite3
from tkinter import ttk

# this allows the admin to delete the table from the database
def delete_all_logins():
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    try:
        c.execute('''DROP TABLE details''')
    except:
        pass
    conn.commit()
    conn.close()


# this allows the admin to delete the table from the database
def delete_all_info():
    conn = sqlite3.connect("userpractices.db")
    d = conn.cursor()

    try:
        d.execute('''DROP TABLE user_practices''')
    except:
        pass
    conn.commit()
    conn.close()


# this page is accessed when the admin is logged in
def admin():
    global foot_track
    admin_page_window = tkinter.Tk()
    admin_page_window.geometry("800x700")
    admin_page_window.title("Footprint tracking")
    admin_page_window.config(bg="White")

    global left_bg
    left_bg = "white"
    global right_bg
    right_bg = "#4EB168"
    global font_
    font_ = "Arial"

    screen_divide = PanedWindow(admin_page_window, orient=HORIZONTAL)
    screen_divide.pack(fill=BOTH, expand=1)

    left = Label(screen_divide, bg=left_bg)  # , text="top pane")
    screen_divide.add(left)

    right = Label(screen_divide, bg=right_bg)  # , text="bottom pane")
    screen_divide.add(right)

#------#LEFT
#-----TOP
    show1 = tkinter.Label(left, fg="white", bg="#4EB168", text="User details", width=15)
    show1.pack(side="top", fill="x")

    delete2 = tkinter.Button(left, fg="white", bg="#4EB168", text="Delete user information",
                             width=20, command=delete_all_info)
    delete2.pack(side="top", fill="x")


#-----BOTTOM
    show2 = tkinter.Label(left, fg="white", bg="#4EB168", text="login details", width=15)
    show2.pack(side="bottom", fill="x")

    delete1 = tkinter.Button(left, fg="white", bg="#4EB168", text="Delete login details",
                             width=20, command=delete_all_logins)
    delete1.pack(side="bottom", fill="x")


#------RIGHT
    myFrame = Frame(right, bd=1, relief="sunken")
    myFrame.pack(fill=Y, padx=10)

    label = tkinter.Label(myFrame, text="USER INFORMATION")
    label.pack(side='top')

    tree = ttk.Treeview(myFrame, columns=(1, 2, 3, 4, 5, 6, 7), height=10, show="headings")
    tree.pack(side='bottom')

    tree.heading(1, text="First name")
    tree.heading(2, text="Last Name")
    tree.heading(3, text="Username")
    tree.heading(4, text="Password")
    tree.heading(5, text="Re-enter password")
    tree.heading(6, text="Security question")
    tree.heading(7, text="Security Answer")

    tree.column(1, width=100)
    tree.column(2, width=100)
    tree.column(3, width=100)
    tree.column(4, width=100)
    tree.column(5, width=100)
    tree.column(6, width=150)
    tree.column(7, width=100)

    label2 = tkinter.Label(myFrame, text="LOGIN DETAILS")
    label2.pack(side='bottom')

    tree2 = ttk.Treeview(myFrame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), height=10, show="headings")
    tree2.pack(side='top')

    tree2.heading(1, text="Username")
    tree2.heading(2, text="Day")
    tree2.heading(3, text="Month")
    tree2.heading(4, text="Year")
    tree2.heading(5, text="Watts_per_day")
    tree2.heading(6, text="recycle_per_week")
    tree2.heading(7, text="number_residents")
    tree2.heading(8, text="petrol_vehicles")
    tree2.heading(9, text="electric_vehicles")
    tree2.heading(10, text="major_transport")
    tree2.heading(11, text="distance")
    tree2.heading(12, text="frequency_travel")
    tree2.heading(13, text="Main_appliance")

    tree2.column(1, width=100)
    tree2.column(2, width=100)
    tree2.column(3, width=100)
    tree2.column(4, width=100)
    tree2.column(5, width=100)
    tree2.column(6, width=100)
    tree2.column(7, width=100)
    tree2.column(8, width=100)
    tree2.column(9, width=100)
    tree2.column(10, width=100)
    tree2.column(11, width=100)
    tree2.column(12, width=100)
    tree2.column(13, width=100)

    tree_scrollx = ttk.Scrollbar(tree2, orient=tkinter.HORIZONTAL, command=tree2.xview)
    tree_scrollx.place(relx=0.02, rely=0.79, relwidth=0.9, relheight=0.03)
    tree2.config(xscrollcommand=tree_scrollx.set)

    tree_scrollx2 = ttk.Scrollbar(tree, orient=tkinter.HORIZONTAL, command=tree.xview)
    tree_scrollx2.place(relx=0.02, rely=0.79, relwidth=0.9, relheight=0.03)
    tree.config(xscrollcommand=tree_scrollx2.set)

    #-----
    tree_scrolly = ttk.Scrollbar(tree2, orient=tkinter.VERTICAL, command=tree2.yview)
    tree_scrolly.place(rely=0.02, relx=0.79, relwidth=0.9, relheight=0.03)
    tree2.config(yscrollcommand=tree_scrolly.set)

    tree_scrolly2 = ttk.Scrollbar(tree, orient=tkinter.VERTICAL, command=tree.yview)
    tree_scrolly2.place(rely=0.02, relx=0.79, relwidth=0.9, relheight=0.03)
    tree.config(yscrollcommand=tree_scrolly2.set)

    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()

    #this displays all the user log in details on the admin page
    for row in c.execute('''  SELECT * FROM details'''):
        tree.insert('', 'end', value=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    conn2 = sqlite3.connect("userpractices.db")
    d = conn2.cursor()

    #this displays all the user daily inputs on the admin page
    for row2 in d.execute(''' SELECT * FROM user_practices'''):
        tree2.insert('', 'end',
                     value=(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7], row2[8], row2[9],
                            row2[10], row2[11], row2[12]))
    admin_page_window.mainloop()
