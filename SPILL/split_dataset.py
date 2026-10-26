import os
import random
import shutil

# Folder where this Python file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Original folders
image_folder = os.path.join(BASE_DIR, "images")
label_folder = os.path.join(BASE_DIR, "labels")

# Check folders
print("Image folder:", image_folder)
print("Label folder:", label_folder)

if not os.path.exists(image_folder):
    print("ERROR: images folder not found!")
    exit()

if not os.path.exists(label_folder):
    print("ERROR: labels folder not found!")
    exit()

# Get images
images = [
    f for f in os.listdir(image_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

print("Images found:", len(images))

# Shuffle
random.seed(42)
random.shuffle(images)

# Calculate split
total = len(images)

train_count = int(total * 0.70)
val_count = int(total * 0.15)

train_images = images[:train_count]
val_images = images[train_count:train_count + val_count]
test_images = images[train_count + val_count:]

# Create folders
for folder in ["train", "val", "test"]:
    os.makedirs(os.path.join(image_folder, folder), exist_ok=True)
    os.makedirs(os.path.join(label_folder, folder), exist_ok=True)


# Copy image + matching label
def copy_files(file_list, folder):

    for image in file_list:

        image_path = os.path.join(image_folder, image)

        name = os.path.splitext(image)[0]
        label = name + ".txt"

        label_path = os.path.join(label_folder, label)

        shutil.copy2(
            image_path,
            os.path.join(image_folder, folder, image)
        )

        if os.path.exists(label_path):
            shutil.copy2(
                label_path,
                os.path.join(label_folder, folder, label)
            )
        else:
            print("WARNING: Label not found:", label)


copy_files(train_images, "train")
copy_files(val_images, "val")
copy_files(test_images, "test")

print()
print("================================")
print("Dataset split completed!")
print("================================")
print("Total images :", total)
print("Training     :", len(train_images))
print("Validation   :", len(val_images))
print("Testing      :", len(test_images))