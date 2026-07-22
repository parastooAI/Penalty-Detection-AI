from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

image_path = "outputs/frames/frame_0180.jpg"

image = cv2.imread(image_path)

results = model(image)
for r in results:
  for box in r.boxes:
   cls = int(box.cls[0])
   conf = float(box.conf[0])

   name = model.names[cls]

   print(name, conf)


annotated = results[0].plot()

cv2.imshow("Detection Result", annotated)

cv2.waitKey(0)
cv2.destroyAllWindows()