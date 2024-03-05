## Settings
1. Virtual Envrionment with Anaconda
  ```bash
  conda create -n vision python=3.11
  echo "alias cav='conda activate vision'" >> ~/.bashrc
  sb && cav
  pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
  pip install numpy opencv-python matplotlib
  ```

2. For Vision Envrironment
  ```bash
  pip install -U ultralytics
  ```



## Download YOLOv8m.pt
[YOLOv8m pretrained Model Download](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt)

## Reference
[YOLOv8 document1](https://docs.ultralytics.com/ko/modes/predict/)

[YOLOv8 document2](https://docs.ultralytics.com/ko/reference/engine/results/#ultralytics.engine.results.Results)


