# YOLOv8 기반 도로표지판 탐지 웹앱

이 프로젝트는 GTSDB (German Traffic Sign Detection Benchmark) 데이터셋을 기반으로, YOLOv8 모델을 학습시켜 도로표지판을 탐지하고 웹에서 실시간으로 시각화할 수 있는 시스템입니다.

---

## 프로젝트 구조

```
project_root/
├── app.py                     # Flask 웹 서버 코드
├── best.pt                    # 훈련된 YOLOv8 모델
├── templates/
│   └── index.html             # 사용자 웹 업로드 UI
├── static/
│   ├── uploads/               # 업로드된 원본 이미지
│   └── results/               # 탐지 결과 이미지 (YOLO 자동 생성)
└── README.md
```


##  실행 방법

1. Python 환경에서 필요한 라이브러리 설치
```bash
pip install flask ultralytics pillow
```

2. `app.py` 실행
```bash
python app.py
```

3. 웹 브라우저에서 접속
```
http://localhost:5000
```

## 사용된 기술

- **모델**: YOLOv8s (Ultralytics)
- **프레임워크**: Flask (Python 기반 웹 서버)
- **데이터셋**: GTSDB (German Traffic Sign Detection Benchmark)
- **기능**:
  - 이미지 업로드
  - YOLO 모델로 탐지 수행
  - 탐지 결과 웹에 즉시 표시

---

## 훈련 성능 요약

- 에폭 수: 50
- 이미지 크기: 640x640
- `mAP50`: 약 0.30
- `mAP50-95`: 약 0.22

---

## 참고
- YOLOv8 공식 문서: https://docs.ultralytics.com
- GTSDB 데이터셋: http://benchmark.ini.rub.de/?section=gtsdb

