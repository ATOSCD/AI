import os

# 경로 설정
label_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\tissue\label"
image_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\tissue\image"

# 각 폴더의 파일 목록을 base 이름으로 저장 (확장자 제외)
label_basenames = set(os.path.splitext(f)[0] for f in os.listdir(label_folder) if f.endswith('.json'))
image_basenames = set(os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.endswith('.jpg'))

# 레이블 파일 중 이미지가 없는 것 삭제
for base in label_basenames - image_basenames:
    json_path = os.path.join(label_folder, base + ".json")
    if os.path.exists(json_path):
        os.remove(json_path)
        print(f"레이블 삭제됨: {json_path}")

# 이미지 파일 중 레이블이 없는 것 삭제
for base in image_basenames - label_basenames:
    img_path = os.path.join(image_folder, base + ".jpg")
    if os.path.exists(img_path):
        os.remove(img_path)
        print(f"이미지 삭제됨: {img_path}")
