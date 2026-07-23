import cv2
from Color_detection import get_dominant_color

image_path = "outputs/frames/frame_0190.jpg"

image = cv2.imread(image_path)

print("Image path:", image_path)
print("Image loaded:", image is not None)

if image is not None:
  color = get_dominant_color(image)
  print("Detected color:", color)
  