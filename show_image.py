import cv2
img=cv2.imread('1.jpg', 1)
cv2.imshow('my-window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()