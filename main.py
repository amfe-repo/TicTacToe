import os
import random
import time

def clear():
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
  state = random.randrange(1, 10)
  position_of_void = []
  count = 0
  
  for element in matrix:
    if element == " ":
      position_of_void.append(count + 1)
    count += 1

  if len(position_of_void) == 0:
    return False
  
  while True:
    for element in position_of_void:
      if element == state:
        return state
      state = random.randrange(1, 10)
      
  

matrix = [" "] * 9
position = 0
position_computer = 0

while True:
  clear() #modify

  #Put in functions
  #Human
  position = int(input("Give me the position: "))
  matrix[position - 1] = "X"
  clear()

  #Computer
  print("Thinking move...")
  time.sleep(2)
  position_computer = computer_move(matrix)

  if position_computer == False:
    print("The game is over")
    break
  else:
    write_table(matrix)
    matrix[position_computer - 1] = "O"
    
  clear()
  
    
