import os

# 🔄 폴더 경로를 제대로 반대로 넣자!
label_folder = r'C:\Users\user\Desktop\4-1\캡스톤\datset\tv\TL_image(단일)_tv'  # ← .json
image_folder = r'C:\Users\user\Desktop\4-1\캡스톤\datset\tv\TS_image(단일)_tv'  # ← .jpg

# 이미지 파일 이름들 (확장자 제거)
image_names = set()
for f in os.listdir(image_folder):
    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
        base = os.path.splitext(f)[0]  # IMG_1182732_tv(tv)
        image_names.add(base)

# 라벨 파일 이름에서 _(4_1) 제거
label_names = set()
for f in os.listdir(label_folder):
    if f.lower().endswith('.json'):
        base = os.path.splitext(f)[0]
        base = base.split('_(')[0]  # IMG_1182732_tv(tv)
        label_names.add(base)

# 이미지에는 있는데 라벨이 없는 파일
missing_labels = sorted(image_names - label_names)
print(f"🔍 라벨이 없는 이미지 파일들 ({len(missing_labels)}개):")
for name in missing_labels:
    print(name)

# 라벨은 있는데 이미지가 없는 파일
missing_images = sorted(label_names - image_names)
print(f"\n📂 이미지가 없는 라벨 파일들 ({len(missing_images)}개):")
for name in missing_images:
    print(name)
