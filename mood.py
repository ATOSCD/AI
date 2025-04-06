import os
import json

# 라벨 폴더 경로
label_folder = r"C:\Users\user\Downloads\037.Small_object_detection을_위한_이미지_데이터\01.데이터\1.Training\2.라벨링데이터\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\1.Training\2.라벨링데이터\TL_침실_방\bedrooom01"

# 무드등의 category_id
MOOD_LIGHT_ID = 696

# 삭제된 수 세기
deleted_count = 0

# 라벨 폴더 순회
for filename in os.listdir(label_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(label_folder, filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # annotations 중 무드등(category_id = 696)이 하나라도 있는지 확인
            has_moodlight = any(ann.get("category_id") == MOOD_LIGHT_ID for ann in data.get("annotations", []))

            if not has_moodlight:
                print(f"🗑 무드등 없음 → 삭제: {filename}")
                os.remove(file_path)
                deleted_count += 1

        except Exception as e:
            print(f"⚠️ 오류 발생: {filename} → {e}")

print(f"\n✅ 완료: 총 {deleted_count}개 라벨 파일 삭제됨 (무드등 annotation 없는 파일)")
