# blocked cell = 0
# normal cell = 1
# goal = 'G'
# car = ['>', '<', '^', 'v']

HEIGHT = 5
WIDTH = 5
car = ['>', '<', '^', 'v']


def get_car_location(puzzle):
  for i in range(len(puzzle)):
    if puzzle[i] in car:
      return i

def generate_actions(puzzle):
  car_location = get_car_location(puzzle)
  actions = []
  if (car_location // HEIGHT != 0) and (puzzle[car_location-WIDTH] != 0): actions.append('^')
  if (car_location %  WIDTH  != (WIDTH -1)) and (puzzle[car_location+1] != 0): actions.append('>')
  if (car_location // HEIGHT != (HEIGHT-1)) and (puzzle[car_location+WIDTH] != 0): actions.append('v')
  if (car_location %  WIDTH  != 0) and (puzzle[car_location-1] != 0): actions.append('<')
  return actions

def apply_action(old_puzzle, action):
  puzzle = old_puzzle[:]
  car_location = get_car_location(puzzle)
  
  if action == '^':
    if puzzle[car_location-WIDTH] == 1:
      puzzle[car_location] = action
      puzzle[car_location], puzzle[car_location-WIDTH] = puzzle[car_location-WIDTH], puzzle[car_location]
    else:
      puzzle[car_location] = 1
      puzzle[car_location-WIDTH] = 'W'
  elif action == '>':
    if puzzle[car_location+1] == 1:
      puzzle[car_location] = action
      puzzle[car_location], puzzle[car_location+1] = puzzle[car_location+1], puzzle[car_location]
    else:
      puzzle[car_location] = 1
      puzzle[car_location+1] = 'W'
  elif action == 'v':
    if puzzle[car_location+WIDTH] == 1:
      puzzle[car_location] = action
      puzzle[car_location], puzzle[car_location+WIDTH] = puzzle[car_location+WIDTH], puzzle[car_location]
    else:
      puzzle[car_location] = 1
      puzzle[car_location+WIDTH] = 'W'
  elif action == '<':
    if puzzle[car_location-1] == 1:
      puzzle[car_location] = action
      puzzle[car_location], puzzle[car_location-1] = puzzle[car_location-1], puzzle[car_location]
    else:
      puzzle[car_location] = 1
      puzzle[car_location-1] = 'W'

  return puzzle

def check_puzzle(puzzle):
  for cell in puzzle:
    if cell == 'W':
      return True
  return False

def puzzle_cost(puzzle,action):
  car_location = get_car_location(puzzle)
  if action == puzzle[car_location]:
    return 1
  else:
    return 2

def h(puzzle):
  car_location = get_car_location(puzzle)
  goal_location = 0
  for i in range(len(puzzle)):
    if puzzle[i] == "G":
      goal_location = i
      break
  if (car_location != None):
    steps = abs( (car_location%WIDTH) - (goal_location%WIDTH) ) + abs((car_location//HEIGHT) - (goal_location//HEIGHT))
  else:
    steps = 0
  
  return steps