import requests

def getdog(RandomDog):
    response = requests.get(f"https://random.dog/woof.json{RandomDog.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "size": data["fileSizeBytes"],
        "image": data["url"]
    }

dog = getdog("Golden Retriever")
print(dog)