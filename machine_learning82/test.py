from ultralytics import YOLO

# 학습된 best 모델 로드 (절대 경로 사용)
model = YOLO(r"C:\Users\user\Desktop\4-1\capAI\machine_learning82\runs\detect\yolov8n_custom2\weights\best.pt")

# test 이미지 폴더에서 예측 수행
results = model.predict(
    source=r"C:\Users\user\Desktop\4-1\capstone\dataset_final\images\test",  # ← 여기도 본인 경로 맞게
    save=True
)

# confidence 추출 및 출력
for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        print(f"Class: {cls_id}, Confidence: {conf:.4f}, BBox: {xyxy}")

from collections import defaultdict

class_counts = defaultdict(int)
class_conf_sums = defaultdict(float)

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        class_counts[cls_id] += 1
        class_conf_sums[cls_id] += conf

print("\n=== Detection Summary ===")
for cls_id in sorted(class_counts):
    count = class_counts[cls_id]
    avg_conf = class_conf_sums[cls_id] / count if count > 0 else 0
    print(f"Class {cls_id}: {count} detections, avg confidence: {avg_conf:.4f}")
