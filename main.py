from game import GameCatalog, extract_appid
from list import get_all_users
from user import User


def main():
    catalog = GameCatalog("catalog.json")
    name = input("Enter your username: ").strip()
    current_user = User(name)

    print(f"\nWelcome {current_user.name}!")
    print("Commands: paste a link to add, 'compare [name]' to see the common games, list-users to see other users, or 'quit'.")
          
    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() == 'quit':
            break

        if user_input.lower() == "list-users":
            users = get_all_users()
            if users:
                print("\nRegistered Users:")
                for u in users:
                    prefix = " (you)" if u == current_user.name else ""
                    print(f" - {u}{prefix}")
            else:
                print("No other users found.")
            continue

        if user_input.lower().startswith("compare "):
            other_name = user_input.split(" ", 1)[1]
            other_user = User(other_name)

            common = current_user.get_common_games(other_user, catalog)
            score = current_user.get_compatibility_with(other_user)

            print(f"\nComparing with {other_name}:")
            print(f"Compability Score: {score:.1%}")
            if common:
                print("Games you both like:")
                for game in common:
                    print(f" - {game.title}")
            else:
                print("No games in common yet!")
            continue

        appid = extract_appid(user_input)

        if appid:
            result_message = current_user.like_game(appid, catalog)
            print(result_message)
        else:
            print("Invalid command or URL")

if __name__ =="__main__":
  main()