import requests

OMDB_API_KEY = ""
with open("api_key.env") as file:
    OMDB_API_KEY = file.read().strip()

if OMDB_API_KEY == "":
    exit(-1)

film = input("Geef een film: ")
while film != 'STOP':

    resource_uri = "http://www.omdbapi.com/"
    params = {
        "apikey": OMDB_API_KEY,
        "t": film
    }

    response = requests.get(resource_uri, params)
    response_data = response.json()

    for key in ['Title', 'Plot', 'imdbRating']:
        if key not in response_data:
            exit(-2)
        print(f"\t{key}: {response_data[key]}")

    print("-" * 120)

    film = input("Geef een film: ")
