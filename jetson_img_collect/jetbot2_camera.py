import cv2
import os
import time

from camera import gstreamer_pipeline

free_count = 0
blocked_count = 0

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

while True:
    ret,image = cap.read()
    cv2.imshow('img',image)

    keyco = cv2.waitKey(1) & 0xFF
    if keyco == 27:
        break

cap.release()
cv2.destroyAllWindows()
