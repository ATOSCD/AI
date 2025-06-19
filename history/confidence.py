from ultralytics import YOLO
import os

# 모델 로드
model = YOLO('C:/Users/user/Desktop/4-1/capAI/machine_learning82/runs/detect/train2/weights/best.pt')

# 감지 실행
results = model.predict(
    source='C:/Users/user/Desktop/4-1/capstone/dataset_final/images/test',
    save=True,
    save_txt=True,
    project='runs/detect',
    name='predict_test_v2',  # 원하는 폴더 이름
    exist_ok=False           # 기존 폴더 덮어쓰기 방지
)

# 감지 결과에서 confidence 추출 및 평균 계산
class_confidence = {}  # 클래스별 confidence 리스트

for result in results:
    boxes = result.boxes
    for box in boxes:
        cls = int(box.cls[0].item())
        conf = box.conf[0].item()
        class_confidence.setdefault(cls, []).append(conf)

# 콘솔에 클래스별 평균 confidence 출력
print("\n=== 클래스별 평균 Confidence ===")
for cls, confs in class_confidence.items():
    avg_conf = sum(confs) / len(confs)
    print(f"Class {cls}: 평균 confidence = {avg_conf:.4f}")

if not class_confidence:
    print("⚠️ 감지된 객체가 없습니다.")
