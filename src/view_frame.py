import cv2

image_path = "outputs/frames/frame_0190.jpg"

image = cv2.imread(image_path)

cv2.imshow("Frame", image)

cv2.waitKey(0)

cv2.destroyAllWindows()