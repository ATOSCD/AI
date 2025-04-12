import os

# 폴더 경로
label_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\chair\label"
image_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\chair\image"

# 이미지 파일 기준 이름들 추출
image_basenames = set()
for f in os.listdir(image_folder):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        base = os.path.splitext(f)[0]
        image_basenames.add(base)

# 라벨 파일 중 이미지에 없는 것 삭제
deleted_count = 0
for f in os.listdir(label_folder):
    if f.endswith('.json'):
        base = os.path.splitext(f)[0]
        clean_base = base.split("_(4_1)")[0]
        if clean_base not in image_basenames:
            file_path = os.path.join(label_folder, f)
            print(f"🗑 삭제: {f}")
            os.remove(file_path)
            deleted_count += 1

print(f"\n✅ 삭제 완료! 총 {deleted_count}개 라벨 파일 삭제됨.")
