from microbit import *

####################### --- Class --- ####################################

def blankFrame():
  return "00000:00000:00000:00000:00000"
    
class Animation:

  def __init__(self,FPS=12):
    self.FPS = FPS
    self.frameList = []
          
  def addFrame(self,*frames):
    for frame in frames:
      self.frameList.append(Image(frame))

  def addFrames(self,*frames):
    self.addFrame(*frames)

  def run(self):
    delay = 1000//self.FPS
    display.show(self.frameList, delay, clear=True)

  def loop(self):
    while True:
      self.run()

  def setFPS(self,FPS):
    self.FPS = FPS
    
###### --- Main Code --- ######    
  
movie = Animation()

movie.addFrames(
  "90000:"
  "09000:"
  "00900:"
  "00090:"
  "00009" ,
    
  "09000:"
  "90900:"
  "09090:"
  "00909:"
  "00090" ,
    
  "00900:"
  "00090:"
  "90009:"
  "09000:"
  "00900" ,
    
  "00090:"
  "00009:"
  "00000:"
  "90000:"
  "09000" ,
    
  "00009:"
  "00000:"
  "00000:"
  "00000:"
  "90000" )

movie.loop()
    
