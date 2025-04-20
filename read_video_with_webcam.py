import cv2


frame_width = 640
frame_height = 480

# vid = cv2.VideoCapture("resources/nature.mp4")        # read video from resource
vid = cv2.VideoCapture(0)                             # read video from webcam

while True:
    success, frame = vid.read()

    if not success:
        print("Failed to grab frame")
        break

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)               # sets colour for videos both from resource and webcam
    # frame = cv2.resize(frame, (frame_width, frame_height))        # resizes video from resource only*
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # waits for user to enter 'q' to exit video streaming
        break
