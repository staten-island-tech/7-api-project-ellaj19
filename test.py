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
    return data

import tkinter
from tkinter import *
def say_hello():
    thing = getmario(responses.get())
    label.config(text =thing)
window =  Tk()
window.title("Nintendo!")
window.geometry("1500x900")
window.resizable(False, False)
my_button = Button(window, text="big ol red button to press", command=say_hello, font=("Helvetica",16), bg="red", fg="black", relief="raised", padx = 10, pady = 5)
my_button.pack()

label = Label(window, text="search an amiibo below", wraplength= 800)
label.pack() 

responses = Entry(window, width= 30)
responses.pack()


window.mainloop()
meow = getmario("yoshi")
print(meow)

""" return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    } """
