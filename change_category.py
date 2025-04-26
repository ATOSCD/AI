import os

# label 폴더 경로
label_dir = r'C:\Users\user\Desktop\4-1\capstone\labels'

# labels 폴더 안의 모든 txt 파일 읽기
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(label_dir, filename)

        # 파일 읽기
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # 각 줄을 수정: 맨 앞 class_id만 0 -> 3 으로
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5:
                parts[0] = '3'  # class_id를 3으로 수정
                new_line = ' '.join(parts)
                new_lines.append(new_line + '\n')

        # 파일 다시 저장
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

print("모든 label 파일에서 class_id 0 → 3으로 수정 완료했습니다!")
