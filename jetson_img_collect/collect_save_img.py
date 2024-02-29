import cv2
import os
import time
import insert_db
from image import bgr8_to_jpeg
# from pynput.keyboard import Controller,Key

blocked_dir = 'dataset/blocked'
free_dir = 'dataset/free'

try:
    os.makedirs(free_dir)
    os.makedirs(blocked_dir)
except FileExistsError:
    print('Directories not created becasue they already exist')


no_dir = '/home/ddrawa/te/camera_data_collect/dataset/blocked'
go_dir = '/home/ddrawa/te/camera_data_collect/dataset/free'
 
no_list = os.listdir(no_dir)
go_list = os.listdir(go_dir)

free_count = 0
blocked_count = 0


def save_snapshot(directory,count,image,go):
    image_path = os.path.join(directory, str(count) + '.jpg')
    image = bgr8_to_jpeg(image)
    with open(image_path, 'wb') as f:
        f.write(image)
    no_list = os.listdir(no_dir)
    go_list = os.listdir(go_dir)
    if go == True:
        img_name = go_dir + '/' + go_list[-1]
    else :
        img_name = no_dir + '/' + no_list[-1]
    
    insert_db.insertBLOB(None, img_name,go)
    
def save_free(image):
    global free_dir, free_count
    free_count = len(os.listdir(free_dir))
    save_snapshot(free_dir,free_count,image,go=True)
    
def save_blocked(image):
    global blocked_dir, blocked_count
    blocked_count = len(os.listdir(blocked_dir))
    save_snapshot(blocked_dir,blocked_count,image,go=False)

def step_forward():
    # robot.forward(0.8)
    robot.set_motors(0.7245,0.8)
    time.sleep(0.5)
    robot.stop()

def step_backward():
    # robot.backward(0.8)
    robot.set_motors(-0.7245,-0.8)
    time.sleep(0.5)
    robot.stop()

def step_left():
    # robot.left(0.74)
    robot.set_motors(-0.7245,0.8)
    time.sleep(0.657)
    robot.stop()

def step_right():
    # robot.right(0.74)
    robot.set_motors(0.7245,-0.8)
    time.sleep(0.71)
    robot.stop()

def step_stop():
    robot.stop()

camera = Camera.instance(capture_width=224, capture_height=224)

robot = Robot()

while True:
    image = camera.value
    cv2.imshow('img',image)

    keyco = cv2.waitKey(1) & 0xFF
    # print(keycode)
    if keyco == 27:
        break

    elif keyco == 70:  ## f
        print('f')
        save_free(image)
        
    elif keyco == 66:  ## b
        print('b')
        save_blocked(image)

    elif keyco == 82:
        print('forward')
        step_forward()

    elif keyco == 84:
        print('back')
        step_backward()

    elif keyco == 81:
        print('left')
        step_left()

    elif keyco == 83:
        print('right')
        step_right()

    elif keyco == 32:
        print('stop')
        step_stop()

camera.stop()
