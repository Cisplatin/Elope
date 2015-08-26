# Elope
An implementation of the Elo rating system in Python.

Intended for use with Python v2.7.6.

Following is an example of how the libraries may be used:

```Python
import ELO

# Initialize the game, add some players
ELO = ELO.ELO()
ELO.add_player("Simon")
ELO.add_player("David")

# Print out the scores before the games
print("Before playing...")
print("Simon's score is %d" % ELO.get_player("Simon").score)
print("David's score is %d" % ELO.get_player("David").score)

# Simon beats David, David beats Simon, then Simon beats David again
ELO.game("Simon", "David")
ELO.game("David", "Simon")
ELO.game("Simon", "David")

# Print out the scores after the games
print("After playing...")
print("Simon's score is %d" % ELO.get_player("Simon").score)
print("David's score is %d" % ELO.get_player("David").score)
```
