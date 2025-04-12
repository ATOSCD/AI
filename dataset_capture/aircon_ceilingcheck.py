import os

# 폴더 경로
label_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\airconditioner_ceiling\label"
image_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\airconditioner_ceiling\image"

# 라벨 파일 기준 이름들 추출 (_(4_1) 제거)
label_basenames = set()
for f in os.listdir(label_folder):
    if f.endswith('.json'):
        base = os.path.splitext(f)[0]
        clean_base = base.split("_(4_1)")[0]
        label_basenames.add(clean_base)

# 이미지 파일 중 label에 없는 것 삭제
deleted_count = 0
for f in os.listdir(image_folder):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        base = os.path.splitext(f)[0]
        if base not in label_basenames:
            file_path = os.path.join(image_folder, f)
            print(f"🗑 삭제: {f}")
            os.remove(file_path)
            deleted_count += 1

print(f"\n✅ 삭제 완료! 총 {deleted_count}개 이미지 삭제됨.")
