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

def getcat(cat):
    response = requests.get(f"https://api.edamam.com/api/recipes/v2/{cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data


meow = getcat("cookies")
print(meow)

""" return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    } """
