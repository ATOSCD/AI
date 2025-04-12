import os
import json

# JSON 파일들이 저장된 폴더 경로
folder_path = r"C:\Users\user\Downloads\download (1)\037.Small_object_detection을_위한_이미지_데이터\01.데이터\2.Validation\2.라벨링데이터\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_침실_방\bedrooom01"

# 유지할 class_name
target_class = "무드등"

# 폴더 내의 모든 JSON 파일에 대해 검사
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 해당 파일 내 annotation이 target_class를 포함하는지 확인
            contains_target = False
            for ann in data.get("annotations", []):
                cat_id = ann.get("category_id")
                for category in data.get("categories", []):
                    if str(category.get("class_id")) == str(cat_id) and category.get("class_name") == target_class:
                        contains_target = True
                        break
                if contains_target:
                    break
            
            # 만약 target_class가 없으면 삭제
            if not contains_target:
                os.remove(file_path)
                print(f"삭제됨: {filename}")
            else:
                print(f"유지됨: {filename}")
        
        except Exception as e:
            print(f"오류 발생 ({filename}): {e}")
