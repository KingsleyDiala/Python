letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {x:y for x, y in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)
#We want to create a function that will take in a word and return how many points that word is worth
def score_word(word):
  point_total = 0
  for x in word:
    point_total += letter_to_points.get(x, 0)
  return point_total
# Let's test this function! Create a variable to test if the fuctions works properly.
brownie_points = score_word('BROWNIE')
print(brownie_points)

# ________ SCORE A GAME ________
# Creating a block of code that contains the mapping of players o how many points they've scored.

# Creating a new dictionary
player_to_words = {'BLUE': ['EARTH', 'ERASER', 'ZAP'], 'TENNIS': ['EYES', 'BELLY', 'COMA'], 'EXIT': ['MACHINE', 'HUSKY', 'PERIOD']}

player_to_points = {}
for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)






