import os
import shutil
source_folder = 'source_images'
destination_folder = 'jpg_images'

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All .jpg files moved successfully.")
