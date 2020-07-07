#video image transformation
import numpy as np
import math
import cv2

def WarpImage(frame):
    ax,bx=10.0,100
    ay,by=20.0,120
    img=np.zeros(frame.shape,dtype=frame.dtype)
    rows,cols=img.shape[:2]
    
    for i in range(rows):
        for j in range(cols):
            offset_x=int(ax*math.sin(2*math.pi*i/bx))
            offset_y=int(ay*math.cos(2*math.pi*j/by))
            if i+offset_y<rows and j+offset_x<cols:
                img[i,j]=frame[(i+offset_y)%rows,(j+offset_x)%cols]
            else:
                img[i,j]=0
    return img
# start video capture
cap = cv2.VideoCapture('Blackbird.mp4')
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('Original video',frame)
    # Our operations on the frame come here 
    img = WarpImage(frame)
         
    # Display the resulting image
    cv2.imshow('Video Transformation',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
