from ultralytics import YOLO

model = YOLO("best.pt")

# 마지막 출력 레이어 구조 확인
print(model.model.model[-1])