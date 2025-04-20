import cv2
import numpy as np

img = cv2.imread("resources/output_images/saved_img.jpg")

# Define the width and height for the output perspective image
width, height = 350, 450

# Define the raw points (opening the image in Paint) of the selected image to get a perspective view (2D view)
pts = np.float32([[115, 96], [538, 97], [82, 426], [573, 425]])

# Define the frame size of the 2D view
bird_view_pts = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Get the transform matrix to get the perspective view of the image
transform_matrix = cv2.getPerspectiveTransform(pts, bird_view_pts)

# Get the final 2D perspective image of the original inclined image
perspective_img = cv2.warpPerspective(img, transform_matrix, (width, height))

# Highlight the selected points on the original image
for x in range(0, 4):
    cv2.circle(img, (int(pts[x][0]), int(pts[x][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original image with points", img)
cv2.imshow("2D perspective image", perspective_img)
cv2.waitKey(0)