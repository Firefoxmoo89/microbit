from microbit import *
from time import ticks_ms

def holdup(daPin):
  while daPin.is_touched():
    print("",end="")

def waittime(starttime):
  return ticks_ms()-starttime

def matrixToImage(matrix):                  # Define function matrixToImage()
  string = ""                               #   Start a string
  for r in matrix:                        #   Iterate through rows of parameter matrix
    for c in r:                      #     Iterate through columns of each row
      string += str(c)                 #       Add each column to string
    string += ":"                           #     Space each row with a ":"
  return Image(string[:-1])                 #   Return string as Image(), cuts last ":" out

animating = True
sameFrame = True
allFrames = []
touching = True
blink = 2
blinking = False
first,last = 0,4
minn,maxx = 0,9
started = False
start = 0

while animating:

  currentFrame = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]
  sameFrame = True
  display.show(matrixToImage(currentFrame))
  row,column = first,first

  while sameFrame:

    if started:
      if waittime(start) > 700:
        blinking = True
      else:
        blinking = False
    else:
      blinking = False

    if blinking:
      if ticks_ms()//1000%2 == 0:
        blink = 7
      elif ticks_ms()//1000%2 == 1:
        blink = 2
      display.set_pixel(column,row,blink)
    else:
      display.set_pixel(column,row,currentFrame[row][column])
  
    if pin2.is_touched():
      holdup(pin2)
      started = False
      display.set_pixel(column,row,currentFrame[row][column])
      if column != last:
        column += 1
      else:
        if row != last:
          row += 1
          column = first
        else:
          row,column = first,first

    elif pin0.is_touched():
      holdup(pin0)
      started = False
      display.set_pixel(column,row,currentFrame[row][column])
      if column != first:
        column -= 1
      else:
        if row != first:
          row -= 1
          column = last
        else:
          row,column = last,last

    elif pin1.is_touched():
      holdup(pin1)
      started = False
      print(row,column)
      if currentFrame[row][column] != minn:
        currentFrame[row][column] -= 1
      else:
        currentFrame[row][column] = maxx

    elif button_a.was_pressed():
      started = False
      sameFrame = False
      print(currentFrame)
      allFrames.append(matrixToImage(currentFrame))

    elif button_b.was_pressed():
      animating = False
      sameFrame = False
      
    else:
      if not started:
        start = ticks_ms()
        started = True

while not button_b.was_pressed():
  display.show(allFrames)
        

  

      
    




  
