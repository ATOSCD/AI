import os

label_dir = r'C:\Users\user\Desktop\4-1\capstone\dataset_final\labels\val'

# .txt 파일 목록
label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
total = len(label_files)
next_threshold = 0.1

print("🔍 음수 바운딩 박스 값 확인 중...")

for idx, filename in enumerate(label_files):
    file_path = os.path.join(label_dir, filename)

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        parts = line.strip().split()
        if len(parts) != 5:
            continue  # 잘못된 라인 무시

        cls_id, x, y, w, h = parts
        try:
            x = float(x)
            y = float(y)
            w = float(w)
            h = float(h)
            if x < 0 or y < 0 or w < 0 or h < 0:
                print(f"❌ 음수 바운딩 박스: {file_path} (줄 {line_num}) → '{line.strip()}'")
                break  # 한 줄이라도 음수면 해당 파일만 한 번 출력
        except ValueError:
            continue  # 숫자 변환 안 되면 무시

    # 10% 단위 진행 출력
    if (idx + 1) / total >= next_threshold:
        print(f"[{int(next_threshold * 100)}%] 검사 중...")
        next_threshold += 0.1

print("✅ 음수 바운딩 박스 검사 완료.")
