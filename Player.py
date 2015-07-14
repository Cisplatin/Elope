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
		__lt__(self, other) returns true if the other score is higher
		than the self score.
		"""
		return self.score < other.score
