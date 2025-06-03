from flask import Flask, request, render_template
from ultralytics import YOLO
import os
from datetime import datetime

# YOLO 모델 로딩
model = YOLO("best.pt")
class_names = model.names  # 클래스 ID → 이름 딕셔너리

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result_img = None
    detected_classes = []

    if request.method == "POST":
        file = request.files["image"]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}.jpg"
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)

        # YOLO 탐지
        results = model.predict(source=upload_path, save=True, project=RESULT_FOLDER, name=timestamp, exist_ok=True)

        # 결과 이미지 경로 설정
        result_dir = os.path.join(RESULT_FOLDER, timestamp)
        saved_img_path = os.path.join(result_dir, os.listdir(result_dir)[0])
        result_img = os.path.relpath(saved_img_path, "static").replace("\\", "/")

        # 탐지된 클래스 ID 추출 후 중복 제거
        boxes = results[0].boxes
        class_ids = boxes.cls.tolist()
        detected_classes = sorted(set(class_names[int(cls)] for cls in class_ids))

    return render_template("index.html", result_img=result_img, detected_classes=detected_classes)

    
if __name__ == "__main__":
    app.run(debug=True)
