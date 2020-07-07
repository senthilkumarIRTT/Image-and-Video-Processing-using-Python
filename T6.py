##Import opencv and print width and height of an image
import cv2
img = cv2.imread('Bird5.jpg')
height,width = img.shape[0:2]
startRow =int(height*0.2)
endRow = int(height*0.8)
startCol = int(width*0.2)
endCol = int(width*0.8)
croppedImage = img[startRow:endRow, startCol:endCol]
cv2.imshow('Original Image',img)
cv2.imshow('Cropped Image',croppedImage)
cv2.waitKey(0)

##RESULT

