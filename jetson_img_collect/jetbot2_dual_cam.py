import cv2
import os
import time

from camera import gstreamer_pipeline

free_count = 0
blocked_count = 0

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
cap2 = cv2.VideoCapture(gstreamer_pipeline(sensor_id = 1,flip_method=0), cv2.CAP_GSTREAMER)

while True:
    ret,image = cap.read()
    ret2,image2 = cap2.read()
    cv2.imshow('img',image)
    cv2.imshow('img2',image2)

    keyco = cv2.waitKey(1) & 0xFF
    if keyco == 27:
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()
