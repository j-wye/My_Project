import cv2
from ultralytics import YOLO  # YOLOv8 라이브러리 임포트
import datetime

def main():
    model = YOLO('yolov8m.pt')

    # Input Camera index Settings
    # Later I gonna change (760 * 480), HD(1280 * 720)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Several Settings for pleasing to the eye (Make Clean Visualization Settings)
    CONFIDENCE_THRESHOLD = 0.6
    fps_list = []
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        start = datetime.datetime.now()
        results = model(frame)[0]
        
        # Visualization of Detection results
        for data in results.boxes.data:
            # (x1, y1) : 좌측 상단, (x2, y2) : 우측 하단, conf : 신뢰도, cls : 클래스
            x_L, y_L, x_R, y_R, conf, cls = data.cpu().numpy()
            if conf < CONFIDENCE_THRESHOLD: continue
            
            label = f'{results.names[int(cls)]} {conf:.2f}'  # 클래스 이름과 신뢰도 레이블
            cv2.rectangle(frame, (int(x_L), int(y_L)), (int(x_R), int(y_R)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x_L), int(y_L)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # FPS 업데이트 및 표시
        end = datetime.datetime.now()
        taken_time = (end - start).total_seconds() # detect 소요시간
        fps = f'FPS : {1 / taken_time:.2f}'
        fps_list.append(1 / taken_time)

        cv2.putText(frame, fps, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('YOLOv8 Object Detection', frame)
        
        # 'q'를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sum, e = 0, 0
            for i in range(len(fps_list)):
                sum += int(fps_list[i])
                e = i
            avg = sum / e
            print(avg)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
