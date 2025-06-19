import os

def print_progress(current, total, label):
    percent = int((current / total) * 100)
    if percent % 10 == 0 and percent not in print_progress.seen:
        print(f"Progress ({label}): {percent}%")
        print_progress.seen.add(percent)
print_progress.seen = set()

base_path = r"C:\Users\user\Desktop\4-1\capstone\dataset_final"
subfolders = ["train", "val", "test"]

for subset in subfolders:
    print(f"\n=== Checking {subset} folder ===")
    
    label_dir = os.path.join(base_path, "labels", subset)
    image_dir = os.path.join(base_path, "images", subset)
    
    label_files_all = [f for f in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, f))]
    image_files_all = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    
    # 확장자 제외한 이름만 추출하면서 진행률 표시
    label_files = set()
    for i, f in enumerate(label_files_all):
        label_files.add(os.path.splitext(f)[0])
        print_progress(i + 1, len(label_files_all), f"labels/{subset}")

    print_progress.seen.clear()  # 리셋

    image_files = set()
    for i, f in enumerate(image_files_all):
        image_files.add(os.path.splitext(f)[0])
        print_progress(i + 1, len(image_files_all), f"images/{subset}")

    only_in_labels = label_files - image_files
    only_in_images = image_files - label_files
    
    if only_in_labels:
        print(f"\n🔹 Only in labels/{subset}:")
        for f in sorted(only_in_labels):
            print(f"  - {f}")
    else:
        print("✅ All label files have corresponding images.")

    if only_in_images:
        print(f"\n🔸 Only in images/{subset}:")
        for f in sorted(only_in_images):
            print(f"  - {f}")
    else:
        print("✅ All image files have corresponding labels.")
