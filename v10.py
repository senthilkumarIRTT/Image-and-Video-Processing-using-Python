#Resize a video and image interpolation
import cv2 
import numpy as np 
  
# Creating a VideoCapture object to read the video 
cap = cv2.VideoCapture('Blackbird.mp4') 
  
  
# Loop untill the end of the video 
while (cap.isOpened()): 
    # Capture frame-by-frame 
    ret, frame = cap.read()
    cv2.imshow('Video Original Size', frame) 
    frame = cv2.resize(frame,(320,240),fx = 0,fy = 0,interpolation =cv2.INTER_CUBIC) 
  
    # Display the resulting frame 
    cv2.imshow('Resized Video', frame) 
  
    # using cv2.Gaussianblur() method to blur the video 
  
    # (5, 5) is the kernel size for blurring. 
    gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0)  
    cv2.imshow('gblur', gaussianblur) 
  
    # define q as the exit button 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
  
# release the video capture object 
cap.release() 
  
# Closes all the windows currently opened. 
cv2.destroyAllWindows()
