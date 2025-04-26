import os
import cv2
import numpy as np
import random
from glob import glob

# 경로 설정
image_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\images\train'
label_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\labels\train'

save_image_dir = image_dir + '_augmented'
save_label_dir = label_dir + '_augmented'

os.makedirs(save_image_dir, exist_ok=True)
os.makedirs(save_label_dir, exist_ok=True)

def load_labels(label_path):
    labels = []
    with open(label_path, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            cls = int(parts[0])
            x_center, y_center, w, h = map(float, parts[1:])
            labels.append([cls, x_center, y_center, w, h])
    return labels

def save_labels(label_path, labels):
    with open(label_path, 'w') as f:
        for label in labels:
            cls, x, y, w, h = label
            f.write(f"{cls} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

def apply_cutout(img, num_holes=1, hole_size=0.2):
    h, w = img.shape[:2]
    mask_value = (0, 0, 0)  # 검정색 마스크

    new_img = img.copy()
    for _ in range(num_holes):
        hole_h = int(h * hole_size)
        hole_w = int(w * hole_size)

        y = random.randint(0, h - hole_h)
        x = random.randint(0, w - hole_w)

        new_img[y:y+hole_h, x:x+hole_w] = mask_value
    return new_img

def rotate_image_and_labels(img, labels, angle):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, rot_matrix, (w, h), borderValue=(128,128,128))

    new_labels = []
    for cls, x, y, bw, bh in labels:
        abs_x = x * w
        abs_y = y * h
        coords = np.array([[abs_x, abs_y]])
        ones = np.ones(shape=(len(coords), 1))
        coords_ones = np.hstack([coords, ones])
        rotated_coords = rot_matrix.dot(coords_ones.T).T
        new_x = rotated_coords[0][0] / w
        new_y = rotated_coords[0][1] / h
        new_labels.append([cls, new_x, new_y, bw, bh])

    return rotated_img, new_labels

def process():
    image_paths = glob(os.path.join(image_dir, '*.jpg')) + glob(os.path.join(image_dir, '*.png'))
    total = len(image_paths)
    next_threshold = 0.1

    for idx, image_path in enumerate(image_paths):
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        label_path = os.path.join(label_dir, name + '.txt')

        img = cv2.imread(image_path)
        labels = load_labels(label_path)

        # 원본 저장
        cv2.imwrite(os.path.join(save_image_dir, name + '_orig' + ext), img)
        save_labels(os.path.join(save_label_dir, name + '_orig.txt'), labels)

        # Cutout 저장
        cutout_img = apply_cutout(img, num_holes=1, hole_size=0.2)
        cv2.imwrite(os.path.join(save_image_dir, name + '_cutout' + ext), cutout_img)
        save_labels(os.path.join(save_label_dir, name + '_cutout.txt'), labels)

        # Rotate 저장 (랜덤 각도)
        angle = random.uniform(-15, 15)  # 랜덤 각도
        rotated_img, rotated_labels = rotate_image_and_labels(img, labels, angle=angle)
        if rotated_labels:
            angle_str = str(int(angle)) if angle >= 0 else f"m{abs(int(angle))}"
            cv2.imwrite(os.path.join(save_image_dir, name + f'_rotate_{angle_str}' + ext), rotated_img)
            save_labels(os.path.join(save_label_dir, name + f'_rotate_{angle_str}.txt'), rotated_labels)

        # 진행 상황 출력
        if (idx + 1) / total >= next_threshold:
            print(f'[{int(next_threshold * 100)}%] Processing...')
            next_threshold += 0.1

if __name__ == '__main__':
    process()