import os

frames_folder = "outputs/frames"

frames = os.listdir(frames_folder)

print("Total frames:", len(frames))

print("\nFirst 10 frames:")

for frame in frames[:10]:
 print(frame)