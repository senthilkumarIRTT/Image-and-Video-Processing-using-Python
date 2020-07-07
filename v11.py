#Edge Detection
import cv2 
import numpy as np 
  
# Creating a VideoCapture object to read the video 
cap = cv2.VideoCapture('Blackbird.mp4') 
  
  
# Loop untill the end of the video 
while (cap.isOpened()): 
    # Capture frame-by-frame 
    ret, frame = cap.read() 
  
    # Display the resulting frame 
    cv2.imshow('Original Colour video', frame) 
  
    # using cv2.Canny() for edge detection. 
    edge_detect = cv2.Canny(frame,100,200) 
    cv2.imshow('Edge detect',edge_detect) 
  
    # define q as the exit button 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
  
# release the video capture object 
cap.release() 
# Closes all the windows currently opened. 
cv2.destroyAllWindows() 
