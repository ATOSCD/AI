import os
import random
import shutil

# 현재 이미지와 라벨 경로
images_dir = r'C:\Users\user\Desktop\4-1\capstone\images'
labels_dir = r'C:\Users\user\Desktop\4-1\capstone\labels'

# 최종 저장 경로
base_output_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final'

# train/val/test 폴더 만들기
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(base_output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(base_output_dir, 'labels', split), exist_ok=True)

# 모든 이미지 파일 가져오기 (jpg만)
all_images = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

# 2000개 랜덤 샘플링
selected_images = random.sample(all_images, 2000)

# 8:1:1 비율 나누기
num_train = int(0.8 * 2000)  # 1600
num_val = int(0.1 * 2000)    # 200
num_test = 2000 - num_train - num_val  # 200

train_images = selected_images[:num_train]
val_images = selected_images[num_train:num_train+num_val]
test_images = selected_images[num_train+num_val:]

# 파일 복사 함수
def copy_files(image_list, split):
    for img_file in image_list:
        base_name = os.path.splitext(img_file)[0]
        label_file = base_name + '.txt'

        src_img_path = os.path.join(images_dir, img_file)
        src_label_path = os.path.join(labels_dir, label_file)

        dst_img_path = os.path.join(base_output_dir, 'images', split, img_file)
        dst_label_path = os.path.join(base_output_dir, 'labels', split, label_file)

        if os.path.exists(src_img_path) and os.path.exists(src_label_path):
            shutil.copy(src_img_path, dst_img_path)
            shutil.copy(src_label_path, dst_label_path)
        else:
            print(f"Warning: {img_file} 또는 {label_file} 파일이 없습니다.")

# 각각 복사
copy_files(train_images, 'train')
copy_files(val_images, 'val')
copy_files(test_images, 'test')

print("2000개 파일을 8:1:1로 분배 완료했습니다.")
