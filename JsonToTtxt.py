import os
import json

# ✅ 학습에 사용할 클래스 이름들 (이외는 무시)
TARGET_CLASS_NAMES = [
    "air conditioner", "bed", "book", "chair",
    "clock",  "door", "fan",
    "laptop", "mug", 
    "thermometer", "tv", "window"
]
name_to_yolo_id = {name: i for i, name in enumerate(TARGET_CLASS_NAMES)}

# ✅ 단일 클래스 폴더 경로
base_dir = r"C:\Users\user\Desktop\4-1\캡스톤\dataset_extra\window"
label_dir = os.path.join(base_dir, "label")
image_dir = os.path.join(base_dir, "image")
output_label_dir = os.path.join(label_dir, "yolo_labels")
os.makedirs(output_label_dir, exist_ok=True)

# ✅ JSON 파일 순회
for file in os.listdir(label_dir):
    if not file.endswith(".json"):
        continue

    json_path = os.path.join(label_dir, file)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 이미지 정보
    image_info = data["images"][0]
    img_w, img_h = image_info["width"], image_info["height"]
    img_id = int(image_info["id"])
    img_name = os.path.splitext(image_info["file_name"])[0]

    # 카테고리 매핑
    category_id_to_name = {int(cat["id"]): cat["name"] for cat in data["categories"]}

    label_lines = []
    for ann in data["annotations"]:
        if int(ann["image_id"]) != img_id:
            continue

        cat_id = int(ann["category_id"])
        class_name = category_id_to_name.get(cat_id)

        if class_name not in TARGET_CLASS_NAMES:
            continue  # ❌ 무시할 클래스

        class_id = name_to_yolo_id[class_name]
        x, y, w, h = ann["bbox"]
        x_center = (x + w / 2) / img_w
        y_center = (y + h / 2) / img_h
        norm_w = w / img_w
        norm_h = h / img_h

        label_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}")

    # ✅ YOLO 포맷 .txt 저장
    if label_lines:
        out_path = os.path.join(output_label_dir, img_name + ".txt")
        with open(out_path, "w") as f:
            f.write("\n".join(label_lines))

print("✅ YOLO .txt 변환 완료!")
print(f"📁 저장 위치: {output_label_dir}")