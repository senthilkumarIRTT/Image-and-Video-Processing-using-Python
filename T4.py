##convert a colour image into a gray scale image
#vertical stack and horizontal stack of images
import cv2
import numpy as np
img = cv2.imread('Bird4.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
numpy_vertical = np.vstack((img,grey_3_channel))
numpy_horizontal = np.hstack((img,grey_3_channel))
cv2.imshow("original image",img)
cv2.imshow("gray image",grey)
cv2.imshow('Numpy Vertical',numpy_vertical)
cv2.imshow('Numpy Horizontal',numpy_horizontal)
cv2.waitKey()
cv2.destroyAllWindows()
##RESULT

