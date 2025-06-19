import os

# 라벨 폴더 경로
label_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_extra\mood_light_extra\test\labels'

# 검토 대상 라벨 파일 찾기
label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

print("🔍 잘못된 YOLO 라벨 파일 검사 중...")

for file_name in label_files:
    file_path = os.path.join(label_dir, file_name)
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if not lines:
        print(f"⚠️ 빈 라벨 파일: {file_path}")
        continue

    for line_num, line in enumerate(lines, 1):
        parts = line.strip().split()
        try:
            if len(parts) != 5:
                raise ValueError("필드 개수 오류")
            int(parts[0])  # 클래스 ID
            float(parts[1])  # center_x
            float(parts[2])  # center_y
            float(parts[3])  # width
            float(parts[4])  # height
        except Exception as e:
            print(f"❌ 잘못된 라벨 형식: {file_path} (줄 {line_num}) → '{line.strip()}'")
            break  # 한 줄이라도 이상하면 해당 파일명만 1회 출력
