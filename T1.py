##Import opencv and print its type. Also display image
import cv2
img = cv2.imread('Bird1.jpg')
print(type(img))
cv2.imshow('Original Image',img)
cv2.waitKey(0)

##RESULT
#<class 'numpy.ndarray'>
