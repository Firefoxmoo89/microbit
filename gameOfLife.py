from microbit import *                      # Import entire microbit library
from time import sleep                      # Import sleep from time module

def matrixToImage(matrix):                  # Define function matrixToImage()
  string = ""                               #   Start a string
  for row in matrix:                        #   Iterate through rows of parameter matrix
    for column in row:                      #     Iterate through columns of each row
      string += str(column)                 #       Add each column to string
    string += ":"                           #     Space each row with a ":"
  return Image(string[:-1])                 #   Return string as Image(), cuts last ":" out

def alive(pixelx,pixely):                   # Define function alive()
    if oldmatrix[pixelx][pixely] != 0:      #   If the pixel in the matrix is lit:
      return True                           #     Return True
    return False                            #   Otherwise, return False

newmatrix = [[0,0,0,0,0],                   # Create an initial image-matrix
             [0,9,9,0,0],
             [0,9,9,0,0],
             [0,0,0,9,9],
             [0,0,0,9,9]]

start = matrixToImage(newmatrix)            # Convert initial matrix to Image called start
display.show(start)                         # Put start on the screen
sleep(2)                                    # Wait for 2 seconds

while True:                                 # Loop endlessly
  
  dead,live = 0,9                                     # Set dead to 0 and live to 9  
  oldmatrix = newmatrix                               # Set the old matrix to the value of the previously new matrix
  newmatrix = [[0,0,0,0,0],                           # Make the new matrix blank
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]
  
  for row in range(5):                                # Iterate 0-4 and call it row
    for column in range(5):                           #   Iterate 0-4 and call it column  
      surroundPop = 0                                 #     Start a count of surrounding population
      pixel = oldmatrix[row][column]                  #     Set pixel to the current row and column of old matrix
      friends = []                                    #     Initialize a list of the pixels surrounding pixels called friends
      for r in [-1,0,1]:                              #     Iterate through -1,0,1 and call it r (stands for row-alterted)
        for c in [-1,0,1]:                            #       Iterate through -1,0,1 and call it c (stands for column-altered)
          if (r != 0) or (c != 0):                    #       As long as it isn't 0,0 (the pixel they are currently on)
            friends.append([row+r,column+c])          #         Append the location of the friend pixel to friends list
      for x,y in friends:                             #     For each friend's x,y location
        if x != -1 and x!=5 and y!=-1 and y!=5:       #       If it doesn't go out of bounds
          if alive(x,y):                              #         If it's alive
            surroundPop += 1                          #           Add one to the total for surrounding population
      if surroundPop == 3:                            #     If the surrounding population is 3
        newmatrix[row][column] = live                 #       Set the current pixel to live
      elif surroundPop==2 and alive(row,column):      #     If the surrounding population is 2 and the current pixel is alive
        newmatrix[row][column] = live                 #       Set the current pixel to live
      else:                                           #     Otherwise
        newmatrix[row][column] = dead                 #       Set the current pixel to dead
        
  output = matrixToImage(newmatrix)                   # Convert the new matrix into an image and set it to output
  display.show(output)                                # Display the output image on the screen
  sleep(.5)                                           # Wait for .5 seconds
