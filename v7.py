# Converting colour image frame into gray scale image
import cv2 
import numpy as np 
  
# Creating a VideoCapture object to read the video 
cap = cv2.VideoCapture('Bullfinch.mp4') 
  
  
# Loop untill the end of the video 
while (cap.isOpened()):
    
    # Capture frame-by-frame 
    ret, frame = cap.read() 
    
    # Display the resulting frame 
    cv2.imshow('colour video',frame) 
  
    # conversion of BGR to grayscale is necessary to apply this operation 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    cv2.imshow('gray video',gray)
    # adaptive thresholding to use different threshold  
    # values on different regions of the frame. 
    Thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, 
                                           cv2.THRESH_BINARY_INV,11,2) 
  
    cv2.imshow('Binary video', Thresh) 
    # define q as the exit button 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
  
# release the video capture object 
cap.release() 
# Closes all the windows currently opened. 
cv2.destroyAllWindows() 
