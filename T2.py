##Import opencv and print width and height of an image
import cv2
img = cv2.imread('Bird2.jpg')
print(type(img))
print(img.shape[0:2])
cv2.imshow('Original Image',img)
cv2.waitKey(0)

##RESULT
#(183, 275)
