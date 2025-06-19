import os

# 분할된 폴더 루트
base_split_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra_split"

splits = ['train', 'val', 'test']

for split in splits:
    image_dir = os.path.join(base_split_dir, split, 'images')
    label_dir = os.path.join(base_split_dir, split, 'labels')

    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    image_basenames = set(os.path.splitext(f)[0] for f in image_files)
    label_basenames = set(os.path.splitext(f)[0] for f in label_files)

    # 이미지에 라벨이 없는 경우
    img_no_label = image_basenames - label_basenames
    # 라벨에 이미지가 없는 경우
    label_no_img = label_basenames - image_basenames

    print(f"📂 {split.upper()} SET 검증 결과:")
    if img_no_label:
        print(f"⚠️ {len(img_no_label)}개의 이미지에 해당 라벨 없음: {sorted(img_no_label)[:5]}...")
    else:
        print("✅ 모든 이미지에 대응되는 라벨 있음.")

    if label_no_img:
        print(f"⚠️ {len(label_no_img)}개의 라벨에 해당 이미지 없음: {sorted(label_no_img)[:5]}...")
    else:
        print("✅ 모든 라벨에 대응되는 이미지 있음.")
    
    print()
