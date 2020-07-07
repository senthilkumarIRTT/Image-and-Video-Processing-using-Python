#Tutorial on video capture
#Colour video capture
#Get the frame size
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    #Capture fram-by-frame
    ret,  frame = cap.read()
    print('width of frame=')
    width = cap.get(3)
    print(width)
    print('height of frame=')
    height = cap.get(4)
    print(height)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
