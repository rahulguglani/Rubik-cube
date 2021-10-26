import cv2
from graphics import *
from pynput import mouse
from pynput.mouse import Button
import time

face = -1


################################# define values ########################################

#color contains upper and lower values of colors in bgr format
#and stored as white,orange,green,red,blue,yellow
color = [[],[],[],[],[],[]]
color[0].append([150,255],[150,255],[150,255]) #white [b lower , b upper] , [g lower, g upper], [r lower, r upper]
color[1].append([80,120],[150,255],[150,255])
color[2].append([150,255],[150,255],[150,255])
color[3].append([150,255],[150,255],[150,255])
color[4].append([150,255],[150,255],[150,255])
color[5].append([150,255],[150,255],[150,255])

##########################################################################################



def calculateColor(c):
    if c[0]>150 and c[1]>150 and c[2]>150 :
        return 'W'
    return 'N'


def findColors(facee,name):
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b1=temp
    print(b1)
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b2=temp
    print(b2)
    temp =[0,0,0]
    cnt =0
    for i in range(115,198):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b3=temp
    print(b3)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b4=temp
    print(b4)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b5=temp
    print(b5)
    temp =[0,0,0]
    cnt =0
    for i in range(198,282):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b6=temp
    print(b6)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(195,278):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b7=temp
    print(b7)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(278,362):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b8=temp
    print(b8)
    temp =[0,0,0]
    cnt =0
    for i in range(282,365):
        for j in range(362,445):
            temp+=facee[i][j]
            cnt+=1
    temp=temp/cnt
    b9=temp
    print(b9)
    cv2.imshow(name,facee)
    cv2.waitKey(1500)
    ColorCode = calculateColor(b1)+calculateColor(b2)+calculateColor(b3)+calculateColor(b4)+calculateColor(b5)+calculateColor(b6)+calculateColor(b7)+calculateColor(b8)+calculateColor(b9)
    print(ColorCode)
    if int(input("is it correct"))==0:
        ColorCode = input("enter color code manually")
    

        






def getcnt():
    return face

def setcnt(a):
    global face
    face =a

def on_move(x, y):
    # print ("Mouse moved")
    pass

def on_click(x, y, button, pressed):
    cnt = getcnt()
    if cnt ==-1 and button== Button.right:
        cnt=0
    elif cnt == 0 and button==Button.right:
        cnt =1
    elif cnt == 1 and button==Button.right:
        cnt =2
    elif cnt == 2 and  button==Button.right:
        cnt =3
    elif cnt == 3 and  button==Button.right:
        cnt =4
    elif cnt == 4 and  button==Button.right:
        cnt =5
    elif cnt == 5 and  button==Button.right:
        cnt =6
    elif cnt == 6 and  button==Button.right:
        cnt =7
    else:
        pass
    if button==Button.right:
        print(cnt)
    setcnt(cnt)
    time.sleep(1)

def on_scroll(x, y, dx, dy):
    pass
    # print ("Mouse scrolled")

def getcamera():
    win = GraphWin("Select Camera",500,250)
    win.setBackground(color_rgb(255,255,255))
    info = Text(Point(250,20),"press 0 for laptop camera")
    info1 = Text(Point(250, 80), "press 1 for usb or wifi connected camera")
    info2 = Text(Point(250, 140), "or enter ip address of camera manually")
    info.draw(win)
    info1.draw(win)
    info2.draw(win)

    responseBox = Entry(Point(250,200),25)
    responseBox.draw(win)

    win.getMouse()
    response = responseBox.getText()
    win.close()

    if(response=='0' or response=='1'):
        return int(response)
    return response



listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()


cap = cv2.VideoCapture(getcamera())
cnt =0
front,up,down,left,right,back = None,None,None,None,None,None
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    cv2.line(frame,(195,115),(445,115),(0))
    cv2.line(frame,(195,115),(195,365),(0))
    cv2.line(frame,(445,115),(445,365),(0))
    cv2.line(frame,(195,365),(445,365),(0))
    cv2.line(frame,(278,115),(278,365),(0))
    cv2.line(frame,(362,115),(362,365),(0))
    cv2.line(frame,(195,198),(445,198),(0))
    cv2.line(frame,(195,282),(445,282),(0))

    
    if(face == 0):
        cv2.putText(frame,"click , when focused on front face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    if( face ==1 ):
        if cnt ==0:
            front = frame
            findColors(front,"front")
            cnt =1
        cv2.putText(frame,"click , when focused on up face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    elif face ==2:
        if cnt ==1:
            up = frame
            findColors(up,"up")
            cnt =2
        cv2.putText(frame,"click , when focused on down face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    elif face == 3:
        if cnt == 2:
            down = frame
            findColors(down,"down")
            cnt =3
        cv2.putText(frame,"click , when focused on left face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    elif face ==4:
        if cnt ==3:
            left = frame
            findColors(left,"left")
            cnt =4
        cv2.putText(frame,"click , when focused on right face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    elif face ==5:
        if cnt ==4:
            right = frame
            findColors(right,"right")
            cnt =5
        cv2.putText(frame,"click , when focused on back face",(10,10),cv2.FONT_HERSHEY_PLAIN,1,(0))
    elif cnt ==5 and face ==6:
        cnt =6
        back= frame
        findColors(back,"back")
    
    if face == 7:
        break

    cv2.imshow('live',frame)
    cv2.waitKey(1)
    # frame=cv2.flip(frame,1)
listener.stop()


cv2.imshow('front',front)

cv2.imshow('up',up)
cv2.imshow('down',down)
cv2.imshow('left',left)
cv2.imshow('right',right)
cv2.imshow('back',back)

# colorCode = findColors(up)+findColors(right)+findColors(front)+findColors(down)+findColors(left)+findColors(back)


cv2.waitKey(0)

