# Personal Projects
## [Research Log](./research%20log/README.md)
## Basic Settings before project
[settings.md](./settings.md) : Installation before doing project. 

## Camera Object Detection
1. YOLOv8
- 기존에 사용하던 알고리즘은 yolov5. 좀 더 최신버전이 나왔고 기존의 방법과 다르게 패키지를 사용해서 진행
- 기존의 방식은 아래와 같이 git clone을 통해서 yolov5라는 프로젝트를 다운로드해서 진행
    - `git clone https://github.com/ultralytics/yolov5.git`
    - 다운로드 받은 pretrained model을 아래의 코드를 통해서 사용
    - `model = torch.hub.load('./yolov5', 'custom',  'yolov5s.pt', source='local')`
- 현재는 pip로 ultralytics 패키지를 받아서 진행
    - `pip install -U ultralytics`
    - 현재는 `from ultralytics import YOLO` 이후 `model = YOLO('./pretrained/yolov8s.pt').to('cuda')` 의 방식을 사용


## 3D LiDAR Object Detection
1. PointPillars


## LiDAR-Camera Calibration (예정)