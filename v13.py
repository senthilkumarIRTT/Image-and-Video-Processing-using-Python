#Histogram Equalization of colour video
import numpy as np
import cv2

#Function for Histogram equalization
def equalizeHistColor(frame):
    # equalize the histogram of color image
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  # convert to HSV
    img[:,:,2] = cv2.equalizeHist(img[:,:,2])     # equalize the histogram of the V channel
    return cv2.cvtColor(img, cv2.COLOR_HSV2RGB)   # convert the HSV image back to RGB format
# start video capture
cap = cv2.VideoCapture('Blackbird.mp4')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()        
    # Our operations on the frame come here    
    #img = frame
    cv2.imshow('Original colour video',frame)
    img = equalizeHistColor(frame)
    # Display the resulting image
    cv2.imshow('Histogram Equalized colour video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
