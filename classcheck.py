import os
import json

# 1. JSON 파일이 있는 폴더 경로
json_folder = r'C:\Users\user\Downloads\037.Small_object_detection을_위한_이미지_데이터\01.데이터\1.Training\2.라벨링데이터\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\1.Training\2.라벨링데이터\TL_주방_다이닝룸\dining_room01'

# 2. 머그컵 class_id
mugcup_class_id = 652

# 3. 삭제 대상이 아닌 파일을 먼저 수집
keep_files = set()

for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(json_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                for ann in data.get("annotations", []):
                    if ann.get("category_id") == mugcup_class_id:
                        keep_files.add(filename)
                        break  # 하나라도 있으면 보존
            except Exception as e:
                print(f"⚠️ {filename} 파싱 실패: {e}")

# 4. 삭제할 파일들을 찾아서 삭제
for filename in os.listdir(json_folder):
    if filename.endswith('.json') and filename not in keep_files:
        file_path = os.path.join(json_folder, filename)
        print(f"🗑 삭제: {filename}")
        os.remove(file_path)  # ← 실제 삭제! 테스트 시엔 주석 처리해도 됨
