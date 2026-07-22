from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

video_path = "data/videos/test.mp4"

cap = cv2.VideoCapture(video_path)

while True:
 ret, frame = cap.read()
 if not ret:
  break

 results = model(frame)

 annotated_frame = results[0].plot()

 display_frame = cv2.resize(annotated_frame, (960, 540))
 cv2.imshow("YOLO Detection", display_frame)
 key=cv2.waitKey(1)
 if cv2.waitKey(1) & 0xFF == ord("q"):
  break

cap.release()
cv2.destroyAllWindows()
