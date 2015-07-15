class Player:

	def __init__(self, score):
		"""
		__ init__(self, score) creates and returns new player with 
		the given score.
		"""
		self.score = score
		self.wins = 0
		self.ties = 0
		self.loses = 0

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
         __iadd__(self, arg) adds the arg value to the player's score.
        """
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
		self.score = new_score

	def get_matches(self):
		"""
		get_matches(self) returns the total number of matches played by 
		this player over all time.
		"""
		return self.wins + self.ties + self.loses
