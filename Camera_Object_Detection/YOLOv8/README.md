## Donwload links
1. [YOLOv8n pretrained Model](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt)

2. [YOLOv8s pretrained Model](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s.pt)

3. [YOLOv8m pretrained Model](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt)

4. [YOLOv8l pretrained Model](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l.pt)

5. [YOLOv8x pretrained Model](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x.pt)

## Settings
Build Environments for Using YOLOv8 :
```bash
cav (#conda activate vision)
pip install -U ultralytics
```
* if you don't have the default settings for conda, vision, then see this [README.md](../README.md) first.

The downloaded pretrained models move to pretrained folder:
```bash
sudo mv ~/Download/yolov8n.pt ~/ros2_ws/src/My_Project/Camera_Object_Detection/YOLOv8/pretrained/
sudo mv ~/Download/yolov8s.pt ~/ros2_ws/src/My_Project/Camera_Object_Detection/YOLOv8/pretrained/
sudo mv ~/Download/yolov8m.pt ~/ros2_ws/src/My_Project/Camera_Object_Detection/YOLOv8/pretrained/
sudo mv ~/Download/yolov8l.pt ~/ros2_ws/src/My_Project/Camera_Object_Detection/YOLOv8/pretrained/
sudo mv ~/Download/yolov8x.pt ~/ros2_ws/src/My_Project/Camera_Object_Detection/YOLOv8/pretrained/
```

## Reference
[YOLOv8 document1](https://docs.ultralytics.com/ko/modes/predict/)

[YOLOv8 document2](https://docs.ultralytics.com/ko/reference/engine/results/#ultralytics.engine.results.Results)

## Explanation of my code
1. Code to check for basic detection 
	```bash
	cav && cd My_Project/Camera_Object_Detection/YOLOv8
	python basic_detection.py
	```
34.00


2. FPS comparison for each model size
	* Result
		| <center>Model</center> | <center>Resolution</center> | <center>CPU</center> | <center>GPU</center> | <center>FPS</center> |
		|:--------|:--------|:--------|:--------|:--------|
		| <center>YOLOv8n.pt</center> | <center>640 * 480</center> | <center>i5-13600KF</center> | <center>NVIDIA GeForce RTX 4070 12GB</center> | <center>**314.75**</center> |
		|| <center>1280 * 720</center> |||<center>**15.17**</center> |
		| <center>YOLOv8s.pt</center> | <center>640 * 480</center> | <center>i5-13600KF</center> | <center>NVIDIA GeForce RTX 4070 12GB</center> | <center>**234.39**</center> |
		|| <center>1280 * 720</center> |||<center>**120**</center> |
		| <center>YOLOv8m.pt</center> | <center>640 * 480</center> | <center>i5-13600KF</center> | <center>NVIDIA GeForce RTX 4070 12GB</center> | <center>**134.21**</center> |
		|| <center>1280 * 720</center> |||<center>**120**</center> |
		| <center>YOLOv8l.pt</center> | <center>640 * 480</center> | <center>i5-13600KF</center> | <center>NVIDIA GeForce RTX 4070 12GB</center> | <center>**92.48**</center> |
		|| <center>1280 * 720</center> |||<center>**120**</center> |
		| <center>YOLOv8x.pt</center> | <center>640 * 480</center> | <center>i5-13600KF</center> | <center>NVIDIA GeForce RTX 4070 12GB</center> | <center>**59.22**</center> |
		|| <center>1280 * 720</center> |||<center>**120**</center> |
