
# progress page
import tkinter
from tkinter import *
from logins import user_login # allows me to call the user_login function from another file

#this is the page that would preceed the progress tracking page
#it should give a brief description of general progress and have some other text
#then it would display a link to the user login page so they can access the progress tracking page
def progress_explain():
    global progress_explain
    progress_explain_window = tkinter.Tk()
    progress_explain_window.geometry("500x230")
    progress_explain_window.title("Progress Page")
    progress_explain_window.config(bg="White")

    progress1 = Label(progress_explain_window,
                  text="Progress tracking and visualization play crucial roles i advancing environmental sustainability efforts. "
                       "\n By monitoring key metrics such as energy consumption, carbon emissions and waste generation, "
                       "\nindividuals, the government and businesses can gauge their environmental impact and track progress over time "
                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    progress1.pack(pady=20)
    progress1.place(x=20, y=10)

    progress2 = Label(progress_explain_window,
                      text="Vizualizing this data though charts, graphs and interactive dashboards enhances understanding "
                           "\n and communication of complex environmental trends and patterns. "
                           "\n Visual representations can highlight areas of success and areas needing improvement, "
                           "\n making it easier for stakeholders to identify priorities and take targeted actions. "
                      ,
                      font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    progress2.pack(pady=20)
    progress2.place(x=20, y=60)

    here = tkinter.Label(progress_explain_window, text="To start Progress tracking", font=("Helvetica", 8), bg="#376836",
                         fg="white", height=1)
    here.pack()
    here.place(x=20, y=120)

    log_button = tkinter.Button(progress_explain_window, text="Log in", command=user_login)
    log_button.pack()
    log_button.place(x=170, y=120)


    progress_explain_window.mainloop()