import os
import shutil
import random

def split_dataset(original_dataset_dir, split_ratio=0.8):
    # Class names (folder names inside original_dataset_dir)
    classes = ['yes', 'no']

    # Define train and test directories
    train_dir = os.path.join(original_dataset_dir, 'train')
    test_dir = os.path.join(original_dataset_dir, 'test')

    # Create train and test subdirectories for each class
    for folder in [train_dir, test_dir]:
        os.makedirs(folder, exist_ok=True)
        for cls in classes:
            os.makedirs(os.path.join(folder, cls), exist_ok=True)

    # Split the dataset
    for cls in classes:
        cls_folder = os.path.join(original_dataset_dir, cls)
        images = [img for img in os.listdir(cls_folder) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
        random.shuffle(images)

        split_idx = int(len(images) * split_ratio)
        train_images = images[:split_idx]
        test_images = images[split_idx:]

        for img in train_images:
            shutil.copy(os.path.join(cls_folder, img), os.path.join(train_dir, cls, img))

        for img in test_images:
            shutil.copy(os.path.join(cls_folder, img), os.path.join(test_dir, cls, img))

    print("✅ Dataset successfully split into train and test folders.")

# === RUN HERE ===
if __name__ == '__main__':
    # You can modify this path based on where your dataset is
    original_dataset_dir = 'artifacts/data_ingestion/brain_tumor_dataset'
    split_dataset(original_dataset_dir)
