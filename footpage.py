
# footpage
import tkinter
from tkinter import *
from logins import user_login  # allows me to call the user_login function from another file

#this is the page that would preceed the footprint tracking page
#it should give a brief description of general progress and have some other text
#then it would display a link to the user login page so they can access the footprint tracking page
def foot_explain():
    global foot_track
    foot_page_window = tkinter.Tk()
    foot_page_window.geometry("470x400")
    foot_page_window.title("Footprint tracking")
    foot_page_window.config(bg="White")


    foot1 = Label(foot_page_window, text="Tracking energy consumption, carbon emissions and waste generation is vital for several reasons. "
                                         "\n Firstly, it allows individuals and organizations to understand their environmental impact. "
                                         "\n By monitoring these metrics, "
                                         "\n one can identify areas where improvements can be made to reduce their carbon footprint "
                                         "\n and minimize waste generation. "
                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    foot1.pack(pady=20)
    foot1.place(x=20, y=10)

    foot2 = Label(foot_page_window,
                  text="Secondly, tracking these factors helps i setting goals for sustainability and efficiency. "
                       "\n By having data on energy consumption and emissions,"
                       "\n  individuals and business can establish targets for reducing their environmental impact over time,"
                       "\n  leading to more sustainable practices. "
                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    foot2.pack(pady=20)
    foot2.place(x=20, y=90)

    foot3 = Label(foot_page_window,
                  text="Furthermore, monitoring energy usage and waste generation can also lead to cost savings. "
                       "\n By identifying inefficiencies and areas where energy of resources are being wasted,"
                       "\n  idnividuals and organizations can implement changes to reduce utility bills "
                       "\n and waste disposal costs."
                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    foot3.pack(pady=20)
    foot3.place(x=20, y=150)

    foot4 = Label(foot_page_window,
                  text="Finally, tracking these metrics promotes accountability and transparency. "
                       "\n It allows stakeholders, including customers, investors, and regultory bodies, "
                       "\n to assess an entity's environmental performance and hold them accountable for their actions. "
                       "\n This can lead to increased trust and credibility for those who prioritze sustainability efforts. "
                       "\n Overall, tracking energy consumption, "
                       "\n carbon emissions, and waste generation is essential for fostering a more sustainable and"
                       "\n  environmentally conscious society. "
                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    foot4.pack(pady=20)
    foot4.place(x=20, y=210)


    here = tkinter.Label(foot_page_window, text="To start footprint tracking", font=("Helvetica", 8),bg="#376836", fg="white", height=1)
    here.pack()
    here.place(x=20, y=320)

    log_button = tkinter.Button(foot_page_window, text="Log in", command=user_login)
    log_button.pack()
    log_button.place(x=150, y=320)


    foot_page_window.mainloop()
