#Tutorial on video capture
#Gray video capture
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    #Capture fram-by-frame
    ret,  frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('colour video',frame)
    cv2.imshow('gray video',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
