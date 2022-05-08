import requests

# read credentials from a file
with open('artsy_credentials.txt') as credentials:
    client_id = credentials.readline().strip()
    client_secret = credentials.readline().strip()

# get auth token
res = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                   data={
                       "client_id": client_id,
                       "client_secret": client_secret
                   })
token = res.json()['token']
headers = {"X-Xapp-Token" : token}

# read artist ids from a file, check with API and add to the dict
artist_data = {}
with open('artists.txt', 'r') as artists:
    for artist in artists:
        res = requests.get(f"https://api.artsy.net/api/artists/{artist.strip()}", headers=headers)
        data = res.json()
        artist_data[data["sortable_name"]] = data["birthday"]

# sort data by year and name
sorted_artist_data = sorted(artist_data.items(), key=lambda x: (x[1], x[0]))

# print sorted names to a file
with open('artists_result.txt', 'w') as result:
    for artist in sorted_artist_data:
        print(artist[0])
