
# main
import tkinter
from tkinter import *
from PIL import Image, ImageTk  # allows me to display images
from logins import admin_login  # allows me to call the admin_login function from another file
from logins import user_login  # allows me to call the user_login function from another file
from footpage import foot_explain  # allows me to call the foot_explain function that describes footprint tracking
from progresspage import progress_explain  # allows me to call the progress_explain function that shows the user their progress
from disposal import disposal  # allows me to call the disposal function from the disposal page
from tips import tips  # allows me to call the tips function from the tips page
from goals import goals  # allows me to call the goals function from the goals page

# this is the main window of the application, the main/home page
main_window = tkinter.Tk()
main_window.geometry("600x650")
main_window.title("welcome")
main_window.config(bg="white")

# this is the logo of the website, it also acts as a link to the home page if the user needs to go back to the home page immediately
Logo = tkinter.Button(main_window, text="Sustainability Tracker", height=1, width=23, bg="white", fg="#4EB168",
                      font=('Open Sans', 15))
Logo.place(x=10, y=5)


# these buttons allow the user to login if they have an account and if they do not they can create an account
def on_hover(event):
    event.widget.configure(bg="#4EB168", fg="black")


def on_default(event):
    event.widget.configure(bg="#376836", fg="White")


def on_hover2(event):
    event.widget.configure(bg="#4EB168", fg="black")


def on_default2(event):
    event.widget.configure(bg="#376836", fg="White")


Admin_login_button = tkinter.Button(main_window, height=2, width=10, text="Admin log In", bg="#376836", fg="White",
                                    command=admin_login)
Admin_login_button.place(x=400, y=5)
Admin_login_button.bind('<Enter>', on_hover)
Admin_login_button.bind('<Leave>', on_default)

User_login_button = tkinter.Button(main_window, height=2, width=10, text="User log In", bg="#376836", fg="White",
                                   command=user_login)
User_login_button.place(x=500, y=5)
User_login_button.bind('<Enter>', on_hover2)
User_login_button.bind('<Leave>', on_default2)

# image resized to fit the space between the search bar and the logo
# the file was downloaded into the computer and opened from there
im = Image.open(r"C:\Users\User\Documents\A level sustainability tracker\sustainability.png")
tkimage = ImageTk.PhotoImage(im)
image = tkinter.Label(main_window, image=tkimage, height=230, width=450).place(x=80, y=50)

#search bar options
#once the search button is clicked, the input placed in the search bar is checked
#if the user searches goals they are taken to the goals page
#if the user searches methods they are taken to the disposal and methods page
#if the user searches tips they are taken to the tips page
#if there is an invalid entry, the error box below is displayed
def invalid_message1():
    global pop
    pop = Toplevel(main_window)
    pop.title("Error")
    pop.geometry("200x150")
    pop.config(bg="#4EB168")

    pop_label = Label(pop, text="invalid input "
                                    )
    pop_label.pack()
def search():
    if entry.get() == "goals" or entry.get() == "Goals":
        goals()
    elif entry.get() == "tips" or entry.get() == "Tips":
        tips()
    elif entry.get() == "methods" or entry.get() == "Methods":
        disposal()
    elif entry.get() == " " or entry.get() == "":
        print("empty entry")
        invalid_message1()
    else:
        print("invalid input")
        invalid_message1()

# search bar
# this allows the user to search for information, if there is no information on the search then it returns the user to the main page
# if the search is relevant to the information then the appropriate page will be called
def entry_focus_in(event):
    if entry.get() == "Search tips, goals and methods":
        entry.delete(0, 'end')
        entry.config(fg="Black")


def entry_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Search tips, goals and methods")
        entry.config(fg="white")

global entry
entry = tkinter.Entry(main_window, width=30, font=("Helvectica", 13), fg="black", bg="#E5F5E5")
entry.place(x=140, y=290)
entry.insert(0, "Search tips, goals and methods")
entry.bind("<FocusIn>", entry_focus_in)
entry.bind("<FocusOut>", entry_focus_out)


search_button = tkinter.Button(main_window, text="Search", font=("Helvectica", 9), bg="#376836", fg="white", command =search)
search_button.pack()
search_button.place(x=420, y=290)

# articles label
# tells the user that there are articles and resources on the right
Article_resource = tkinter.Label(main_window, text="Articles and resources", fg="Black", bg="White",
                                 font=("Helvectica", 13))
Article_resource.place(x=50, y=350)

# Articles
# these articles just give the user a brief page of information for readings and could be called based on the user search or clicking the links
Disp_recycling = tkinter.Button(main_window, width=25, text="Disposal and recycling methods", bg="white", fg="black",
                                font=("Helvectica", 11), command=disposal)
Disp_recycling.place(x=310, y=320)
sus_tips = tkinter.Button(main_window, width=25, text="Sustainability tips", bg="white", fg="black",
                          font=("Helvectica", 11), command=tips)
sus_tips.place(x=310, y=350)
sus_goals = tkinter.Button(main_window, width=25, text="Sustainability goals", bg="white", fg="black",
                           font=("Helvectica", 11), command=goals)
sus_goals.place(x=310, y=380)

# these are the main functions of the program
# the "learn more" buttons would take the user to a page that gives a little description of the functions
footprint_track = tkinter.Label(main_window, height=3, width=22, text="Footprint tracking                         ",
                                bg="#E5F5E5", fg="black", font=("Helvectica", 12), padx=30)
footprint_track.place(x=330, y=420)
learn_more = tkinter.Button(main_window, text="Learn more", width=10, font=("Helvectica", 9), bg="#376836", fg="white",
                            command=foot_explain)
learn_more.place(x=485, y=440)

progress_track = tkinter.Label(main_window, height=5, width=22,
                               text="                  Progress tracking and visualization                         ",
                               bg="#E5F5E5", fg="black", font=("Helvectica", 12), padx=35)
progress_track.place(x=330, y=470)
learn_more2 = tkinter.Button(main_window, text="Learn more", width=10, font=("Helvectica", 9), bg="#376836", fg="white",
                             command=progress_explain)
learn_more2.place(x=485, y=533)

# second image
# image resized to fit the space between the articles and resources and the mini logo at the bottom
# the file was downloaded into the computer and opened from there
im2 = Image.open(r"C:\Users\User\Documents\A level sustainability tracker\leaves.jpg")
tkimage2 = ImageTk.PhotoImage(im2)
image2 = tkinter.Label(main_window, image=tkimage2, height=210, width=265).place(x=35, y=380)

# mini logo placed at the bottom of the page
mini_logo = tkinter.Label(main_window, text="Sustainability Tracker", height=1, width=20, bg="white", fg="#4EB168",
                          font=('Open Sans', 11))
mini_logo.place(x=10, y=600)
main_window.mainloop()