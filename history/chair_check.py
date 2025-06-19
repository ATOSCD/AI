import os

# labels 폴더 경로
label_dir = r'C:\Users\user\Desktop\4-1\capstone\labels'

# 결과 저장용 리스트
bad_files = []

# labels 폴더 안 모든 txt 파일 확인
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(label_dir, filename)

        with open(file_path, 'r') as f:
            lines = f.readlines()

        # 한 줄이라도 class_id가 3이 아닌 경우가 있는지 확인
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5:
                if parts[0] != '3':
                    bad_files.append(filename)
                    break  # 하나라도 발견되면 그 파일은 추가하고 바로 다음 파일로 넘어감

# 결과 출력
if bad_files:
    print("class_id가 3이 아닌 파일들:")
    for file in bad_files:
        print(file)
else:
    print("모든 파일의 class_id가 3입니다!")
