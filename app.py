from flask import Flask, request, render_template
from ultralytics import YOLO
import os
from datetime import datetime

# YOLO 모델 로딩
model = YOLO("best.pt") # 훈련된 모델 경로

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result_img = None
    if request.method == "POST":
        file = request.files["image"]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}.jpg"
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)

        # YOLO 탐지 수행
        results = model.predict(source=upload_path, save=True, project=RESULT_FOLDER, name=timestamp, exist_ok=True)

        # YOLO는 image0.jpg로 저장함 → 동적으로 찾아야 함
        result_dir = os.path.join(RESULT_FOLDER, timestamp)
        saved_files = os.listdir(result_dir)
        saved_img_path = os.path.join(result_dir, saved_files[0])  # image0.jpg 등
        result_img = os.path.relpath(saved_img_path, "static")     # "results/타임스탬프/image0.jpg"
        result_img = result_img.replace("\\", "/")
        print("🖼️ 이미지가 웹에 표시될 경로:", result_img)
    
    return render_template("index.html", result_img=result_img)

    
if __name__ == "__main__":
    app.run(debug=True)
