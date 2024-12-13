# This object will represent a game.
# @author Matt Wilson

class Boardgame:
    
    # Needed values
    # id, name, url, rating, max player, min player, results
    def __init__(self, id, name, geek_rating, max_player, min_player):
        self.id = id
        self.name = name
        self.geek_rating = geek_rating
        self.max_player = max_player
        self.min_player = min_player
        self.p_count_results = []

