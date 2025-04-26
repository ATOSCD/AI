from pycocotools.coco import COCO
import os
import shutil

# 경로 설정
annotation_path = r'C:\Users\user\Downloads\annotations\instances_train2017.json'
image_source_dir = r'C:\Users\user\Downloads\train2017\train2017'
image_target_dir = r'C:\Users\user\Desktop\4-1\capstone\images'
label_target_dir = r'C:\Users\user\Desktop\4-1\capstone\labels'

# 폴더 없으면 만들기
os.makedirs(image_target_dir, exist_ok=True)
os.makedirs(label_target_dir, exist_ok=True)

# COCO 주석 파일 로드
coco = COCO(annotation_path)

# 'chair' 카테고리 ID 가져오기
chair_cat_id = coco.getCatIds(catNms=['chair'])[0]

# 'chair'가 포함된 이미지 ID 가져오기
chair_img_ids = coco.getImgIds(catIds=[chair_cat_id])

print(f"'chair'가 포함된 이미지 수: {len(chair_img_ids)}")

# chair 이미지만 복사 + labels txt 생성
for img_id in chair_img_ids:
    img_info = coco.loadImgs(img_id)[0]
    img_filename = img_info['file_name']  # ex) 000000000670.jpg
    img_width = img_info['width']
    img_height = img_info['height']

    # 이미지 복사
    src_img_path = os.path.join(image_source_dir, img_filename)
    dst_img_path = os.path.join(image_target_dir, img_filename)

    if os.path.exists(src_img_path):
        shutil.copy(src_img_path, dst_img_path)

    # chair annotation만 가져오기
    ann_ids = coco.getAnnIds(imgIds=[img_id], catIds=[chair_cat_id])
    anns = coco.loadAnns(ann_ids)

    # label txt 저장
    label_filename = os.path.splitext(img_filename)[0] + ".txt"
    label_file_path = os.path.join(label_target_dir, label_filename)
    
    with open(label_file_path, 'w') as f:
        for ann in anns:
            bbox = ann['bbox']  # [x_min, y_min, width, height]
            x_center = (bbox[0] + bbox[2]/2) / img_width
            y_center = (bbox[1] + bbox[3]/2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height
            # YOLO 포맷: class_id x_center y_center width height
            f.write(f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

print(f"총 {len(chair_img_ids)}개의 이미지를 복사하고, label 파일을 생성했습니다.")
