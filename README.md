# SteamProject v 0.1

Add steam games to your list using links like "https://store.steampowered.com/app/105600/Terraria/" and compare with your friends list to find games you both enjoy.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
Run the program with: `python3 main.py`

Commands inside the app:
- Paste a Steam URL: Adds a game to your list (e.g., https://store.steampowered.com/app/400/Portal/).
- list-users: See a list of all registered users. (User needs to add something before showing up on list)
- compare [username]: See which games you and another user both like, along with a compatibility score.
- quit: Exit the program safely.