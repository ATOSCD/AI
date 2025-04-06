import os

# 경로 설정
image_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\laptop\image"
label_folder = r"C:\Users\user\Desktop\4-1\캡스톤\datset\laptop\label"

# 이미지 파일 이름들 (확장자 제거)
image_basenames = {
    os.path.splitext(f)[0]
    for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
}

# 라벨 파일 이름들 (확장자 제거 + _(4_1) 제거)
label_basenames = {
    os.path.splitext(f)[0].split("_(4_1)")[0]
    for f in os.listdir(label_folder)
    if f.endswith('.json')
}

# 비교
only_in_images = image_basenames - label_basenames
only_in_labels = label_basenames - image_basenames
common = image_basenames & label_basenames

# 출력
print(f"✅ 매칭된 파일 수: {len(common)}")

if only_in_images:
    print(f"\n❌ 라벨이 없는 이미지 파일 ({len(only_in_images)}개):")
    for name in sorted(only_in_images):
        print(name)

if only_in_labels:
    print(f"\n❌ 이미지가 없는 라벨 파일 ({len(only_in_labels)}개):")
    for name in sorted(only_in_labels):
        print(name)

if not only_in_images and not only_in_labels:
    print("\n🎉 이미지와 라벨이 모두 정확히 매칭됩니다!")
