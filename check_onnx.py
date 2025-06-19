import onnxruntime as ort
import numpy as np

# 1. ONNX 모델 경로
onnx_path = "best.onnx"

# 2. ONNX 모델 로드
session = ort.InferenceSession(onnx_path)

# 3. 입력 이름 및 shape 확인
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape
print(f"Input name: {input_name}, shape: {input_shape}")

# 4. 더미 입력 생성 (예: 160x160 RGB 이미지)
dummy_input = np.random.rand(1, 3, 160, 160).astype(np.float32)

# 5. 모델 추론 실행
outputs = session.run(None, {input_name: dummy_input})

# 6. 출력 텐서 shape 확인
output_shape = outputs[0].shape  # 예: (1, 18, 525)
print(f"Output shape: {output_shape}")

# 7. 클래스 수 추정: 18 - (4 bbox + 1 obj_conf) = 13
num_outputs = output_shape[1]
num_classes = num_outputs - 5
print(f"⚠️ Estimated number of classes in ONNX model: {num_classes}")
