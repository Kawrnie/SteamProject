import requests
import json
import re

def extract_appid(url):
    match = re.search(r"/app/(\d+)", url)
    return int(match.group(1)) if match else None

class Game:
    def __init__(self, appid, title, genres):
        self.appid = appid
        self.title = title
        self.genres = genres
        self.poster_url = f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{appid}/library_600x900_2x.jpg"
        
    def to_dict(self):
        return {
            "appid": self.appid,
            "title": self.title,
            "genres": self.genres,
            "poster_url": self.poster_url
        }

    def get_game_name(appid):
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}"

        response = requests.get(url)
        data = response.json()

        if data and data[str(appid)]["success"]:
            game_info = data[str(appid)]["data"]
            return game_info["name"]
        return None 
        
class GameCatalog:
    def __init__(self, filename="catalog.json"):
        self.filename = filename
        self.catalog = self._load_catalog()

    def _load_catalog(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _fetch_from_steam(self, appid):
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()

            if data and data[str(appid)]["success"]:
                info = data[str(appid)]["data"]
                genres = [g["description"] for g in info.get("genres", [])]
                return {
                    "title": info["name"],
                    "genres": genres
                }
        except Exception as e:
            print(f"Error connecting to Steam: {e}")
            
        return None

    def get_game_obj(self, appid):
        appid_str = str(appid)
        if appid_str not in self.catalog:
            data = self._fetch_from_steam(appid)
            if data:
                self.catalog[appid_str] = data
                self.save_catalog()
            else:
                return None
        game_data = self.catalog[appid_str]
        return Game(
            appid=appid, 
            title=game_data["title"], 
            genres=game_data["genres"]
        )    

    def save_catalog(self):
        with open(self.filename, "w") as f:
            json.dump(self.catalog, f, indent=4)
