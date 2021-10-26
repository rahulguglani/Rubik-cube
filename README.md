# Rubik-cube
it is a python project using opencv to get cube position and using kociemba algorithm to sove the cube.
## Dependencies
1. kociemba
2. opencv-python
3. pynput
4. time

## Description
It takes photos of cube faces and detect pieces by calibrating color from centre piece. then make color code and pass it to kociemba algorithm which solves the cube, and gives the steps to solve cube which is displayed with the help of opencv.

## how to use it
0. download images , graphics.py and kociembatry.py and place them in same folder. then run kociembatry.py after installing all dependencies
1. first of all it will ask you camera option if you want to use default camera enter 0 and left click on the screen, if you want to use external camera enter 1 and click on screen.
2. then it will show live feed from camera with a cube face marking over it . Now we have to  __alling cube faces in order__ :  
  i.Top(white)  
  ii.Left(orange)  
  iii.Front(green)  
  iv.Right(red)   
  v.Back(blue)  
  vi.Down(yellow)   
3. Right click anywhere to active camera, then when face is alinged right click again to capture that face, then aling other face in order then right click again and so on till all the 6 faces are captured. then finally right click one more time to exit the screen.
4. Then program will confirm whether detected color are right or wrong enter 1 in terminal if detected colors are right , if wrong enter 0 and then manually enter colorcode of that face.
5. After confirming all the faces the program will show the moves to solve the cube. 
