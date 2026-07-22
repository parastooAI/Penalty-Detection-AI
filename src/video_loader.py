import cv2
video_path= "data/videos/test.mp4"
cap=cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Erroe:cannot open video.")
    exit()
#information vidio
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

fps = cap.get(cv2.CAP_PROP_FPS)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

duration = frame_count / fps

print("========== Video Information ==========")

print(f"Total Frames : {frame_count}")

print(f"FPS          : {fps}")

print(f"Resolution   : {width} x {height}")

print(f"Duration     : {duration:.2f} seconds")

print("=======================================")


while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("football video",frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()   