class Intelligence: #verify scope
  #Need implement diagonal verify

  def verify_diagonal(mt):
    if mt[4] != " ":
      if mt[0]==mt[4]==mt[8] or mt[2]==mt[4]==mt[6]:
        if mt[4] == "X":
          return True
        else:
          return False
    
  def verify_horizontal(mt):
    count = 0

    for i in range(0,3): 
      if mt[count]!=" " or mt[count+1]!=" " or mt[count+2] != " ":
        if mt[count]==mt[count+1]==mt[count+2]:
          if mt[count] == "X":
            return True
          else:
            return False
      
      count += 3

  def verify_vertical(mt):
    for i in range(0,3):
      if mt[i]!=" " or mt[i+3]!=" " or mt[i+6] != " ":
        if mt[i]==mt[i+3]==mt[i+6]:
          if mt[i] == "X":
            return True
          else:
            return False
      
      
  def verify_player_win(self, matrix):
    state = 4

    #Horizontal Line
    state = Intelligence.verify_horizontal(matrix)
    if state == True or state == False:
      return state
    
    #Vertical line
    state = Intelligence.verify_vertical(matrix)
    if state == True or state == False:
      return state
    
    #Diagonal Line
    state = Intelligence.verify_diagonal(matrix)
    if state == True or state == False:
      return state
  