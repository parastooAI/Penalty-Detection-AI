import cv2
import os

video_path = "data/videos/test.mp4"
output_folder = "outputs/frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
  print("Error: Cannot open video")
  exit()

frame_number = 0

while True:
 ret, frame = cap.read()

 if not ret:
  break

 filename = os.path.join(
  output_folder,
  f"frame_{frame_number:04d}.jpg"
)

 success = cv2.imwrite(filename, frame)

 if success:
  frame_number += 1
 else:
  print("Failed saving:", filename)

cap.release()
print(f"{frame_number} frames saved successfully!")
