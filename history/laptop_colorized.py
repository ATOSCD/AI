import os

folder = r"C:\Users\user\Desktop\4-1\capstone\dataset_extra\laptop_extra\label"

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        old_path = os.path.join(folder, filename)
        new_filename = filename.replace("laptop(laptop)", "laptop(laptop)_colorized")
        new_path = os.path.join(folder, new_filename)
        os.rename(old_path, new_path)

print("✅ 모든 파일 이름이 변경되었습니다.")
