##convert a colour image into a gray scale image
import cv2
img = cv2.imread('Bird3.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("original image",img)
cv2.imshow("gray image",grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
##RESULT

