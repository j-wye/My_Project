from ultralytics import YOLO
import cv2
import time

def main():
    model = YOLO('./pretrained/yolov8m.pt').to('cuda')

    # Input Camera index Settings
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Several Settings for pleasing to the eye (Make Clean Visualization Settings)
    CONFIDENCE_THRESHOLD = 0.7

    initial_time = 0
    while True:
        ret, img = cap.read()
        if not ret: break
        
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
            
            # confidence 값이 threshold보다 작다면 검출하지 않고 continue
            if conf < CONFIDENCE_THRESHOLD: continue
            
            # 클래스 이름과 신뢰도 레이블
            label = f'{results.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(img, (int(x_L), int(y_L)), (int(x_R), int(y_R)), (0, 255, 0), 2)
            cv2.putText(img, label, (int(x_L), int(y_L)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        
        cv2.imshow('YOLOv8 Object Detection', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
