import os
import random
import time
from IA import Intelligence

def clear_and_write():
  os.system("clear")
  write_table(matrix)

def write_table(matrix): 
  for i in range(0,9):
    print("|{0}: {1} ".format(i+1, matrix[i]), end="")
    if i == 2 or i==5:
      print("")
      print("-" * 17)

  return print("")

def computer_move(matrix): #optimize
  position_of_void = []
  count = 0

  print("Thinking move...")
  time.sleep(2)
  
  for element in matrix:
    if element == " ":
      position_of_void.append(count + 1)
    count += 1

  if len(position_of_void) == 0:
    return False
  
  while True:
    state = random.randrange(1, 10)
    for element in position_of_void:
      if element == state:
        matrix[state - 1] = "O"
        return matrix
      
      

def verify_game_over(computer_state, matrix):
  ia = Intelligence()

  winner = ia.verify_player_win(matrix)

  if winner:
    print("The human win")
    return True
  
  if winner == False:
    print("The computer win")
    return True

  if computer_state == False:
    print("Draw")
    return True

def human_move(matrix):
  position = 0

  position = int(input("Give me the position: "))
  matrix[position - 1] = "X"

  return matrix


matrix = [" "] * 9
position_computer = 4

while True: #optimize
  clear_and_write() 
  
  #Human
  matrix = human_move(matrix)
  clear_and_write()
  
  if verify_game_over(position_computer, matrix):
    break

  #Computer
  position_computer = computer_move(matrix)

  if position_computer != False:
    matrix = position_computer
  clear_and_write()

  if verify_game_over(position_computer, matrix):
    break
  
  