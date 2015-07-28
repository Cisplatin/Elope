class Player:

    MAX_DIFFERENCE = 400 # Maximum score difference for effect change
    
    THRESHHOLD_MATCHES = 30 # Minimum number of matches a player has to play
                            # for their k factor to be assigned other than 40
    THRESHHOLD_SCORE = 2400 # Minimum score for players to have a kfactor change                                

    K_TIER1 = 40 # the kfactor for a player with less than threshhold_matches
    K_TIER2 = 20 # the kfactor for a player who's score has never been above
    K_TIER3 = 10 # the kfactor for a player who's score has been above
    
    WIN = 1   # Points earned for a victory
    TIE = 0.5 # Points earned for a tie
    LOSE = 0  # Points earned for a lose

    def __init__(self, score):
        """
        __ init__(self, score) creates and returns new player with 
        the given score.
        """
        self.score = score
        self.wins = 0
        self.ties = 0
        self.loses = 0
        self.been_above_threshhold_score = False

    def __eq__(self, other):
        """
        __eq__(self, other) returns true if the scores of the two given
        players are equal, false otherwise.
        """
        return self.score == other.score

    def __lt__(self, other):
        """
        __lt__(self, other) returns true if the self score is less
        than the other score.
        """
        return self.score < other.score

    def __gt__(self, other):
        """
        __gt__(self, other) returns true if the self score is greater
        than the other score.
        """
        return self.score > other.score

    def __le__(self, other):
        """
        __le__(self, other) returns true if the self score is less than 
        or equal to the other score.
        """
        return self.score <= other.score

    def __ge__(self, other):
        """
        ___ge___(self, other) returns true if the self score is greater 
        than or equal to the other score. 
        """
        return self.score >= other.score

    def __iadd__(self, arg):
        """
        ___iadd__(self, arg) adds the arg value to the player's score.
        """
        if (self.score + arg >= Player.THRESHHOLD_SCORE):
            self.been_above_threshhold_score = True

        return self.score + arg

    def __isub__(self, arg):
        """
        __isub__(self, arg) subtracts the arg value from the 
        player's score.
        """
        return self.score - arg

    def get_score(self):
        """
        get_score(self) returns the score of the player.
        """
        return self.score

    def set_score(self, new_score):
        """
        get_score(self, new_score) sets the players score to new_score.
        """
        if (new_score >= Player.THRESHHOLD_SCORE):
            self.been_above_threshhold_score = True
        self.score = new_score

    def get_matches(self):
        """
        get_matches(self) returns the total number of matches played by 
        this player over all time.
        """
        return self.wins + self.ties + self.loses

    def expected_score_against(self, other):
        """
        expected_score_against(self) returns the expected score against
        the other player.
        """
        ratio = (other.get_score() - self.score) / float(Player.MAX_DIFFERENCE)
        return 1 / (1 + 10 ** ratio)

    def k_factor(self):
        """
        k_factor returns the development coefficient for a specific player
        based on the following rules
        k is 40 for a player who has played less than THRESHHOLD_MATCHES
        k is 20 for a player who's rating is under THRESHHOLD_SCORE
        k is 10 for a player whos rating has ever been above THRESHHOLD_SCORE
        """
        if (self.get_matches() < Player.THRESHHOLD_MATCHES): 
            return Player.K_TIER1
        elif (self.been_above_threshhold_score):
            return Player.K_TIER3
        else:
		    return Player.K_TIER2        

    def beats(self, other):
        """
        beats(self, other) updates the ELO score of the two players where
        self player beats the other player.
        """
        new_rating = (self.score + self.k_factor() * 
                     (Player.WIN - self.expected_score_against(other)))
        self.score = int(new_rating)
        new_rating = (other.score + other.k_factor() *
                     (Player.LOSE - other.expected_score_against(self)))
        other.score = int(new_rating)
