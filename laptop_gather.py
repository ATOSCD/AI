import os
import random
import shutil

# 입력 경로 (laptop_extra)
image_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra\image"
label_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra\label\yolo_labels"

# 출력 경로
output_root = r"C:\Users\user\Desktop\4-1\capstone\dataset_final"
image_out = os.path.join(output_root, "images")
label_out = os.path.join(output_root, "labels")

# 출력 디렉토리 준비
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(image_out, split), exist_ok=True)
    os.makedirs(os.path.join(label_out, split), exist_ok=True)

# 이미지 및 유효 라벨 확인
all_images = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]
valid_images = []
skipped_images = []

for f in all_images:
    name = os.path.splitext(f)[0]
    txt_path = os.path.join(label_dir, name + ".txt")
    if os.path.exists(txt_path):
        valid_images.append(f)
    else:
        skipped_images.append(f)

# 셔플 후 분할
random.shuffle(valid_images)
total = len(valid_images)
n_train = int(total * 0.7)
n_val = int(total * 0.2)
n_test = total - n_train - n_val  # 남은 건 test로

train_files = valid_images[:n_train]
val_files = valid_images[n_train:n_train + n_val]
test_files = valid_images[n_train + n_val:]

# 복사 함수
def copy_split(files, split):
    for f in files:
        name = os.path.splitext(f)[0]
        img_src = os.path.join(image_dir, f)
        txt_src = os.path.join(label_dir, name + ".txt")
        img_dst = os.path.join(image_out, split, f)
        txt_dst = os.path.join(label_out, split, name + ".txt")

        shutil.copy(img_src, img_dst)
        shutil.copy(txt_src, txt_dst)

# 파일 복사
copy_split(train_files, "train")
copy_split(val_files, "val")
copy_split(test_files, "test")

# 요약 출력
print(f"\n✅ laptop_extra 클래스 분할 완료!")
print(f"   총 이미지:       {len(all_images)}")
print(f"   라벨 누락 제외:  {len(valid_images)} (누락 {len(skipped_images)})")
print(f"   → train: {len(train_files)} | val: {len(val_files)} | test: {len(test_files)}")

if skipped_images:
    print(f"   ⚠️ 누락된 이미지 파일 목록:")
    for skip in skipped_images:
        print(f"     - {skip}")
