import os

# ✅ 경로 설정
image_dir = r"C:\Users\user\Desktop\4-1\캡스톤\dataset_extra\mug\image"
label_dir = r"C:\Users\user\Desktop\4-1\캡스톤\dataset_extra\mug\label"
yolo_label_subdir = os.path.join(label_dir, "yolo_labels")

# ✅ 현재 존재하는 이미지 파일 이름들 (.jpg → 이름만 추출)
image_filenames = {
    os.path.splitext(file)[0]
    for file in os.listdir(image_dir)
    if file.lower().endswith(".jpg")
}

# ✅ label 폴더 내 JSON 파일 중, 이미지에 없는 것 삭제
deleted_count = 0
for file in os.listdir(label_dir):
    if not file.endswith(".json"):
        continue

    json_name = os.path.splitext(file)[0]
    if json_name not in image_filenames:
        json_path = os.path.join(label_dir, file)
        try:
            os.remove(json_path)
            deleted_count += 1
            print(f"🗑️ 삭제됨: {file}")
        except Exception as e:
            print(f"⚠️ 삭제 실패: {file} → {e}")

print(f"\n✅ 완료: 총 {deleted_count}개의 JSON 라벨 파일 삭제됨 (이미지 없는 경우)")
