from ultralytics import YOLO
import cv2
import time
import random

def plot_one_box(x, img, color=None, label=None, line_thickness=2):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def main():
    model = YOLO('./pretrained/yolov8m.pt').to('cuda')
    class_names = model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in class_names]
    
    # Input Camera index Settings
    # "/dev/video2" == 2 : 회색 점이 나타는 것으로 보아 depth 파트
    # "/dev/video4" == 4 : RGB의 깔끔한 화면으로 나타나는 것으로 보아 RGB 파트
    cap = cv2.VideoCapture(4)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    if not (cap.isOpened()) :
         print("Could not open video device")
    
    # Several Settings for pleasing to the eye (Make Clean Visualization Settings)
    CONFIDENCE_THRESHOLD = 0.7
    initial_time = 0
    while True:
        ret, img = cap.read()
        if not ret : break
        
        # Calculate and display FPS
        current_time = time.time()
        taken_time = current_time - initial_time
        fps = 1 / taken_time
        fps_str = f'FPS : {fps:.1f}'
        initial_time = current_time

        cv2.putText(img, fps_str, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        results = model(img)[0]
        
        # Visualization of Detection results
        for data in results.boxes.data:
            # (x1, y1) : 좌측 상단, (x2, y2) : 우측 하단, conf : 신뢰도, cls : 클래스
            x_L, y_L, x_R, y_R, conf, cls = data.cpu().numpy()
            print(data.cpu().numpy())
            # confidence 값이 threshold보다 작다면 검출하지 않고 continue
            if conf < CONFIDENCE_THRESHOLD: continue
            
            plot_one_box([x_L, y_L, x_R, y_R], img, colors[int(cls)], f'{class_names[int(cls)]} {float(conf):.2f}')
        
        cv2.imshow('YOLOv8 Object Detection', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
