import os

# 폴더 경로
image_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\mood_light\image"
label_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\mood_light\label"

# 이미지 파일 이름 세트 (확장자 제거)
image_basenames = {
    os.path.splitext(f)[0]
    for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
}

# 라벨 파일 이름 세트 (확장자 제거)
label_basenames = {
    os.path.splitext(f)[0]
    for f in os.listdir(label_folder)
    if f.lower().endswith('.json')
}

# 공통으로 존재하는 이름만 남기고, 나머지는 제거 대상
common = image_basenames & label_basenames
only_in_images = image_basenames - common
only_in_labels = label_basenames - common

# 이미지 삭제
for name in only_in_images:
    for ext in ('.jpg', '.jpeg', '.png'):
        file_path = os.path.join(image_folder, name + ext)
        if os.path.exists(file_path):
            print(f"🗑 이미지 삭제: {file_path}")
            os.remove(file_path)

# 라벨 삭제
for name in only_in_labels:
    file_path = os.path.join(label_folder, name + '.json')
    if os.path.exists(file_path):
        print(f"🗑 라벨 삭제: {file_path}")
        os.remove(file_path)

print(f"\n✅ 삭제 완료! 이미지와 라벨이 모두 있는 쌍만 유지됨.")
