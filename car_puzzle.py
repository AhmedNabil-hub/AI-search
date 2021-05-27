"""
Car Problem
---------------------
| G |   | X |   |   |
---------------------
|   |   |   |   |   |
---------------------
| X |   | > |   |   |
---------------------
|   |   | X |   |   |
---------------------
|   |   |   |   |   |
---------------------

[
  'G',1,0,1,1,
  1,1,1,1,1,
  0,1,'>',1,1,
  1,1,0,1,1,
  1,1,1,1,1
]
"""

# blocked cell = 0
# normal cell = 1
# goal = 'G'
# car = ['>', '<', '^', 'v']

from puzzle_functions import *
import random
import AiSearch

HEIGHT = 5
WIDTH = 5
car = ['>', '<', '^', 'v']

def print_puzzle(puzzle):
  S = ""
  
  for cell in puzzle:
    if   cell == 0: S += "X"
    elif cell == 1: S += " "
    elif cell == "G": S += "G"
    elif cell in car : S += cell
    else: S += "W"
    
  print("-"*5*WIDTH)
  for cell in range(len(S)):
    print("| " + S[cell] + " |", end="")
    if ((cell+1) % WIDTH) == 0:
      print()
      print("-"*5*WIDTH)

def puzzle_shuffle():
  rand_dir = random.sample(car, 1)
  num_blocks = random.randint(0,WIDTH*HEIGHT//3)
  rand_state = [0]*num_blocks
  rand_state += [1]*(WIDTH*HEIGHT-num_blocks-2)
  rand_state += rand_dir
  rand_state.append("G")
  random.shuffle(rand_state)
  
  return rand_state


def human_solve(puzzle):
  puzzle=puzzle[:]
  while (True):
    print_puzzle(puzzle)
    available_actions=generate_actions(puzzle)
    if (len(available_actions) > 0):
      print('available actions: ' + ' , '.join(available_actions))
      action=input("your action:")
      if action not in available_actions:
        print('Game Over')
        return
      puzzle=apply_action(puzzle,action)
      if check_puzzle(puzzle):
        print_puzzle(puzzle)
        print("You win")
        return
    else:
      print("No Solution")

def computer_solve(puzzle,strategy,h=None,flag=False):
  S=AiSearch.solve(strategy,puzzle,generate_actions,apply_action,check_puzzle,puzzle_cost,h)
  print(strategy)
  if (S != "failure"):
    for i in S:
      print(i,": ",S[i])
    print('-'*50)
    if flag:
      puzzle=puzzle[:]
      print_puzzle(puzzle)
      for action in S['solution']:
        puzzle=apply_action(puzzle,action)
        print_puzzle(puzzle)
  else:
    print("No Solution")

# puzzle = [
#   1,1,1,0,0,
#   0,1,0,0,1,
#   "^",1,1,0,0,
#   1,1,"G",1,1,
#   1,1,1,0,1
# ]


puzzle = puzzle_shuffle()

# print_puzzle(puzzle)

# human_solve(puzzle)
# computer_solve(puzzle,'DFS', None, True)
# computer_solve(puzzle,'BFS', None, True)
# computer_solve(puzzle,'UCS', None, True)
# computer_solve(puzzle,'Greedy',h, True)
# computer_solve(puzzle,'Astar',h, True)





