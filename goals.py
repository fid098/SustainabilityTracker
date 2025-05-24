
# goals

import tkinter
from PIL import Image, ImageTk  # allows me to display images
from tkinter import *
import PIL.Image as Image
from PIL import ImageFont
from PIL import ImageDraw

#this is a text filled page
#this only displays text relating to sustainability goals

def goals():
    goals_page_window = tkinter.Tk()
    goals_page_window.geometry("550x450")
    goals_page_window.title("Sustainability goals")
    goals_page_window.config(bg="White")

    poverty= Label(goals_page_window, text=" No Poverty"
                                           "\n End poverty in all its forms everywhere."
                                           " \n Eradicating poverty is not a task of charity, it’s an act of justice and the key to unlocking an enormous human potential"
                                           " \n Still, nearly half of the world’s population lives in poverty,"
                                           "\n and lack of food and clean water is killing thousands every single day of the year.."
                                           "\n Together, we can feed the hungry, wipe out disease and give everyone in the world a chance to prosper "
                                           "\n and live a productive and rich life", font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    poverty.pack(pady=20)
    poverty.place(x=20)


    hunger = Label(goals_page_window, text=" End hunger"
                                           "\n End hunger, achieve food security and improved nutrition and promote sustainable agriculture."
                                           " \n Hunger is the leading cause of death in the world. Our planet has provided us with tremendous resources."
                                           " \n But unequal access and inefficient handling leaves millions of people malnourished. "
                                           "\n If we promote sustainable agriculture with modern technologies and fair distribution systems,"
                                           "\n we can sustain the whole world’s population and make sure that nobody will ever suffer from hunger again.", font=("Helvetica", 7), bd=1, relief="sunken", justify="left")

    hunger.pack(pady=20)
    hunger.place(x=20, y=100)

    energy =  Label(goals_page_window, text=" Ensure access to affordable, reliable, sustainable and modern energy for all"
                                           "\n Renewable energy solutions are becoming cheaper, more reliable and more efficient every day"
                                           " \n  Our current reliance on fossil fuels is unsustainable and harmful to the planet,"
                                           " \n which is why we have to change the way we produce and consume energy. "
                                           "\n  Implementing these new energy solutions as fast as possible is essential to counter climate change,"
                                           "\n one of the biggest threats to our own survival.", font=("Helvetica", 7), bd=1, relief="sunken", justify="left")

    energy.pack(pady=20)
    energy.place(x=20, y=190)

    climate = Label(goals_page_window, text=" Take urgent action to combat climate change and its impacts"
                                           "\n Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries", font=("Helvetica", 7), bd=1, relief="sunken", justify="left")

    climate.pack(pady=20)
    climate.place(x=20, y=280)

    economic = Label(goals_page_window,
                   text=" Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all."
                        "\n Economic growth should be a positive force for the whole planet."
                        " \n  This is why we must make sure that financial progress creates decent and"
                        "\n fulfilling jobs while not harming the environment. "
                        " \n We must protect labour rights and once and for all put a stop to modern slavery and child labour. "
                        "\n If we promote job creation with expanded access to banking and financial services, "
                        "\n we can make sure that everybody gets the benefits of entrepreneurship and innovation.", font=("Helvetica", 7), bd=1,
                   relief="sunken", justify="left")

    economic.pack(pady=20)
    economic.place(x=20, y=320)


    goals_page_window.mainloop()

