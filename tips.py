
#tips
import tkinter
from tkinter import *

#this is a text filled page
#this displayed information relating to sustainabaility tips
def tips():
    tips_page_window = tkinter.Tk()
    tips_page_window.geometry("550x550")
    tips_page_window.title("Tips Page")
    tips_page_window.config(bg="White")

    dryer = Label(tips_page_window, text=" Retire your dryer"
                                             "\n Consider using a drying rack whenever possible instead of"
                                         "\n throwing your clothes in the dryer."
                                         "\n  You'll save money, save energy and prolong the life of your clothes."
                                             ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    dryer.pack(pady=20)
    dryer.place(x=20)

    bulbs = Label(tips_page_window, text=" Switch to better bulbs"
                                         "\n Ninety percent of the electricity used by incandescent light bulbs is given off as heat, "
                                         "\n which is wasted energy and money."
                                         "\n  Here's a bright(er) idea: Switch to LEDs, CFLs or halogen bulbs instead."
                                         "\n  They use as little as 20 percent of the electricity — "
                                         "\n reducing your energy bill and your carbon footprint."

                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    bulbs.pack(pady=20)
    bulbs.place(x=20, y=70)

    filter = Label(tips_page_window, text=" Refresh your air filters "
                                         "\n Clean — by vacuuming or rinsing with water — or replace your HVAC filters every three months."
                                          "\n  Your heater or air conditioning will blow more efficiently and draw less power."

                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    filter.pack(pady=20)
    filter.place(x=20, y=160)

    devices = Label(tips_page_window, text=" Pull the plug on your devices"
                                          "\n Thanks to standby mode, electronic devices consume power even when they are turned off. "
                                           "\n Almost 10 percent of your energy bill goes toward this -phantom power- consumption. "
                                           "\n Save money — and reduce your carbon footprint — "
                                           "\n by unplugging your devices at the end of the day or when they’re not in use."


                   ,
                   font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    devices.pack(pady=20)
    devices.place(x=20, y=210)

    electronics = Label(tips_page_window, text=" Opt for refurbished electronics"
                                           "\n If you're in the market for a new phone or computer, consider picking up a refurbished unit."
                                               "\n You'll keep at least one device from languishing in a landfill while reducing the environmental "
                                               "\n impact posed by manufacturing and "
                                               "\n shipping a new unit from overseas. If your device is damaged beyond repair,"
                                               "\n a little research should point you to the right place to properly recycle it. "


                    ,
                    font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    electronics.pack(pady=20)
    electronics.place(x=20, y=290)

    carbon = Label(tips_page_window, text=" Calculate your carbon footprint"
                                           "\n Confused about where to start if you want to help the planet? Start by"
                                          "\n  taking inventory of your current level of carbon emissions, "
                                          "\n known as your carbon footprint: Carbon Footprint Calculator."


                    ,
                    font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    carbon.pack(pady=20)
    carbon.place(x=20, y=380)

    bike = Label(tips_page_window, text=" Bike to work"
                                           "\n Consider biking to work at least one day each week."
                                        "\n  You'll eliminate that day's commute-related CO2 emissions"
                                        "\n  (assuming you don't walk to work) "
                                        "\n and cut your emissions for the week by a minimum of 20 percent."



                    ,
                    font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    bike.pack(pady=20)
    bike.place(x=20, y=450)


    tips_page_window.mainloop()
