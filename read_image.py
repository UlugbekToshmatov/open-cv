import cv2
import os


# Read image from disk
img = cv2.imread("resources/book_with_text_on_desk.jpg")

# Resize the image size to the desired one
frame_width = 640
frame_height = 580
img = cv2.resize(img, (frame_width, frame_height))

# Set the path where you want to save the image
save_dir = 'resources/output_images'
filename = 'saved_img.jpg'

# Create directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Full path to save image
save_path = os.path.join(save_dir, filename)

# Save image
cv2.imwrite(save_path, img)

# Show the resized image
cv2.imshow("Resized image", img)
cv2.waitKey(0)