import os
import shutil
from PIL import Image

# 입력 경로
src_img_dir = 'GTSDB/Images'
gt_file = 'GTSDB/gt.txt'

# 출력 경로
output_img_dir = 'dataset/images/train'
output_label_dir = 'dataset/labels/train'
os.makedirs(output_img_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 라벨 처리
with open(gt_file, 'r') as f:
    for line in f:
        filename, xmin, ymin, xmax, ymax, class_id = line.strip().split(';')
        ppm_path = os.path.join(src_img_dir, filename)
        jpg_filename = filename.replace('.ppm', '.jpg')
        jpg_path = os.path.join(output_img_dir, jpg_filename)

        # 이미지 변환 및 저장
        with Image.open(ppm_path) as img:
            img.save(jpg_path)
            w, h = img.size

        # 바운딩 박스 YOLO 포맷으로 변환
        xmin, ymin, xmax, ymax = map(int, [xmin, ymin, xmax, ymax])
        x_center = ((xmin + xmax) / 2) / w
        y_center = ((ymin + ymax) / 2) / h
        box_width = (xmax - xmin) / w
        box_height = (ymax - ymin) / h

        yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n"
        label_path = os.path.join(output_label_dir, filename.replace('.ppm', '.txt'))

        with open(label_path, 'a') as lf:
            lf.write(yolo_line)
