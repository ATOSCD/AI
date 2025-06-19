import os

# YOLO 라벨 파일들이 저장된 경로
label_dir = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra\label"

# 1. 클래스 ID 0 → 12로 변경
for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            if line.strip() == "":
                continue
            parts = line.strip().split()
            if parts[0] == "0":
                parts[0] = "12"
            new_lines.append(" ".join(parts))

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

print("✅ 클래스 ID 0 → 12로 변경 완료")

# 2. 여전히 13이 아닌 ID가 있는지 확인
non_13_ids = set()

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if line.strip() == "":
                continue
            parts = line.strip().split()
            class_id = parts[0]
            if class_id != "12":
                non_13_ids.add(class_id)

# 결과 출력
if non_13_ids:
    print(f"⚠️ 13이 아닌 클래스 ID가 존재합니다: {sorted(non_13_ids)}")
else:
    print("✅ 모든 클래스 ID가 12입니다.")
