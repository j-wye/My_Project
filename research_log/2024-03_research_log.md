#### 2024-03-01
- Make Github and study how to use
- KITTI Dataset Setting [🔗](../LiDAR_Object_Detection/PointPillars/README.md#datasets)
- Customize python codes and settings [🔗](../LiDAR_Object_Detection/PointPillars/)
- Progress training with downloaded datasets [🔗](../LiDAR_Object_Detection/PointPillars/README.md#compile)

#### 2024-03-04
- Compare the pretrained model with the model I trained
- Pretrained model's performance is better than I did
- Progress evalutation, test and visualization [:link:](../LiDAR_Object_Detection/PointPillars/README.md#evaluation)

#### 2024-03-05
- ***<U>3D LiDAR Object Detection의 결과를 어떻게 활용해야 할지는 좀 더 고민해볼것..</U>***
- 지금까지 떠오른 생각은 아래와 같다
    
    1. My Subjective thoughts (Eliminate feasibility) # 실현가능성 배제
        - Object Detection with LiDAR and Camera simultaneously and separately
        - Generate each accuracy result as a list
        - Create a new list from each of the two lists via dot product
        - Normalize the new list to generate the final accuracy list

        이렇게 만들어진 final accuracy list가 기존의 각각의 accuracy list와 비교해서 어떠할지 한번 시도..!
        - 비가오거나, 흐릿할 때 final accuracy list가 더 나은 성능을 보인다면 성공적인 시도

        또 다른 방법 : 날씨에 따른 가중치를 두어 two accuracy list dot product
        - 문제점 : 가중치를 어떻게 메길 것인지
            - *<U>날씨에 따라 줄 수 있는 standard가 존재하는지아니면 이걸(?) 연구.. 이미 존재하는지 찾아보기</U>*

    2. LiDAR-Camera Calibration
        - LiDAR-Camera Calibration을 진행 (알고리즘 미정)
        - 이를 사용해 object detection accuracy 향상 확인 (그냥 해보는 느낌)

    3. Manipulator Robot
        - Robot arm에 camera가 장착되면 이를 활용해 볼 방법 생각
            - Basic : camera object detection기반으로 robot arm 조종
            - Known environment 여러 미션 수행
                1. 물건을 찾을때까지 SLAM주행
                2. 물건을 찾으면 robot arm을 조종해서 물체를 들거나 하는 mission
                3. 행동 이후 다시 원래 자리로 돌아오기
    
    4. LiDAR PCD Structure study
        - VoxelNet[:link:](https://arxiv.org/abs/1711.06396), PointNet++[:link:](https://arxiv.org/abs/1706.02413)
        - Study the concept, then apply with the algorithm


#### 2024-03-06
- Study how to use YOLOv8 [:link:](../Camera_Object_Detection/YOLOv8/README.md#reference)
- Performance experiments with all pretrained models [:link:](../Camera_Object_Detection/YOLOv8/README.md#model-test)
    - I put first priority on **Real-time**
    - LiDAR Object Detection 코드가 완성되면 반복적인 실험으로 적절한 pretrained model 선택
- Up to now progress [:link:](../Camera_Object_Detection/YOLOv8/README.md#progress)

#### 2024-03-07 ~ 2024-03-12 (예정)
- Coding for ***Extracting*** Camera Object Detection accuracy list
- Coding for ***Extracting*** LiDAR Object Detection accuracy list (Difficult..)


#### TODO
- Camera, Lidar 각각 Detection 가능하도록 코드 작성
- Calibration 공부
    - 자동으로 calibration 가능한 알고리즘 먼저 해볼 것
        - camera, lidar가 장착되어 rosbag record한 데이터에 대해서 자동으로 calibration 값을 구해주는지
- 이후 두 센서를 어떻게 합칠 것인지 .... 
    - 기계관 107에 존재하는 차량 하나를 사용해서 데이터셋 확보(?)
        - 하나의 환경에서 고정된 두 센서를 활용한 데이터 수집 
    - 아니면 
- Lidar Segmentation (나중에)
