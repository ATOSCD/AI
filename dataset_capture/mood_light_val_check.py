import os

# 🔹 원천 이미지 폴더
image_folder = r"C:\Users\user\Downloads\037.Small_object_detection을_위한_이미지_데이터\01.데이터\2.Validation\1.원천데이터\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\1.원천데이터\TL_침실_방\bedrooom01"

# 🔹 라벨링 JSON 폴더
label_folder = r"C:\Users\user\Downloads\download (1)\037.Small_object_detection을_위한_이미지_데이터\01.데이터\2.Validation\2.라벨링데이터\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_침실_방\bedrooom01"

# 🔍 라벨 파일 이름(확장자 제거) 추출
label_basenames = {
    os.path.splitext(f)[0]
    for f in os.listdir(label_folder)
    if f.endswith('.json')
}

# 🗑 라벨링에 없는 이미지 삭제
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
