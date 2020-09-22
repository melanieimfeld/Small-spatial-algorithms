import random
import numpy as np
from collections import Counter

#lonely: count 0 or 1 ones - [i][j] turns to 0
#overpopulated: 4 or more ones - [i][j] turns to 0
#reproduction: [2-3] ones - [i][j] turns to 1

''''
[-6,6],[-5,6]                [5,6],[6,6]
[-6,5],[-5,5]                [5,5],[6,5]


i - 1 * (sign of i)

when i == -6:
  i - (1 * sign of i) = -5

when i == 6:
  i - (1 * sign of i) = 5

[-6,-5],[-5,-5]             [5,-5],[6,-5]   
[-6,-6],[-5,-6]             [5,-6],[6,-6]

'''
board = np.zeros((12,12))
board_copy = np.zeros((12,12))




test = np.array([
        [1,0,1],
        [1,1,1],
        [0,1,1]])

test2 = [1,0,0,0,1,1,0,1]

colIndex = 1
rowIndex = 1
d = 1


for rowIndex in range(len(board)):
      for colIndex in range(len(board[rowIndex])):
        print(("rowIndex: {}, colIndex:{}").format(rowIndex,colIndex))
        if (colIndex % 11 == 0) or (rowIndex % 11 == 0):
          print("left, right, top, down boundary")
        else:

          print("current number", board[rowIndex][colIndex])

          #find neighbors
          neighbors = board[rowIndex-1:rowIndex+1+d , colIndex-1:colIndex+1+d].flatten()

          #count 1 and 0
          counts = Counter(neighbors)
          print(counts)
          #identify status of cell
          if counts[1]==2 or  counts[1]==3: #reproduce
            print("reproduce")
            board[rowIndex][colIndex] = 1
          else: #die
            board[rowIndex][colIndex] = 0
            print("die")



class gameMatrix:
  def __init__(self, items):
    self.items = items
    self.board = np.zeros((self.items,self.items))
    self.d = 1
    
  def populate(self):
    for i in range(len(self.board)): #rows 12
      for j in range(len(self.board[i])): #cols 6
        self.board[i][j] = random.randint(0,1)

  def is_reproduction(self):
    for rowIndex in range(len(self.board)):
      for colIndex in range(len(self.board[rowIndex])):
     
        if (colIndex % self.items-1 == 0) or (rowIndex % self.items-1 == 0): #boundary conditions
          #print("left, right, top, down boundary")
          pass
        else:
          #find neighbors
          neighbors = self.board[rowIndex-1:rowIndex+1+self.d , colIndex-1:colIndex+1+self.d].flatten()
          #count 1 and 0
          counts = Counter(neighbors)
          #identify status of cell
          if counts[1]==2 or  counts[1]==3: #reproduce
            #print("reproduce")
            self.board[rowIndex][colIndex] = 1
          else: #die
            self.board[rowIndex][colIndex] = 0
            #print("die")

  def display(self):
    print(("Round: \n {}").format(self.board))


def main():
  turn = 0
  newboard = gameMatrix(6)
  newboard.populate() 
  #newboard.display()


  while turn < 3:
    turn += 1
    newboard.display()
    newboard.is_reproduction()
   
main()