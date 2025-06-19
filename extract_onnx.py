from ultralytics import YOLO

# best.pt 모델 로드
model = YOLO("best.pt")

# 클래스 수 명시 (버그 방지용)
model.model.nc = len(model.model.names)

# ONNX로 export
model.export(format="onnx", opset=12, imgsz=160)