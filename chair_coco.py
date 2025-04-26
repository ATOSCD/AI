from pycocotools.coco import COCO

# 주석 파일 경로 수정
coco = COCO(r'C:\Users\user\Downloads\annotations\instances_train2017.json')

# 'chair' 카테고리의 ID 가져오기
cat_ids = coco.getCatIds(catNms=['chair'])

# 해당 카테고리가 포함된 이미지 ID 가져오기
img_ids = coco.getImgIds(catIds=cat_ids)

print(f"'chair' 카테고리가 포함된 이미지 수: {len(img_ids)}")