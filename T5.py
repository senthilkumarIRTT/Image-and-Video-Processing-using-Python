##Import opencv and rotate an image
import cv2
img = cv2.imread('Bird3.jpg')
height,width =img.shape[0:2]
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2),270,1)
rotatedImage = cv2.warpAffine(img,rotationMatrix,(width, height))
####
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2),360,1)
originalImage = cv2.warpAffine(img,rotationMatrix,(width, height))
print(type(originalImage))
####
cv2.imshow("original image",originalImage)
cv2.imshow("rotated image",rotatedImage)
cv2.waitKey(0)

##RESULT

