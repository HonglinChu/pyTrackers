from cftracker import dsst
from cftracker.config import dsst_config
import numpy as np
import cv2


tracker =  dsst.DSST(dsst_config.DSSTConfig())# tracker instance
cap=cv2.VideoCapture(0)#or video
ret,frame=cap.read()
roi=cv2.selectROI(windowName="demo", img=frame, showCrosshair=False, fromCenter=False)
x,y,w,h=roi
tracker.init(frame,roi) # initialize tracker with GT bounding box
while True:
    ret,frame=cap.read()
    x1,y1,w1,h1 = tracker.update(frame) # update tracker and output estimated position
    x1=int(x1)
    y1=int(y1)
    w1=int(w1)
    h1=int(h1)
    cv2.rectangle(frame, (x1, y1), (x1+w1,y1+h1), (255, 0, 0), 2)
    cv2.imshow('demo', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Exit!")
        break