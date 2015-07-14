class Player:

	def __init__(self, score):
		"""
		__ init__(self, score) creates and returns new player with 
		the given score.
		"""
		self.score = score

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
		__le__(self, other) returns true if the self score is less than 		or equal to the other score.
		"""
		return self.score <= other.score

	def __ge__(self,other):
		"""
		___ge___(self, other) returns true if the self score is greater 		than or equal to the other score. 
		"""

	def getScore(self):
		"""
		score(self) returns the score of the player.
		"""
		return self.score

	def changeScore(self, change):
		"""
		changScore(self, change) increases the score of the player by 
		the value given in change.
		"""
		self.score += change
	
	
a = Player()
b = Player()
a == b
