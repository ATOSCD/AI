# 🧠 AI Object Detection Project

이 저장소는 **데이터 전처리 초기 단계**, **중간 처리 과정**, **시행착오** 등을 포함한 **우리의 개발 히스토리**를 담고 있습니다.  
그로 인해 **파일 구조가 다소 지저분**해 보일 수 있습니다.  
training은 [**Ultralytics 리포지토리(v8,v11)**](https://github.com/ultralytics/ultralytics), [**Ultralytics 리포지토리(v5)**](https://github.com/ultralytics/yolov5.git)를 **클론 후 명령어로 사용**했기 때문에 파일 구조가 매우 복잡하여 해당 파일들은 포함되어 있지 않습니다.

---

## 🧠 모델 개발 이력

- **사용 모델**:  
  YOLO v5n (Ultralytics),  
  YOLO v8n / v8s / v8m (Ultralytics),  
  YOLO v11n (Ultralytics)

- **입력 크기**:  
  640×640 (기본값 버전 및 `--rect` 패딩 적용 버전)

- **학습 및 파인튜닝 전략**:  
  준비한 데이터셋으로 직접 학습하고, 학습된 `.pt` 파일을 기반으로 파인튜닝을 수행함

- **커스텀 증강 기법**:  
  - Cutout  
  - 회전(Rotate)  
  - 가장자리 크롭(Crop) *(lamp 클래스에 적용)*  
  - 픽셀 밝기 변화 *(노트북 클래스에 적용)*

---

## 🗃️ 사용한 데이터셋 정보

- **클래스 목록**:  
  에어컨, 침대, 책, 의자, 시계, 문, 선풍기, 노트북, 머그컵, 온도계, TV, 창문, 전등, 휴지

- **데이터 포맷**:  
  YOLO 형식 (`.txt` 파일, 정규화된 bounding box 좌표 포함)

- **데이터 분할 비율**:  
  - 일부 데이터셋: Train / Validation / Test = **8:1:1**  
  - 일부 데이터셋: Train / Validation / Test = **7:2:1**


