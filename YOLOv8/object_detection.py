import cv2
from ultralytics import YOLO  # YOLOv8 라이브러리 임포트
import time

def main():
    model = YOLO('yolov8m.pt')

    cap = cv2.VideoCapture(0)
    
    fps = 0
    frame_count = 0
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        
        # Visualization of Detection results
        for det in results[0].boxes.data:
            # (x1, y1) : 좌측 상단, (x2, y2) : 우측 하단, conf : 신뢰도, cls : 클래스
            x1, y1, x2, y2, conf, cls = det.cpu().numpy()
            label = f'{results[0].names[int(cls)]} {conf:.2f}'  # 클래스 이름과 신뢰도 레이블
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # FPS 업데이트 및 표시
        frame_count += 1
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > 1:  # 매 초마다 FPS 업데이트
            fps = int(frame_count / elapsed_time)
            frame_count = 0
            start_time = current_time

        cv2.putText(frame, f'FPS: {fps:.2f}', (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('YOLOv8m Object Detection', frame)
        
        # 'q'를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
