import requests
def getmario(nintendo):
    response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={nintendo.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data
meow = getmario("yoshi")
print(meow)