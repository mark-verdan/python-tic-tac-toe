matrix_temp = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]


matrix_dict = { "1": (0,0) , "2" : (0,1) ,"3": (0,2) ,
"4": (1,0), "5": (1,1), "6": (1,2),
"7": (2,0), "8": (2,1), "9": (2,2) } 


def player_move(player):
    while True:
       try: 
          core = input(f"{player}, Choose your position!(1-9): ").strip()
          row, col = matrix_dict[core] 
          
          if matrix_temp[row][col] != " ":
              print("Nope.")
              continue
          elif matrix_temp[row][col] == " ":
              matrix_temp[row][col] = player
              
          for clo in matrix_temp:
              print(clo)
          break
              
       except KeyError:
           print("Invalid..") 
           continue 

def win_condi(player):
    for row in matrix_temp:
        if all(cell == player for cell in row):
            print(f"{player} has won!! ") 
            return True
    for col in range(3):
        if all(matrix_temp[row][col] == player for row in range(3)):
            print(f"{player} has won!! ")
            return True
    if all(matrix_temp[i][i] == player for i in range(3)):
        print(f"{player} has won!! ") 
        return True
    elif all(matrix_temp[i][2-i] == player for i in range(3)):
        print(f"{player} has won!! ") 
        return True
     
    return False

def draw():
    if all(matrix_temp[i][j] != " " for i in range(3) for j in range(3)):
        print("Draw..") 
        return True
        
    return False   

print("Welcome to THE simple XOX program") 

for i in matrix:

  print(i)
 
while True:
     player_move("X")
     if win_condi("X"):
         break
     if draw():  
         break  
     player_move("O")
     if win_condi("O"):
         break
     if draw():
         break