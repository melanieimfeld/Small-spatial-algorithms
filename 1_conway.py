import random
import numpy as np
from collections import Counter

NUMRUNS = 3 #defines how often to reproduce

def reassignCell(neighbors):
  counts = Counter(neighbors)
  if counts[1]==2 or  counts[1]==3: #reproduce
    print("reproduce")
    board[rowIndex][colIndex] = 1
  else: #die
    board[rowIndex][colIndex] = 0
    print("die")

class gameMatrix:
  def __init__(self, items, turn):
    self.items = items
    self.board = np.zeros((self.items,self.items))
    self.newboard = self.board
    self.d = 1
    self.turn = turn
    
  def populate(self):
    for i in range(len(self.board)): #rows 12
      for j in range(len(self.board[i])): #cols 6
        self.board[i][j] = random.randint(0,1)

    self.board = np.pad(self.board,(1,1))
    self.newboard = self.board

  def is_reproduction(self):
    for rowIndex in range(len(self.board)):
      for colIndex in range(len(self.board[rowIndex])):

        neighbors = self.board[rowIndex-self.d:rowIndex+1+self.d , colIndex-self.d:colIndex+1+self.d].flatten()

        counts = Counter(neighbors) #count 1 and 0
        if counts[1]==2 or counts[1]==3: #reproduce
          self.newboard[rowIndex][colIndex] = 1
        else: #die
          self.newboard[rowIndex][colIndex] = 0

  def display(self):
    rowLen = self.newboard.shape[0] #helper to remove the padding
    colLen = self.newboard.shape[1]
    print(("Round: {} \n {}").format(self.turn, self.newboard[1:rowLen-1,1:colLen-1]))

def main():
  turn = 0
  newboard = gameMatrix(6,1)
  newboard.populate() 

  while turn < NUMRUNS: #defines how often 
    turn += 1
    newboard.turn = turn
    newboard.display()
    newboard.is_reproduction()
   
main()

