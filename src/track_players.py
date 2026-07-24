import cv2
from ultralytics import YOLO
from Color_detection import get_dominant_color
from player_manager import update_player
from ball_detector import closest_player_to_ball
players= {}

model = YOLO("models/yolov8n.pt")

video_path = "data/videos/test.mp4"

cap = cv2.VideoCapture(video_path)
ball_x=None
ball_y=None
while True:
 ret, frame = cap.read()

 if not ret:
  break

 results = model.track(frame, persist=True, tracker="botsort.yaml",verbose=False)
 boxes = results[0].boxes

 if boxes.id is not None:
  for box, track_id, cls in zip(boxes.xyxy, boxes.id,boxes.cls):
      x1,y1,x2,y2=map(int,box)
      class_id=int(cls)
      if class_id==32:
      #sport ball
         ball_x=int((x1+x2)/2)
         ball_y=int((y1+y2)/2)
         
         print("ball positions:", ball_x, ball_y)
         continue


  player_crop = frame[y1:y2, x1:x2]

  color = get_dominant_color(player_crop)
  center_x=(x1+x2)//2
  center_y=(y1+y2)//2
  players=update_player(
     int(track_id),
     color,
     center_x,
     center_y
   )
  
  if ball_x is not None and ball_y is not None:
     closest_id, distance=closest_player_to_ball(
         players,
         ball_x,
         ball_y 
     )
     print(
        "clsest player:",
        closest_id,
        "Distance",
        distance
     )
  for players_id, data in players.items():
      positions=data["positions"]

      for i in range(1,len(positions)):
         cv2.line(
            frame,
            positions[i-1],
            positions[i],
            (0,255,0),
            2
         )

   
 annotated_frame = results[0].plot()

 display_frame = cv2.resize(annotated_frame, (960, 540))

 cv2.imshow("Tracking", display_frame)

 if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()