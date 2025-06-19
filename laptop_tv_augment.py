from PIL import Image
import numpy as np
import random
import os

# 이미지가 저장된 폴더 경로
input_folder = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop\image"
output_folder = os.path.join(input_folder, "processed")

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 폴더 내 모든 jpg 파일 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath).convert("RGB")
        arr = np.array(img)

        # 밝기 기반 마스크
        gray = np.dot(arr[..., :3], [0.299, 0.587, 0.114])
        mask = gray < 40

        # 마스크 영역에 무작위 색상 적용
        for y in range(arr.shape[0]):
            for x in range(arr.shape[1]):
                if mask[y, x]:
                    arr[y, x] = [random.randint(0, 255) for _ in range(3)]

        # 저장
        out_path = os.path.join(output_folder, filename)
        Image.fromarray(arr).save(out_path)

print("모든 이미지 처리 완료.")