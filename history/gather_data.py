import os
import random
import shutil

# 입력 및 출력 경로 설정
dataset_extra_root = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra"
output_root = r"C:\Users\user\Desktop\4-1\capstone\dataset_final"
image_out = os.path.join(output_root, "images")
label_out = os.path.join(output_root, "labels")

# 출력 디렉토리 생성
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(image_out, split), exist_ok=True)
    os.makedirs(os.path.join(label_out, split), exist_ok=True)

# 전체 통계 저장용
total_summary = {
    "total_copied": 0,
    "total_skipped": 0,
    "train": 0,
    "val": 0,
    "test": 0
}

# 클래스별 처리
for class_folder in os.listdir(dataset_extra_root):
    class_path = os.path.join(dataset_extra_root, class_folder)
    image_dir = os.path.join(class_path, "image")
    label_dir = os.path.join(class_path, "label", "yolo_labels")

    if not os.path.isdir(image_dir) or not os.path.isdir(label_dir):
        print(f"⚠️ 폴더 없음 → 건너뜀: {class_folder}")
        continue

    all_images = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]
    valid_images = []
    skipped_images = []

    for f in all_images:
        txt_path = os.path.join(label_dir, os.path.splitext(f)[0] + ".txt")
        if os.path.exists(txt_path):
            valid_images.append(f)
        else:
            skipped_images.append(f)

    random.shuffle(valid_images)

    total = len(valid_images)
    n_train = int(total * 0.7)
    n_val = int(total * 0.2)
    n_test = int(total * 0.1)
    remainder = total - (n_train + n_val + n_test)
    n_train += remainder  # 남는 건 train에 포함

    train_files = valid_images[:n_train]
    val_files = valid_images[n_train:n_train + n_val]
    test_files = valid_images[n_train + n_val:]

    def copy_split(files, split):
        for f in files:
            name = os.path.splitext(f)[0]
            img_src = os.path.join(image_dir, f)
            txt_src = os.path.join(label_dir, name + ".txt")
            img_dst = os.path.join(image_out, split, f)
            txt_dst = os.path.join(label_out, split, name + ".txt")

            shutil.copy(img_src, img_dst)
            shutil.copy(txt_src, txt_dst)

    copy_split(train_files, "train")
    copy_split(val_files, "val")
    copy_split(test_files, "test")

    print(f"\n✅ {class_folder}")
    print(f"   총 이미지:       {len(all_images)}")
    print(f"   라벨 누락 제외:  {len(valid_images)} (누락 {len(skipped_images)})")
    print(f"   → train: {len(train_files)} | val: {len(val_files)} | test: {len(test_files)}")

    if skipped_images:
        print(f"   ⚠️ 누락된 이미지 파일 목록:")
        for skip in skipped_images:
            print(f"     - {skip}")

    total_summary["total_copied"] += len(valid_images)
    total_summary["total_skipped"] += len(skipped_images)
    total_summary["train"] += len(train_files)
    total_summary["val"] += len(val_files)
    total_summary["test"] += len(test_files)

# 전체 결과 요약
print("\n🎉 전체 클래스 분할 완료!")
print(f"📦 전체 복사된 이미지/라벨: {total_summary['total_copied']}개")
print(f"🚫 전체 라벨 누락 이미지:   {total_summary['total_skipped']}개")
print(f"🔹 총 분할 결과 → train: {total_summary['train']}, val: {total_summary['val']}, test: {total_summary['test']}")
