
# foot tracker
import tkinter
from tkinter import *
import sqlite3


#this creates a new database called user_details to hold the daily inputs of the user
def create_file():
    conn = sqlite3.connect("userpractices.db")
    c = conn.cursor()

#these are the columns in the database and data is added into these columns after every input
    c.execute('''  CREATE TABLE IF NOT EXISTS user_practices
    (Username VARCHAR(255),
    Day INT, 
    Month INT,
    Year INT,
    Watts_per_day INT,
    recycle_per_week INT,
    number_residents INT,
    petrol_vehicles INT,
    electric_vehicles INT,
    major_transport VARCHAR(255),
    distance INT,
    frequency_travel INT,
    Main_appliance VARCHAR(225)
    )
    ''')
    conn.close()


create_file()

#this page is opened when the user proceeds from the description of footprint tracking
#this page allows the user to enter their information weekly
#the information is stored in a database

def foot_track():
    global foot_track
    foot_track_window = tkinter.Tk()
    foot_track_window.geometry("420x600")
    foot_track_window.title("Footprint tracking")
    foot_track_window.config(bg="White")

    little_logo = tkinter.Label(foot_track_window, text="Sustainability Tracker", height=1, width=20, bg="white", fg="#4EB168",
                              font=('Open Sans', 12))
    little_logo.place(x=10, y=550)

    header = tkinter.Label(foot_track_window, fg="white", bg="#4EB168", text=("Footprint Tracking"), font=("Arial", 17))
    header.pack(pady=5)
    header.place(x=120, y=20)

    energy = tkinter.Label(foot_track_window, fg="Black", bg="White", text="Energy Consumption", font=("Open Sans", 12))
    energy.place(x=40, y=70)

    def appliance_power():
        #for every appliance, a different number of watts is displayed on the screen when the user clicks on "go"
        if clicked2.get() == "Air conditioner":

            message1 = Label(foot_track_window, bg="white", fg="black", height=1, text="600",
                             font=("Open Sans", 10))
            message1.place(x=90, y=125)
        elif clicked2.get() == "Clothes dryer":
            message2 = Label(foot_track_window, bg="white", fg="black", height=1, text="3000",
                             font=("Open Sans", 10))
            message2.place(x=90, y=125)
        elif clicked2.get() == "Dishwasher":
            message3 = Label(foot_track_window, bg="white", fg="black", height=1, text="1600",
                             font=("Open Sans", 10))
            message3.place(x=90, y=125)
        elif clicked2.get() == "Electric kettle":
            message4 = Label(foot_track_window, bg="white", fg="black", height=1, text="2000",
                             font=("Open Sans", 10))
            message4.place(x=90, y=125)
        elif clicked2.get() == "Fan":
            message4 = Label(foot_track_window, bg="white", fg="black", height=1, text="70",
                             font=("Open Sans", 10))
            message4.place(x=90, y=125)
        elif clicked2.get() == "Heater":
            message5 = Label(foot_track_window, bg="white", fg="black", height=1, text="2000",
                             font=("Open Sans", 10))
            message5.place(x=90, y=125)
        elif clicked2.get() == "Microwave oven":
            message6 = Label(foot_track_window, bg="white", fg="black", height=1, text="800",
                             font=("Open Sans", 10))
            message6.place(x=90, y=125)
        elif clicked2.get() == "Desktop computer":
            message7 = Label(foot_track_window, bg="white", fg="black", height=1, text="100",
                             font=("Open Sans", 10))
            message7.place(x=90, y=125)
        elif clicked2.get() == "Laptop computer":
            message8 = Label(foot_track_window, bg="white", fg="black", height=1, text="50",
                             font=("Open Sans", 10))
            message8.place(x=90, y=125)
        elif clicked2.get() == "Refrigerator":
            message9 = Label(foot_track_window, bg="white", fg="black", height=1, text="200",
                             font=("Open Sans", 10))
            message9.place(x=90, y=125)
        elif clicked2.get() == "Television":
            message10 = Label(foot_track_window, bg="white", fg="black", height=1, text="70",
                             font=("Open Sans", 10))
            message10.place(x=90, y=125)
        elif clicked2.get() == "Toaster":
            message11 = Label(foot_track_window, bg="white", fg="black", height=1, text="1000",
                             font=("Open Sans", 10))
            message11.place(x=90, y=125)
        elif clicked2.get() == "Vacuum Cleaner":
            message12 = Label(foot_track_window, bg="white", fg="black", height=1, text="1600",
                             font=("Open Sans", 10))
            message12.place(x=90, y=125)
        elif clicked2.get() == "Washing machine":
            message8 = Label(foot_track_window, bg="white", fg="black", height=1, text="2000",
                             font=("Open Sans", 10))
            message8.place(x=90, y=125)
        elif clicked2.get() == "Clothes iron":
            message9 = Label(foot_track_window, bg="white", fg="black", height=1, text="2400",
                             font=("Open Sans", 10))
            message9.place(x=90, y=125)

    watts = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Watts",  font=("Open Sans", 10))
    watts.place(x=160, y=125)

    def box2(event):
        hours.config(state=NORMAL)
        hours.delete(0, END)
#this allows the user to enter how many hours they used that appliance for on that day
    hours = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=25 )
    hours.insert(0, "Hours of use")
    hours.config(state=DISABLED)
    hours.bind("<Button-1>", box2)
    hours.pack()
    hours.place(x=40, y=160)

    day = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per day",  font=("Open Sans", 10))
    day.place(x=190, y=160)

    #this displays a drop down box that includes a number of heavily used appliances that the user would select from
    def show2():
        global drop_down2
        global drop2
        global options2
        drop_down2.config(text = clicked2.get())

    options2 = [
    "--select--",
     "Air conditioner",
      "Clothes dryer",
        "Clothes iron",
        "Dishwasher",
        "Electric kettle",
        "Fan",
        "Heater",
        "Microwave oven",
        "Desktop computer",
        "Laptop computer",
        "Refrigerator",
        "Television",
        "Toaster",
        "Vacuum Cleaner",
        "Washing machine",
       ]

    clicked2 = StringVar(foot_track_window)
    clicked2.set("--select--")

    drop2 = OptionMenu(foot_track_window, clicked2,  *options2)
    drop2.pack()
    drop2.place(x=235, y=100)

    Typical_appliance = tkinter.Label(foot_track_window,fg="Black", bg="White", text="what typical appliance would you use?", font=("Open Sans", 10))
    Typical_appliance.pack()
    Typical_appliance.place(x=8, y =100)

    go = tkinter.Button(foot_track_window,fg="white", bg="#4EB168", text="go", height=1, command=appliance_power)
    go.place(x=380, y=105)



######################################################################################################



    waste = tkinter.Label(foot_track_window, fg="Black", bg="White", text="Waste Generation", font=("Open Sans", 12))
    waste.place(x=40, y=200)

#this allows the user to enter how many recycle bags he/she used on that particular day
    def box3(event):
        recycle.config(state=NORMAL)
        recycle.delete(0, END)

    recycle = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=25 )
    recycle.insert(0, "Recycle bags used")
    recycle.config(state=DISABLED)
    recycle.bind("<Button-1>", box3)
    recycle.pack()
    recycle.place(x=40, y=230)

    week = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per day",  font=("Open Sans", 10))
    week.place(x=160, y=230)

    def box4(event):
        residents.config(state=NORMAL)
        residents.delete(0, END)

#this allows the user to enter how many residents of the household there are
    residents = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=24 )
    residents.insert(0, "Number of residents")
    residents.config(state=DISABLED)
    residents.bind("<Button-1>", box4)
    residents.pack()
    residents.place(x=40, y=260)

    household = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per Household",  font=("Open Sans", 10))
    household.place(x=160, y=260)




###########################################################################################################################################
    carbon = tkinter.Label(foot_track_window, fg="Black", bg="White", text="Carbon Emission", font=("Open Sans", 12))
    carbon.place(x=40, y=330)

    def box5(event):
        petrol.config(state=NORMAL)
        petrol.delete(0, END)

#this allows the user to enter the number of petrol vehicles that they own
    petrol = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=25)
    petrol.insert(0, "Number of petrol vehicles")
    petrol.config(state=DISABLED)
    petrol.bind("<Button-1>", box5)
    petrol.place(x=40, y=360)

    household2 = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per Household",  font=("Open Sans", 10))
    household2.place(x=210, y=360)

    def box6(event):
        electric.config(state=NORMAL)
        electric.delete(0, END)
#this allows the user to enter the number of electric vehicles that they own
    electric = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=23)
    electric.insert(0, "Number of electric vehicles")
    electric.config(state=DISABLED)
    electric.bind("<Button-1>", box6)
    electric.place(x=40, y=390)

    household3 = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per Household",  font=("Open Sans", 10))
    household3.place(x=210, y=390)

#this displays a drop down box that gives the user options of what their major means of transportation was
    def show4():
        global drop4
        global drop_down4
        global options4
        drop_down4.config(text=clicked4.get())

    options4 = [
        "--select--",
        "Walking",
        "Car",
        "Train",
        "Cycling"
    ]

    clicked4 = StringVar(foot_track_window)
    clicked4.set("--select--")

    drop4 = OptionMenu(foot_track_window, clicked4, *options4)
    drop4.pack()
    drop4.place(x=195, y=417)

    major_transport = tkinter.Label(foot_track_window, fg="Black", bg="White",
                                      text="Major Means of transport?", font=("Open Sans", 10))
    major_transport.pack()
    major_transport.place(x=40, y=420)

    def box7(event):
        distance.config(state=NORMAL)
        distance.delete(0, END)

#this allows the user to enter the average distance of their travel with the major means of transport
    global distance
    distance = tkinter.Entry(foot_track_window, borderwidth=1, font=("Open Sans", 10), width=23)
    distance.insert(0, "Average distance")
    distance.config(state=DISABLED)
    distance.bind("<Button-1>", box7)
    distance.place(x=40, y=450)

    miles = tkinter.Label(foot_track_window, fg="Black", bg="White", text=" In miles", font=("Open Sans", 10))
    miles.place(x=210, y=450)

    def box8(event):
        frequency.config(state=NORMAL)
        frequency.delete(0, END)
#this allows the user to enter the frequency of travel using their major means of transport
    frequency = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=23)
    frequency.insert(0, "Frequency of travel")
    frequency.config(state=DISABLED)
    frequency.bind("<Button-1>", box8)
    frequency.place(x=40, y=480)

    day2 = tkinter.Label(foot_track_window, fg="Black", bg="White",text=" Per day",  font=("Open Sans", 10))
    day2.place(x=210, y=480)

    def box9(event):
        day.config(state=NORMAL)
        day.delete(0, END)


#these entry boxes allow the user to enter the date of their input
    day = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=4)
    day.insert(0, "DD")
    day.config(state=DISABLED)
    day.bind("<Button-1>", box9)
    day.place(x=200, y=510)

    def box10(event):
        month.config(state=NORMAL)
        month.delete(0, END)

    month = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=4)
    month.insert(0, "MM")
    month.config(state=DISABLED)
    month.bind("<Button-1>", box10)
    month.place(x=240, y=510)

    def box11(event):
        year.config(state=NORMAL)
        year.delete(0, END)

    year = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=5)
    year.insert(0, "YYYY")
    year.config(state=DISABLED)
    year.bind("<Button-1>", box11)
    year.place(x=280, y=510)

    def box11(event):
        username3.config(state=NORMAL)
        username3.delete(0, END)

    username3 = tkinter.Entry(foot_track_window, borderwidth=1,font=("Open Sans", 10), width=17)
    username3.insert(0, "Enter username: ")
    username3.config(state=DISABLED)
    username3.bind("<Button-1>", box11)
    username3.place(x=200, y=540)

#this allows the user to enter their data into the database
    global add_entry
    def add_entry(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        conn = sqlite3.connect("userpractices.db")
        c = conn.cursor()

        c.execute('''    INSERT OR IGNORE INTO user_practices
        (Username, Day, Month, Year,Watts_per_day,recycle_per_week,number_residents,petrol_vehicles,electric_vehicles,major_transport, distance,
         frequency_travel, Main_appliance)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13))
        conn.commit()
        conn.close()

    # these are error box messages
    #these are displayed when there is an error somewhere
    def invalid_message1():
        global pop
        pop = Toplevel(foot_track_window)
        pop.title("Error")
        pop.geometry("200x150")
        pop.config(bg="#4EB168")

        pop_label = Label(pop, text="invalid date"
                          )
        pop_label.pack()

    def missing_entry():
        global pop2
        pop2 = Toplevel(foot_track_window)
        pop2.title("Error")
        pop2.geometry("200x150")
        pop2.config(bg="#4EB168")

        pop2_label = Label(pop2, text=" Entry missing "
                           )
        pop2_label.pack()

    def max_char():
        global pop3
        pop3 = Toplevel(foot_track_window)
        pop3.title("Error")
        pop3.geometry("200x150")
        pop3.config(bg="#4EB168")

        pop3_label = Label(pop3, text="The max number is 10 "
                           )
        pop3_label.pack()

    def select():
        global pop4
        pop4 = Toplevel(foot_track_window)
        pop4.title("Error")
        pop4.geometry("200x150")
        pop4.config(bg="#4EB168")

        pop4_label = Label(pop4, text="Please select an option"
                           )
        pop4_label.pack()

    def password_match():
        global pop5
        pop5 = Toplevel(foot_track_window)
        pop5.title("Error")
        pop5.geometry("200x150")
        pop5.config(bg="#4EB168")

        pop5_label = Label(pop5, text="The passwords do not match"
                           )
        pop5_label.pack()

    def String_error():
        global pop6
        pop6 = Toplevel(foot_track_window)
        pop6.title("Error")
        pop6.geometry("200x150")
        pop6.config(bg="#4EB168")

        pop6_label = Label(pop6, text="Invalid input type: String"
                           )
        pop6_label.pack()

    def Digit_error():
        global pop7
        pop7 = Toplevel(foot_track_window)
        pop7.title("Error")
        pop7.geometry("200x150")
        pop7.config(bg="#4EB168")

        pop7_label = Label(pop7, text="Invalid input type: Integer"
                           )
        pop7_label.pack()

    def bags():
        global pop8
        pop8 = Toplevel(foot_track_window)
        pop8.title("Error")
        pop8.geometry("200x150")
        pop8.config(bg="#4EB168")

        pop8_label = Label(pop8, text="too many recycle bags per day"
                           )
        pop8_label.pack()

    def residents_error():
        global pop9
        pop9 = Toplevel(foot_track_window)
        pop9.title("Error")
        pop9.geometry("200x150")
        pop9.config(bg="#4EB168")

        pop9_label = Label(pop9, text="Too many residents"
                           )
        pop9_label.pack()

    def petrol_error():
        global pop10
        pop10 = Toplevel(foot_track_window)
        pop10.title("Error")
        pop10.geometry("200x150")
        pop10.config(bg="#4EB168")

        pop10_label = Label(pop10, text="too many Petrol vehicles"
                           )
        pop10_label.pack()

    def electric_error():
        global pop11
        pop11 = Toplevel(foot_track_window)
        pop11.title("Error")
        pop11.geometry("200x150")
        pop11.config(bg="#4EB168")

        pop11_label = Label(pop11, text="too many Electric vehicles"
                           )
        pop11_label.pack()

    def hours_error():
        global pop12
        pop12 = Toplevel(foot_track_window)
        pop12.title("Error")
        pop12.geometry("200x150")
        pop12.config(bg="#4EB168")

        pop12_label = Label(pop12, text="Cannot input over 24 hours"
                           )
        pop12_label.pack()

    def exist():
        global exist
        global pop13
        pop13 = Toplevel(foot_track_window)
        pop13.title("Error")
        pop13.geometry("200x150")
        pop13.config(bg="#4EB168")

        pop13_label = Label(pop13, text="This username does not exist"
                           )
        pop13_label.pack()

    def special_error():
        global pop14
        pop14 = Toplevel(foot_track_window)
        pop14.title("Error")
        pop14.geometry("200x150")
        pop14.config(bg="#4EB168")

        pop14_label = Label(pop14, text="Invalid input type: Special character"
                           )
        pop14_label.pack()

    def date_error():
        global pop15
        pop15 = Toplevel(foot_track_window)
        pop15.title("Error")
        pop15.geometry("200x150")
        pop15.config(bg="#4EB168")

        pop15_label = Label(pop15, text="Date enterred is occupied"
                           )
        pop15_label.pack()

    
    # this is the validation function
    # this checks the inputs them and regulates them based on certain criteria
    # if they do not meet the criteria there is an error message
    # if they meet the criteria the user inputs are entered into the database
    def validation():
        if hours.get().isalpha() == True:
            String_error()
        elif int(hours.get()) > 24:
            hours_error()
        elif username3.get().isdigit() == True:
            Digit_error()
        elif day.get().isalpha() == True:
            String_error()
        elif month.get().isalpha() == True:
            String_error()
        elif year.get().isalpha() == True:
            String_error()
        elif recycle.get().isalpha() == True:
            String_error()
        elif residents.get().isalpha() == True:
            String_error()
        elif petrol.get().isalpha() == True:
            String_error()
        elif electric.get().isalpha() == True:
            String_error()
        elif distance.get().isalpha() == True:
            String_error()
        elif frequency.get().isalpha() == True:
            String_error()
        elif day.get().isalpha() == True:
            String_error()
        elif month.get().isalpha() == True:
            String_error()
        elif year.get().isalpha() == True:
            String_error()
        elif int(recycle.get()) > 10:
            bags()
        elif int(residents.get()) > 10:
            residents_error()
        elif int(petrol.get()) > 10:
            petrol_error()
        elif int(electric.get()) > 10:
            electric_error()
        elif len(day.get()) > 2:
            invalid_message1()
        elif int(day.get()) > 31:
            invalid_message1()
        elif len(month.get()) > 2:
            invalid_message1()
        elif int(month.get()) > 12:
            invalid_message1()
        elif len(year.get()) > 4:
            invalid_message1()
        elif clicked4.get() == "--select--":
            select()
        elif clicked2.get() == "--select--":
            select()
        #elif str(hours.get()).isalnum() == False:
         #   special_error()
        #elif residents.get().isalnum() == False:
         #   special_error()
        #elif recycle.get().isalnum() == False:
         #   special_error()
        #elif petrol.get().isalnum() == False:
         #   special_error()
        #elif electric.get().isalnum() == False:
         #   special_error()
        #elif distance.get().isalnum() == False:
         #   special_error()
        #elif frequency.get().isalnum() == False:
         #   special_error()
        #elif day.get().isalnum() == False:
         #   special_error()
        #elif month.get().isalnum() == False:
         #   special_error()
        #elif year.get().isalnum() == False:
         #   special_error()
        else:
            username_check()

    #this checks if the username entered is in the database
    def username_check():
        h = 0
        conn = sqlite3.connect("user_login_details.db")
        c = conn.cursor()
        for row in c.execute('''   SELECT username FROM details '''):
            if username3.get() == row[0]:
                h = 1

        if h == 1:
            #add()
            date_check()
        else:
            exist()

    #this checks if there is a date occupied so the user can not enter the same date twice
    def date_check():
        global date_check
        z = 0
        j = 0
        k = 0
        l = 0
        conn = sqlite3.connect("userpractices.db")
        c = conn.cursor()
        for row in c.execute(''' SELECT Day, Month, Year FROM user_practices WHERE Username="%s" ''' % (username3.get())):

            if int(day.get()) == row[0] and int(month.get()) == row[1] and int(year.get()) == row[2]:
                z = 1
            if int(day.get()) != row[0] and int(month.get()) == row[1] and int(year.get()) == row[2]:
                j = 1
            if int(day.get()) == row[0] and int(month.get()) != row[1] and int(year.get()) == row[2]:
                k = 1
            if int(day.get()) == row[0] and int(month.get()) == row[1] and int(year.get()) != row[2]:
                l = 1


            #if day.get() == row[0]:
             #   if month.get() == row[1]:
              #      if year.get() == row[2]:
               #         z = 1

        if z == 1:
            date_error()
        if j == 1:
            add()
        if k == 1:
            add()
        if l == 1:
            add()

    def add():
        add_entry(username3.get(), day.get(), month.get(), year.get(), hours.get(), recycle.get(),
                          residents.get(), petrol.get(),
                          electric.get(), clicked4.get(), distance.get(), frequency.get(),
                          clicked2.get())



    #once the submit button is clicked, the input is enterred into the database using lambda
    submit = tkinter.Button(foot_track_window, fg="white", bg="#4EB168", text="Submit", height=1, width=5,
                            command=validation)
    submit.pack()
    submit.place(x=60, y=510)

    foot_track_window.mainloop()
