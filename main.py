import cv2

video = cv2.VideoCapture("video.mp4")

# returns a tuple of each frame, and whether it exists
success, frame = video.read()

# initiate file name system
count = 1

# loop over each frame in the video
while success:
  # save the frame
  cv2.imwrite(f'images/frame{count}.jpg', frame)
  # load a new frame
  success, frame = video.read()
  # increment file naming system
  count += 1
