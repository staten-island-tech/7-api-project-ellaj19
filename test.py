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
    return pprint.pprint(data)

import tkinter
window = tk



meow = getmario("yoshi")
print(meow)

""" return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    } """
