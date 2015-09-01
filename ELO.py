from Player import Player

class ELO:
    
    DEFAULT_SCORE = 1000 # The default score for new players

    def __init__(self):
        """
        __init__(self) initializes an empty ELO container used to hold
        all players involved in this specific scheme.
        """        
        self.players = {}
        self.game_count = 0

    def add_player(self, player):
        """
        add_player(self, player) adds player to the list of players
        in the scheme. They start with the average score of 1000.
        """
        if player in self.players:
            raise Exception("There is already a player named %s." 
                    % player)
        else:
            self.players[player] = Player(ELO.DEFAULT_SCORE)

    def remove_player(self, player):
        """
        remove_player(self, player) removes the player given from the
        list of players in the scheme.
        """
        if not player in self.players:
            raise Exception("There is no player named %s."
                    % player)
        else:
            del self.players[player]

    def get_player(self, player):
        """
        get_player(self, player) returns the player with the given name
        """
        if not player in self.players:
            raise Exception("There is no player names %s."
                    % player)
        else:
            return self.players[player]

    def get_all_players(self):
        """
        get_all_players(self, player) returns a list of all players
        """
        return self.players

    def number_of_players(self):
        """
        number_of_players(self) returns the number of players in this
        scheme.
        """
        return len(self.players)

    def average_score(self):
        """
        average_score(self) returns the average score of all players in
        the given ELO scheme.
        """
        player_count = self.number_of_players()
        if player_count == 0:
            raise Exception("Cannot find the average score of "
                    "0 players.")
        else:
            total = sum([self.players[player].get_score()
                     for player in self.players])
            return total / self.number_of_players()

    def game(self, player1, player2):
        """
        player1 beats player2, this function should adjust their ELO scores
        """
        if not player1 in self.players or not player2 in self.players:
            raise Exception("Cannot find one or either players")
        else:
            self.players[player1].beats(self.players[player2])
            return
	   
    def tie(self, player1, player2):
        """
        player1 and player2 play a game and tie   
        """ 
        if not player1 in self.players or not player2 in self.players:
            raise Exception("Cannot find one or either players")
        else:
            self.players[player1].ties(self.players[player2])
            return
