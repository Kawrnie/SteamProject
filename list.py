import json
import os

def save_user_likes(username, appid_list):
    filename = f"user_{username}.json"
    with open(filename, "w") as f:
        json.dump(appid_list, f, indent=4)

def load_user_likes(username):
    filename = f"user_{username}.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_all_users():
    users = []

    for filename in os.listdir("."):
        if filename.startswith("user_") and filename.endswith(".json"):
            username = filename[5:-5]
            users.append(username)
    return users