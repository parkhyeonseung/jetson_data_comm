import cv2
import os
import time
import insert_db
from camera import gstreamer_pipeline
from motor import Robot
# from pynput.keyboard import Controller,Key


free_count = 0
blocked_count = 0
    
robot = Robot()

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)


while True:
    ret,image = cap.read()
    cv2.imshow('img',image)

    keyco = cv2.waitKey(1) & 0xFF
    # print(keycode)
    if keyco == 27:
        break

    elif keyco == 70:  ## f
        print('f')
        insert_db.insertBLOB(None, image,go=1)
        free_count+=1
        
    elif keyco == 90:  ## left
        print('z')
        insert_db.insertBLOB(None, image,go=2)
        blocked_count+=1

    elif keyco == 88:  ## right
        print('x')
        insert_db.insertBLOB(None, image,go=3)
        blocked_count+=1

    elif keyco == 82:
        print('forward')
        # robot.stop()
        robot.forward(0.7)

    elif keyco == 84:
        print('back')
        # robot.stop()
        robot.backward(0.7)

    elif keyco == 81:
        print('left')
        # robot.stop()
        robot.left(0.7)

    elif keyco == 83:
        print('right')
        # robot.stop()
        robot.right(0.7)

    elif keyco == 32:
        print('stop')
        robot.stop()
        
robot.init()
cap.release()
cv2.destroyAllWindows()