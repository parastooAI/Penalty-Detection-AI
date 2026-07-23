import cv2
import numpy as np


def get_dominant_color(image):
 hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

 pixels = hsv.reshape(-1, 3)

 mean_color = np.mean(pixels, axis=0)

 h = mean_color[0]
 s = mean_color[1]
 v = mean_color[2]

#Red team
 if h < 10 or h > 170:
  return "red"

#Blue detiails on white jersey
 elif 90< h < 130 and s>50:
  return "blue_white"

# Yellow referre uniform
 elif 20<h< 40 and s>80:
  return "yellow"

 else:
  return "unknown"