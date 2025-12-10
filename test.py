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

def getmario(nintendo):
    response = requests.get(f"https://www.amiiboapi.com/api/{nintendo.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
         "amiiboSeries": data["amiiboSeries"],
			"character": data["character"],
			"gameSeries": data["gameSeries"],
			"head": data["head"],
			"image": data["image"],
			"name": data["name"],
			"release": data["release"],
			"tail": data["tail"],
			"type": data["type"]
    }


meow = getmario("amiibo/?name=yoshi")
print(meow)

""" return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    } """
