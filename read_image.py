import cv2


img = cv2.imread("resources/map.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)  # set 0 to wait for infinitely