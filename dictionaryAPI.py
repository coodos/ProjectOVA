import requests

baseURL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

def getMeaning(word):
    try: 
        data = requests.get(baseURL.format(word))
        return data.json()[0]["meanings"][0]["definitions"][0]["definition"]
    except Exception: 
        return None