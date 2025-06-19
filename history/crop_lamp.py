import os
from PIL import Image
import shutil

# 입력 이미지/라벨 경로
image_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light\image"
label_dir = image_dir.replace("image", "label")

# 출력 경로
output_image_dir = image_dir + "_cropped"
output_label_dir = label_dir + "_cropped"
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 바운딩 박스가 가장자리와 겹치는지 확인하는 함수
def is_bbox_in_edge_area(bbox, img_width, img_height, margin=0.3):
    xc, yc, w, h = bbox
    xmin = (xc - w / 2) * img_width
    xmax = (xc + w / 2) * img_width
    ymin = (yc - h / 2) * img_height
    ymax = (yc + h / 2) * img_height

    x_margin = img_width * margin
    y_margin = img_height * margin

    if xmin < x_margin or xmax > (img_width - x_margin):
        return True
    if ymin < y_margin or ymax > (img_height - y_margin):
        return True
    return False

# 이미지 처리
for filename in os.listdir(image_dir):
    if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    image_path = os.path.join(image_dir, filename)
    label_path = os.path.join(label_dir, os.path.splitext(filename)[0] + ".txt")

    # 이미지 열기
    img = Image.open(image_path)
    w, h = img.size

    # 바운딩 박스 검사
    skip_crop = False
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            bbox = list(map(float, parts[1:]))
            if is_bbox_in_edge_area(bbox, w, h):
                skip_crop = True
                break

    if skip_crop:
        # 그대로 복사
        shutil.copy(image_path, os.path.join(output_image_dir, filename))
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_label_dir, os.path.basename(label_path)))
    else:
        # 중앙 40% ~ 70% 영역만 crop
        left = int(w * 0.3)
        upper = int(h * 0.3)
        right = int(w * 0.7)
        lower = int(h * 0.7)
        cropped = img.crop((left, upper, right, lower))
        cropped.save(os.path.join(output_image_dir, filename))
        # 라벨은 제거 (잘린 이미지엔 유효하지 않음)
