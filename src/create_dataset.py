import os
import shutil

source_folder = "outputs/frames"
dataset_folder = "dataset/penalty"

os.makedirs(dataset_folder, exist_ok=True)

contact_frame = 180

start = contact_frame - 15
end = contact_frame + 15

for i in range(start, end + 1):
 filename = f"frame_{i:04d}.jpg"

 src = os.path.join(source_folder, filename)
 dst = os.path.join(dataset_folder, filename)

 if os.path.exists(src):
  shutil.copy(src, dst)
print("Dataset created successfully!")