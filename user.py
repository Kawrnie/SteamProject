from list import load_user_likes, save_user_likes
from game import GameCatalog

class User:
    def __init__(self, name):
        self.name = name
        self.liked_game_ids = set(load_user_likes(name))

    def like_game(self, appid, catalog):
        if appid not in self.liked_game_ids:
            game = catalog.get_game_obj(appid)
            if game:
                self.liked_game_ids.add(appid)
                save_user_likes(self.name, list(self.liked_game_ids))
                return f"Added {game.title}!"
            return "Game not found."
        return "Already in your list."
    
    def get_common_games(self, other_user, catalog):
        common_ids = self.liked_game_ids.intersection(other_user.liked_game_ids)

        common_games = []
        for appid in common_ids:
            game = catalog.get_game_obj(appid)
            if game:
                common_games.append(game)
        return common_games 

    def get_compatibility_with(self, other_user):
        if not self.liked_game_ids or not other_user.liked_game_ids:
            return 0.0
            
        common_ids = self.liked_game_ids.intersection(other_user.liked_game_ids)
        total_unique_likes = self.liked_game_ids.union(other_user.liked_game_ids)
        
        return len(common_ids) / len(total_unique_likes)