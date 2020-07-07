import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MPJG')
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
     
    if ret==True:
        frame1 = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame1)
        cv2.imshow('original video',frame)
        cv2.imshow('flipped video',frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
