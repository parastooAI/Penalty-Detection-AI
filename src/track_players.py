import cv2
from ultralytics import YOLO
from Color_detection import get_dominant_color

model = YOLO("models/yolov8n.pt")

video_path = "data/videos/test.mp4"

cap = cv2.VideoCapture(video_path)

while True:
 ret, frame = cap.read()

 if not ret:
  break

 results = model.track(frame, persist=True)
 boxes = results[0].boxes

 if boxes.id is not None:
  for box, track_id in zip(boxes.xyxy, boxes.id):

   x1, y1, x2, y2 = map(int, box)

   player_crop = frame[y1:y2, x1:x2]

   color = get_dominant_color(player_crop)

   print("ID:", int(track_id), "Color:", color)

 annotated_frame = results[0].plot()

 display_frame = cv2.resize(annotated_frame, (960, 540))

 cv2.imshow("Tracking", display_frame)

 if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()