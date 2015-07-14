from Player import Player

class ELO:
	
	DEFAULT_SCORE = 1000 # The default score for new players

	def __init__(self):
		"""
		__init__(self) initializes an empty ELO container used to hold
		all players involved in this specific scheme.
		"""		
		self.players = {}

	def add_player(self, player):
		"""
		add_player(self, player) adds player to the list of players
		in the scheme. They start with the average score of 1000.
		"""
		if player in self.players:
			raise Exception("There is already a player named %s." % player)
		self.players[player] = Player(ELO.DEFAULT_SCORE)

	def remove_player(self, player):
		"""
		remove_player(self, player) removes the player given from the
		list of players in the scheme.
		"""
		if not player in self.players:
			raise Exception("There is no player named %s." % player)
		del self.players[player]
