import os

image_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra\image"
label_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra\label"

# 파일 이름 (확장자 제거한 base name) 수집
image_files = {os.path.splitext(f)[0]: f for f in os.listdir(image_dir) if f.endswith(".jpg")}
label_files = {os.path.splitext(f)[0]: f for f in os.listdir(label_dir) if f.endswith(".txt")}

# 이미지에만 있고 라벨에 없는 경우
only_in_images = set(image_files.keys()) - set(label_files.keys())
for base in only_in_images:
    file_path = os.path.join(image_dir, image_files[base])
    os.remove(file_path)
    print(f"🗑 Deleted image: {file_path}")

# 라벨에만 있고 이미지에 없는 경우
only_in_labels = set(label_files.keys()) - set(image_files.keys())
for base in only_in_labels:
    file_path = os.path.join(label_dir, label_files[base])
    os.remove(file_path)
    print(f"🗑 Deleted label: {file_path}")

print("✅ 이름이 일치하지 않는 파일 삭제 완료.")
