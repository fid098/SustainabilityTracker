
# progress
import tkinter
import sqlite3
from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#def plot():
#    import matplotlib.pyplot as plt
#    import numpy as np

#    conn = sqlite3.connect("userpractices.db")
#    c = conn.cursor()

#    plt.style.use('fivethirtyeight')

#    # make data
#    np.random.seed(1)
#    x = 4 + np.random.normal(0, 1.5, 200)

#    # plot:
#    fig, ax = plt.subplots()

#    ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

#    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#           ylim=(0, 56), yticks=np.linspace(0, 56, 9))

#    plt.show()


# this is where the inputs of the user are calculated to give a result
def result():
    global rate
    rate = 0
    conn = sqlite3.connect("userpractices.db")
    c = conn.cursor()

    for row in c.execute('''   SELECT Watts_per_day,recycle_per_week,number_residents,petrol_vehicles,electric_vehicles,major_transport, distance,
         frequency_travel, Main_appliance FROM user_practices WHERE Day= "%s" and Month = "%s" and Year = "%s" and 
         Username = "%s" '''% (day.get(), month.get(), year.get(), username4.get())):
        #the watts differ for every different appliance selected by the user
        appliance_watts = 0
        if row[8] == "Air conditioner":
            appliance_watts = 600
            rate = 1.2
        elif row[8] == "Clothes dryer":
            appliance_watts = 3000
            rate = 6
        elif row[8] == "Dishwasher":
            appliance_watts = 1600
            rate = 3.2
        elif row[8] == "Electric kettle":
            appliance_watts = 2000
            rate = 4
        elif row[8] == "Fan":
            appliance_watts = 70
            rate = 0.14
        elif row[8] == "Heater":
            appliance_watts = 2000
            rate = 4
        elif row[8] == "Microwave oven":
            appliance_watts = 800
            rate = 1.6
        elif row[8] == "Desktop computer":
            appliance_watts = 100
            rate = 0.2
        elif row[8] == "Laptop computer":
            appliance_watts = 50
            rate = 0.1
        elif row[8] == "Refrigerator":
            appliance_watts = 200
            rate = 0.4
        elif row[8] == "Television":
            appliance_watts = 70
            rate = 0.14
        elif row[8] == "Toaster":
            appliance_watts = 1000
            rate = 2
        elif row[8] == "Vacuum Cleaner":
            appliance_watts = 1600
            rate = 3.2
        elif row[8] == "Washing machine":
            appliance_watts = 2000
            rate = 4
        elif row[8] == "Clothes iron":
            appliance_watts = 2400
            rate = 4.8
    for row2 in c.execute('''   SELECT Watts_per_day,recycle_per_week,number_residents,petrol_vehicles,electric_vehicles,major_transport, distance,
         frequency_travel, Main_appliance FROM user_practices WHERE Day= "%s" and Month = "%s" and Year = "%s" and 
         Username = "%s" '''% (day.get(), month.get(), year.get(), username4.get())):
        #the amount of carbon emitted differs for every means of transportation
        carbon_emitted = 0
        if row2[5] == "Walking":
            carbon_emitted = 3.479
        elif row2[5] == "Car":
            carbon_emitted = 221.4
        elif row2[5] == "Train":
            carbon_emitted = 80
        elif row2[5] == "Cycling":
            carbon_emitted = 30

        #this is where the calculations are done and then outputted in the text document
        global average_kw_day
        average_kw_day = 4.93
        global energy_per_day
        energy_per_day = ((appliance_watts/1000) * row[0]) + average_kw_day
        global bag_per_day
        bags_per_day = row[1]
        global residents
        residents = row[2]
        global petrol_vehicles
        petrol_vehicles = row[3]
        global electric_vehicles
        electric_vehicles = row[4]
        global major_transport
        major_transport = row[5]
        global average_distance
        average_distance = row[6]
        global frequency_travel
        frequency_travel = row[7]
        global total_carbon
        total_carbon = ((carbon_emitted * frequency_travel) * (average_distance * petrol_vehicles))

        my_text.insert(END, "hello " + str(username4.get()))
        my_text.insert(END, "\n")
        my_text.insert(END, str(residents) + " people lived at your house")
        my_text.insert(END, "\n")
        my_text.insert(END, "You used up " + str(energy_per_day) + " kiloWatt hour(kWh) for the day")
        my_text.insert(END, "\n")
        my_text.insert(END, "You used " + str(bags_per_day) + " recycle bags for the day")
        my_text.insert(END, "\n")
        my_text.insert(END, "You had " + str(petrol_vehicles) + " petrol vehicles in your household")
        my_text.insert(END, "\n")
        my_text.insert(END, "You had " + str(electric_vehicles) + " electric vehicles in your household")
        my_text.insert(END, "\n")
        my_text.insert(END, "Your major means of transport was " + major_transport)
        my_text.insert(END, "\n")
        my_text.insert(END, "Your average distance of transport was " + str(average_distance) + " miles")
        my_text.insert(END, "\n")
        my_text.insert(END, "You travelled " + str(frequency_travel) + " times per day")
        my_text.insert(END, "\n")
        my_text.insert(END, "You emitted a total of " + str(total_carbon) + " grams of carbon dioxide per mile(gCO2eq/m) on the day ")
        my_text.insert(END, "\n")


#this function checks if there is a missing entry in the username entry box
#if there is not, the dates are displayed
def check():
    if username4.get() == "" or username4.get() == " ":
        print("please enter a username")
        missing_entry()
    else:
        username_check()


#these are error box messages
#they are displayed when there is an error somewhere
def invalid_message1():
    global pop
    pop = Toplevel(progress_page_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid input "
                                    )
    pop_label.pack()

def missing_entry():
    global pop2
    pop2 = Toplevel(progress_page_window)
    pop2.title("Error")
    pop2.geometry("200x150")
    pop2.config(bg="#4EB168")

    pop2_label = Label(pop2, text=" Entry missing "
                                    )
    pop2_label.pack()

def max_char():
    global pop3
    pop3 = Toplevel(progress_page_window)
    pop3.title("Error")
    pop3.geometry("200x150")
    pop3.config(bg="#4EB168")

    pop3_label = Label(pop3, text="The max character length is 10 "
                                    )
    pop3_label.pack()

def select():
    global pop4
    pop4 = Toplevel(progress_page_window)
    pop4.title("Error")
    pop4.geometry("200x150")
    pop4.config(bg="#4EB168")

    pop4_label = Label(pop, text="Please select an option"
                                    )
    pop4_label.pack()

def password_match():
    global pop5
    pop5 = Toplevel(progress_page_window)
    pop5.title("Error")
    pop5.geometry("200x150")
    pop5.config(bg="#4EB168")

    pop5_label = Label(pop5, text="The passwords do not match"
                                    )
    pop5_label.pack()

def String_error():
    global pop6
    pop6 = Toplevel(progress_page_window)
    pop6.title("Error")
    pop6.geometry("200x150")
    pop6.config(bg="#4EB168")

    pop6_label = Label(pop6, text="Invalid input type: String"
                                    )
    pop6_label.pack()


def exist():
    global exist
    global pop7
    pop7 = Toplevel(progress_page_window)
    pop7.title("Error")
    pop7.geometry("200x150")
    pop7.config(bg="#4EB168")

    pop7_label = Label(pop7, text="This username does not exist"
                           )
    pop7_label.pack()

def Digit_error():
    global pop8
    pop8 = Toplevel(progress_page_window)
    pop8.title("Error")
    pop8.geometry("200x150")
    pop8.config(bg="#4EB168")

    pop8_label = Label(pop8, text="Invalid input type: Integer"
                           )
    pop8_label.pack()

#this checks if the username entered is in the database
def username_check():
    h=0
    conn = sqlite3.connect("user_login_details.db")
    c = conn.cursor()
    for row in c.execute('''   SELECT username FROM details '''):
        print(row[0])
        if username4.get() == row[0]:
            print("there are usernames")
            h = 1

    if h==1:
        dates()
    else:
        exist()

#this is the validation function
#this checks the inputs them and regulates them based on certain criteria
#if they do not meet the criteria there is an error message
#if they meet the criteria, the progress is displyaed
def check2():
    if username4.get() == "" or username4.get() == " ":
        print("username entry missing")
        missing_entry()
    elif username4.get().isalpha() == True:
        username_check()
    elif username4.get().isdigit() == True:
        Digit_error()
    elif day.get() == "" or day.get() == " ":
        print("day entry missing")
        missing_entry()
    elif month.get() == "" or month.get() == " ":
        print("month entry missing")
        missing_entry()
    elif year.get() == "" or year.get() == " ":
        print("year entry missing")
        missing_entry()
    elif len(day.get()) > 2:
        print("invalid day")
        invalid_message1()
    elif int(day.get()) > 31:
        print("invalid day")
        invalid_message1()
    elif len(month.get()) > 2:
        print("invalid month")
        invalid_message1()
    elif int(month.get()) > 12:
        print("invalid month")
        invalid_message1()
    elif len(year.get()) > 4:
        print("invalid year")
        invalid_message1()
    elif day.get().isalpha()  == True:
        String_error()
    elif month.get().isalpha()  == True:
        String_error()
    elif year.get().isalpha()  == True:
        String_error()
    else:
        result()

#this function displays the dates of every input of a certain user
def dates():
    global dates
    conn = sqlite3.connect("userpractices.db")
    c = conn.cursor()

    for row3 in c.execute(''' SELECT Day, Month, Year FROM user_practices WHERE Username="%s" ''' %(username4.get())):
        my_text.insert(END, "Input on: ")
        dates = row3
        my_text.insert(END,str(dates))
        my_text.insert(END, "\n")


def progress2():
    global progress_page_window
    progress_page_window = tkinter.Tk()
    progress_page_window.geometry("420x600")
    progress_page_window.title("Disposal Page")
    progress_page_window.config(bg="White")



    main = tkinter.Label(progress_page_window, bg="white", fg="#4EB168", text="Progress tracking", font=("Arial", 15))
    main.pack(pady=5)
    main.place(x=90, y=20)

#these entry boxes take in dates of when the user input data previously
    def click(event):
        day.config(state=NORMAL)
        day.delete(0, END)

    def click1(event):
        month.config(state=NORMAL)
        month.delete(0, END)

    def click2(event):
        year.config(state=NORMAL)
        year.delete(0, END)

    def click3(event):
        username4.config(state=NORMAL)
        username4.delete(0, END)

    global day
    day = tkinter.Entry(progress_page_window, borderwidth=3)
    day.insert(0, "Enter day")
    day.config(state=DISABLED)
    day.bind("<Button-1>", click)
    day.pack()
    day.place(x=90, y=80)

    global month
    month = tkinter.Entry(progress_page_window, borderwidth=3)
    month.insert(0, "Enter month")
    month.config(state=DISABLED)
    month.bind("<Button-1>", click1)
    month.pack()
    month.place(x=90, y=110)

    global year
    year = tkinter.Entry(progress_page_window, borderwidth=3)
    year.insert(0, "Enter year")
    year.config(state=DISABLED)
    year.bind("<Button-1>", click2)
    year.pack()
    year.place(x=90, y=140)

    global username4
    username4 = tkinter.Entry(progress_page_window, borderwidth=3)
    username4.insert(0, "Enter username")
    username4.config(state=DISABLED)
    username4.bind("<Button-1>", click3)
    username4.pack()
    username4.place(x=230, y=110)

    button = tkinter.Button(progress_page_window, text="go", command=check2)
    button.pack()
    button.place(x=90, y= 170)

    see_dates = tkinter.Button(progress_page_window, text="see dates of inputs", command=lambda:check())
    see_dates.pack()
    see_dates.place(x=230, y=140)

    #this allows the user to clear the screen
    def clear():
        my_text.delete(1.0, END)

    #this displays a large text screen to allow the users data for the day to be outputted
    global my_text
    my_text = tkinter.Text(progress_page_window, width=50, height=20)
    my_text.pack(pady=20)
    my_text.place(x=10, y=200)

    clear = tkinter.Button(progress_page_window, text="clear screen", command=clear)
    clear.pack()
    clear.place(x=120, y=170)

    progress_page_window.mainloop()


