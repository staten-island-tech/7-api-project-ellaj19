import requests

""" def getfruit(fruit):
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data


fruit = getfruit("strawberry")
print(fruit) """
import pprint

def getmario(nintendo):
    response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={nintendo.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return pprint.pformat(data)

import tkinter
from tkinter import *
def say_hello():
    thing = getmario(responses.get())
    label.config(text =thing)
window =  Tk()
window.title("Nintendo!")
my_button = Button(window, text="what nintendo character would you like to see?", command=say_hello, font=("Limelight",16), bg="lightblue", fg="black", relief="raised", padx = 10, pady = 5)
my_button.pack()

responses = Entry(window, width= 30)
responses.pack()

label = Label(window, text="", wraplength= 800)
label.pack()
window.mainloop()
meow = getmario("yoshi")
print(meow)

""" return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    } """
