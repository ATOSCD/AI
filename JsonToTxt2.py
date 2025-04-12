import os
import json

# ✅ YOLO 클래스 목록 정의 ("tissue" 추가)
TARGET_CLASS_NAMES = [
    "air conditioner", "bed", "book", "chair",
    "clock", "door", "fan",
    "laptop", "mug",
    "thermometer", "tv", "window",
    "lamp",  # 이전에 추가한 무드등
    "tissue"  # 이번에 추가할 두루마리휴지
]
TISSUE_KOREAN_NAME = "두루마리휴지"
TISSUE_CLASS_ID = TARGET_CLASS_NAMES.index("tissue")

# ✅ 경로 설정
base_dir = r"C:\Users\user\Desktop\4-1\캡스톤\dataset_extra\tissue\label"
output_dir = os.path.join(base_dir, "yolo_labels")
os.makedirs(output_dir, exist_ok=True)

# ✅ JSON 파일 순회
for file in os.listdir(base_dir):
    if not file.endswith(".json"):
        continue

    json_path = os.path.join(base_dir, file)
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        image_info = data.get("images", [])[0]
        image_id = image_info["id"]
        img_width = image_info["width"]
        img_height = image_info["height"]

        if img_width == 0 or img_height == 0:
            print(f"⚠️ 이미지 크기 오류 (width 또는 height가 0): {file}")
            continue

        annotations = data.get("annotations", [])
        categories = {cat["class_id"]: cat["class_name"] for cat in data.get("categories", [])}
        yolo_lines = []

        for ann in annotations:
            class_id = ann["category_id"]
            class_name = categories.get(class_id)

            if class_name != TISSUE_KOREAN_NAME:
                continue

            x, y, w, h = ann["bbox"]
            x_center = (x + w / 2) / img_width
            y_center = (y + h / 2) / img_height
            norm_w = w / img_width
            norm_h = h / img_height

            yolo_lines.append(f"{TISSUE_CLASS_ID} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}")

        if yolo_lines:
            output_path = os.path.join(output_dir, f"{image_id}.txt")
            with open(output_path, "w", encoding="utf-8") as out_f:
                out_f.write("\n".join(yolo_lines))

    except Exception as e:
        print(f"🚫 오류 발생: {file} → {e}")
