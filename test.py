import requests

def getcat(cat):
    response = requests.get(f"https://api.thecatapi.com/v1/images/search{cat.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    for key, value in cat.items():
        print(key, "→", value)

    data = response.json()
    return {
        "id": data["id"],
        "url": data["url"],
        "width": data["width"],
        "height": data["height"]
    }


cat = getcat("cv9")
print(cat)