import os
import random
import shutil

# 경로 설정
val_images_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\images\val'
val_labels_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\labels\val'
train_images_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\images\train'
train_labels_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\labels\train'

# val images 파일 리스트 가져오기 (확장자는 jpg 가정)
val_images = [f for f in os.listdir(val_images_dir) if f.endswith('.jpg')]

# 절반 랜덤 선택
num_to_move = len(val_images) // 2
files_to_move = random.sample(val_images, num_to_move)

for img_file in files_to_move:
    # 파일 이름에서 확장자 제거
    basename = os.path.splitext(img_file)[0]
    label_file = basename + '.txt'

    # 원본 경로
    src_img_path = os.path.join(val_images_dir, img_file)
    src_label_path = os.path.join(val_labels_dir, label_file)

    # 목적지 경로
    dst_img_path = os.path.join(train_images_dir, img_file)
    dst_label_path = os.path.join(train_labels_dir, label_file)

    # 파일 이동
    if os.path.exists(src_img_path) and os.path.exists(src_label_path):
        shutil.move(src_img_path, dst_img_path)
        shutil.move(src_label_path, dst_label_path)
    else:
        print(f"Warning: {img_file} or {label_file} not found.")

print(f"총 {num_to_move}개의 이미지와 라벨 파일을 옮겼습니다.")
