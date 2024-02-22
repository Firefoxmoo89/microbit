# Collection of micro bit projects
Projects made for the class MECH-1010 CE for the microbit device by BBC (https://microbit.org/). Descriptions of each are below.

## animateClass.py
This was designed as a learning project meant to teach beginner Python programmers what a class is. The format is very simple and originally came with an instruction sheet in which the requirements would be given to the student and instruction on "classes" and "objects" were given. A class is defined to create animation objects, where methods add frames to its frame list and other methods play the final product. 

## animateLocal.py
As opposed to the simple class structure of the previous project, which utilized animation frames programmed by the coder in the file itself, this is a program that allows a user to draw animation frames directly on the device. 
Closing the circuit on the pins enables them to be used as buttons. In this project, pin 2 moves the cursor right while pin 0 moves it left. Pin 1 draws, setting the pixel to the highest brightness and lowering it with further presses.
Button A sets the current frame into stone, adds it to the frame list, and resets the user on a new frame. Button B finishes the animating process and starts the playback.

## gameOfLife.py
This project is based on Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). A starting matrix is created with bright pixels, after which the system is run.
To evaluate the survival of the pixel, the coordinates of each surrounding pixel are calculated and add to a total of live vs dead. This game does not extend past the limits of the 5 x 5 screen, so there isn't much that can happen. 
