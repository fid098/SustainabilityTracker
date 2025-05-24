
# disposal page
import tkinter
from tkinter import *

#this is a text filled page
#this only displays text relating to disposal and recycling methods

def disposal():
    disposal_page_window = tkinter.Tk()
    disposal_page_window.geometry("550x600")
    disposal_page_window.title("Disposal methods Page")
    disposal_page_window.config(bg="White")

    header = tkinter.Label(disposal_page_window, bg="white", fg="#4EB168", text="Disposal and recycling methods",
                           font=("Arial", 14))
    header.pack(pady=5)
    header.place(x=60, y=20)

    shoes = Label(disposal_page_window, text=" How to dispose of Sports Shoes and Pre-loved Footwear"
                                             "\n If they are still in good or wearable condition, they can also be donated to charity."
                                             " \n Check with your local council before putting used sports shoes in your kerbside rubbish or recycling bin."
                                             " \n Donate any pre-loved footwear that are still in good, wearable condition to your local charities, op shops, or resale venues."
                                             "\n OR "
                                             "\n Drop off used or pre-loved sport shoes at specific collection points throughout Australia."
                                             "\n For more info, look up Save our Soles or Tread Lightly."
                                             "\n OR"
                                             "\n There are a number of recycling organisations that can arrange a collection for your old shoes, "
                                             "\n along with other pieces of textile or clothing you'd like to recycle. "
                                             "\n Do you research to find a local organisation that could help you with this.",
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    shoes.pack(pady=20)
    shoes.place(x=20)

    mattress = Label(disposal_page_window, text=" How to dispose of Mattresses"
                                                "\n If your used mattress is in good condition, there are organisations and "
                                                "\n charities that may receive them as donations."
                                                " \n Various parts of a used mattress can also be upcycled into other things,"
                                                "\n  make sure you do your research for ideas before throwing it away."
                                                " \nThere are several organisations, such as recyclemymattress.com.au, that collect and"
                                                "\n  recycle mattresses and prevent them from reaching landfill. "
                                                "\n These organisations have collection points all around the country and work with major mattress brands. "
                                                "\n Always check with your local council and chosen mattress brand when you're looking to dispose of a used mattress."
                                                "\n OR "
                                                "\n A number of brands can now collect your used mattress to be recycled or disposed of responsibly,"
                                                "\n when you purchase a new one from them. "
                                                "\n Always check with your chosen mattress brand whether they provide a collection service for used mattresses."

                     , font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    mattress.pack(pady=20)
    mattress.place(x=20, y=150)

    bulbs = Label(disposal_page_window, text=" How to dispose of Light bulbs"
                                             "\n Some light bulbs contain materials which can be recycled at specialty drop-off locations."
                                             " \n Most local councils will accept fluorescent bulbs, halogen bulbs, incandescent bulbs, "
                                             "\n and LEDs for recycling at transfer stations. Your local library, stationery store, digital department store, "
                                             "\n or grocery shop may also be a collection point. "
                                             "\n Check with your local council for nearby recycling drop-off locations."
                                             "\n OR "
                                             "\n Always check with your local council to ensure that they accept light bulbs in general waste. "
                                             "\n Most councils will accept all kinds of light bulbs (with the exception of fluorescent bulbs) in general waste."
                                             "\n  To dispose, wrap the light bulb in some newspaper, then place into the rubbish bin. "
                                             "\n Please note: Compact fluorescent lamps and fluorescent tubes should NOT be disposed of in your household rubbish "
                                             "\n as they contain small amounts of mercury, "
                                             "\n which is a health and environmental hazard."

                  ,
                  font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    bulbs.pack(pady=20)
    bulbs.place(x=20, y=320)

    oil = Label(disposal_page_window, text=" How to dispose of Cooking Oil"
                                           "\n There are a few options to safely and sustainably dispose of cooking oil. "
                                           "\n Cooking oil should not be poured down the drain or flushed down the toilet, "
                                           "\n as it can easily cause clogged pipes once the oil has cooled."

                                           "\n OR "
                                           "\n Oil can be reused a couple of times by straining it through a sieve or cheese cloth after each use. "
                                           "\n Ensure the oil is cool to touch (not boiling hot) before doing this."

                ,
                font=("Helvetica", 7), bd=1, relief="sunken", justify="left")
    oil.pack(pady=20)
    oil.place(x=20, y=490)

    disposal_page_window.mainloop()