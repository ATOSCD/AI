import os

label_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\labels\val'

# 라벨 값이 0.0~1.0 사이가 아니면 자르기
def clip_bbox(val):
    return min(max(float(val), 0.0), 1.0)

# 전체 라벨 파일 순회
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):
        path = os.path.join(label_dir, filename)

        with open(path, 'r') as f:
            lines = f.readlines()

        fixed_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue  # 잘못된 라인은 무시

            cls_id, x, y, w, h = parts
            try:
                x = clip_bbox(x)
                y = clip_bbox(y)
                w = clip_bbox(w)
                h = clip_bbox(h)
                fixed_lines.append(f"{cls_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
            except ValueError:
                continue  # 숫자 변환 안 되면 건너뜀

        # 덮어쓰기
        with open(path, 'w') as f:
            f.writelines(fixed_lines)

print("✅ 모든 바운딩 박스를 0~1 범위로 보정 완료.")
