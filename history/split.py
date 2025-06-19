import os
import random
import shutil

# 원본 경로
image_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra\image"
label_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra\label"

# 출력 경로 기본 루트
base_output = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra_split"

# 비율 설정
train_ratio, val_ratio, test_ratio = 7, 2, 1

# 모든 이미지 파일 리스트 (jpg만)
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

# 셔플
random.shuffle(image_files)

# 분할 인덱스 계산
total = len(image_files)
train_end = int(total * train_ratio / (train_ratio + val_ratio + test_ratio))
val_end = train_end + int(total * val_ratio / (train_ratio + val_ratio + test_ratio))

train_files = image_files[:train_end]
val_files = image_files[train_end:val_end]
test_files = image_files[val_end:]

splits = {
    "train": train_files,
    "val": val_files,
    "test": test_files
}

# 각 split에 대해 이미지/라벨 복사
for split_name, files in splits.items():
    img_out_dir = os.path.join(base_output, split_name, "images")
    lbl_out_dir = os.path.join(base_output, split_name, "labels")
    os.makedirs(img_out_dir, exist_ok=True)
    os.makedirs(lbl_out_dir, exist_ok=True)

    for img_file in files:
        label_file = os.path.splitext(img_file)[0] + ".txt"

        src_img = os.path.join(image_dir, img_file)
        src_lbl = os.path.join(label_dir, label_file)

        dst_img = os.path.join(img_out_dir, img_file)
        dst_lbl = os.path.join(lbl_out_dir, label_file)

        # 이미지 복사
        shutil.copy2(src_img, dst_img)

        # 라벨이 존재할 때만 복사
        if os.path.exists(src_lbl):
            shutil.copy2(src_lbl, dst_lbl)

print("✅ 7:2:1로 이미지와 라벨을 랜덤하게 분할하여 복사 완료했습니다.")
