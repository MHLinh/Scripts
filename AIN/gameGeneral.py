import nashpy as nash
import numpy as np

# A function to compute all the combinations of strategies 
# that can be played by the players.
# Parameters:
#   row_size - the number of rows (row strategies)
#   col_size - the number of columns (column strategies)
def get_strategie_loc(row_size, col_size):
  strat_loc = []
  for i in range(row_size):
    row = [0 for k in range(row_size)]
    row[i] = 1
    for j in range(col_size):
      col = [0 for k in range(col_size)]
      col[j] = 1
      strat_loc.append((np.array(row),np.array(col)))
  return strat_loc

# A function to compute the nash equilibria of a game.
# Parameters:
#   game - nashpy game generated from two matrices
#   strat_loc - all combinations of strategies of the players
def nashEquilibrium(game, strat_loc):
  print()
  print("Nash Equilibrium")
  for each_strat_loc in strat_loc:
    strat = game[each_strat_loc[0], each_strat_loc[1]]
    outcome = game.is_best_response(each_strat_loc[0], each_strat_loc[1])
    if outcome[0] and outcome[1]:
      print(f"Row {each_strat_loc[0].argmax()+1}, Col {each_strat_loc[1].argmax()+1}: {strat}")
      
# A function to compute the pareto optimal strategies of a game.
# Parameters:
#   game - nashpy game generated from two matrices
#   strat_loc - all combinations of strategies of the players
def pareto_optimal(game, strat_loc):
  strats = [game[each_strat_loc[0], each_strat_loc[1]] for each_strat_loc in strat_loc]  
    
  print()
  print("Pareto Optimal")
  
  for each_strat_loc in strat_loc:
    strat = game[each_strat_loc[0], each_strat_loc[1]] # 3 0
    PO = True
    for each_strat in strats:
      if each_strat[0] > strat[0] and each_strat[1] >= strat[1]:
        PO = False
        break
      elif  each_strat[0] >= strat[0] and each_strat[1] > strat[1]:
        PO = False
        break
      
    if PO:
      print(f"Row {each_strat_loc[0].argmax()+1}, Col {each_strat_loc[1].argmax()+1}: {strat}")

# A function to compute the social welfare of strategies of a game.
# Parameters:
#   game - nashpy game generated from two matrices
#   strat_loc - all combinations of strategies of the players
def social_welfare(game, strat_loc):
  strats = [game[each_strat_loc[0], each_strat_loc[1]] for each_strat_loc in strat_loc]  
  sum_utility = [sum(each) for each in strats]
  max_utility = max(sum_utility)
  min_utility = min(sum_utility)

  print()
  print("Social Welfare")
  print(f"Max Uitlity {max_utility}, Min Utility {min_utility}")

  for each_strat_loc in strat_loc:
    strat = game[each_strat_loc[0], each_strat_loc[1]]
    sumU = sum(strat)
    if sumU == max_utility:
      print(f"Row {each_strat_loc[0].argmax()+1}, Col {each_strat_loc[1].argmax()+1}: {strat} Maximises")
    
    if sumU == min_utility:
      print(f"Row {each_strat_loc[0].argmax()+1}, Col {each_strat_loc[1].argmax()+1}: {strat} Minimises")

# A function to compute the mixed nash equilibria of a game.
# Parameters:
#   game - nashpy game generated from two matrices
#   strat_loc - all combinations of strategies of the players
def mixed(game):

  equilibria = game.support_enumeration()

  print()
  print("Mixed strategy equilibria")

  for eq in equilibria:
    print()
    row = eq[0]
    col = eq[1]

    print("Row player")
    for index, prob in enumerate(row):
      print(f"Strat {index + 1} with probability: {prob}")

    print()
    print("Column player")
    for index, prob in enumerate(col):
      print(f"Strat {index + 1} with probability: {prob}")

# A function to compute the utilities of a game.
# Parameters:
#   game - nashpy game generated from two matrices
#   probs - probabilities of playing the strategies
def get_utilities(game, probs):
  u = game[probs[0], probs[1]]
  print()
  print("Mixed strategy utility")
  print(f"With given prob row player utility: {u[0]}, col player utility: {u[1]}")

# I = np.array([[3, 2], [1, 4]])
# J = np.array([[3, 4], [1,2]])
# game = nash.Game(I, J)
# print()
# print("Game")
# print(game)

# equilibria = game.support_enumeration()

# for eq in equilibria:
#   print()
#   print(eq)

# I = np.array([[3, -1], [0, 1]])
# J = np.array([[-3, 1], [0, -1]])
# game = nash.Game(I, J)
# print()
# print("Game")
# print(game)

# equilibria = game.support_enumeration()

# for eq in equilibria:
#   print()
#   print(eq)

# I = np.array([[3, 2], [1, 4]])
# J = np.array([[3, 4], [1, 2]])
# I = np.array([[4, 1], [1, 4]])
# J = np.array([[4, 5], [5, 4]])

I = np.array([[2, 12, 4], [6, 4, 4], [4, 4, 6]])
J = np.array([[12, 14, 4], [10, 2, 8], [6, 2, 6]])
# I = np.array([[3,-1], [0, 1]])
# J = np.array([[-3, 1], [0, -1]])
# I = np.array([[2, 0], [0, 1]])
# J = np.array([[1, 0], [0, 2]])
game = nash.Game(I, J)

print()
print("Game")
print(game)

# mixed(game)
# dominantStrategy(I,J)

# getUtilities(game, [[0.5, 0.5], [1/100, 99/100]])

strat_locs = get_strategie_loc(3, 3)

nashEquilibrium(game, strat_locs)
paretoOptimal(game, strat_locs)
socialWelfare(game, strat_locs)