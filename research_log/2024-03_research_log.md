#### 2024-03-01
- Make Github and study how to use
- KITTI Dataset Setting [🔗](../LiDAR_Object_Detection/PointPillars/README.md#datasets)
- Customize python codes and settings [🔗](../LiDAR_Object_Detection/PointPillars/)
- Progress training with downloaded datasets [🔗](../LiDAR_Object_Detection/PointPillars/README.md#compile)

#### 2024-03-04
- Compare the pretrained model with the model I trained
- Pretrained model's performance is better than I did
- Progress evalutation, test and visualization [🔗](../LiDAR_Object_Detection/PointPillars/README.md#evaluation)

#### 2024-03-05
- ***<U>3D LiDAR Object Detection의 결과를 어떻게 활용해야 할지는 좀 더 고민해볼것..</U>***
- 지금까지 떠오른 생각
    
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
        - VoxelNet[🔗](https://arxiv.org/abs/1711.06396), PointNet++[🔗](https://arxiv.org/abs/1706.02413)
        - Study the concept, then apply with the algorithm


#### 2024-03-06
- Study how to use YOLOv8 [🔗](../Camera_Object_Detection/YOLOv8/README.md#reference)
- Performance experiments with all pretrained models [🔗](../Camera_Object_Detection/YOLOv8/README.md#model-test)
    - I put first priority on **Real-time**
    - LiDAR Object Detection 코드가 완성되면 반복적인 실험으로 적절한 pretrained model 선택
- Up to now progress [🔗](../Camera_Object_Detection/YOLOv8/README.md#progress)

#### 2024-03-07 ~ 2024-03-12 (예정)
- Coding for ***Extracting*** Camera Object Detection accuracy list
- Coding for ***Extracting*** LiDAR Object Detection accuracy list (Difficult..)

#### 2024-03-11
- Searching about which mathematical subjects have to learn :
    1. Linear Algebra (선형대수학)

    2. Calculus and Multivariable Calculus (미적분학 및 다변수 미적분학)

    3. Probability and statistics (확률론과 통계)

    4. Optimiaztion Theory (최적화 이론)
        - Convex Optimization (볼록 최적화) : `목적함수와 제약 조건이 모두 볼록 함수인 최적화 문제, 전역 최적해 존재`
        - Non-convex Optimization (비볼록 최적화) : `볼록이 아닌 최적화 문제로, 여러 지역 최적해를 가질 수 있음`
        - Gradient Descent (경사하강법) : `목적함수의 gradient를 사용하여 최소점 찾는 방법`
        - Stochastic Optimization (확률적 최적화) : `불확실성을 포함하는 최적화 문제를 해결하는 방법`

    5. Non-linear Algebra (비선형 대수학)

    6. Graph Theory (그래프 이론)
        - Wieghted Graphs (가중치 그래프) : `각 엣지에 가중치가 할당된 그래프`
        - Paths and Cycles (경로와 사이클) : `그래프내에서 노드 사이를 연결하는 엣지의 순서. 사이클은 시작점과 종료점이 같은 경로`
        - Graph Connectivity (그래프 연결성) : `어떤 노드에서 다른 노드로 도달할 수 있는지의 여부`
        - Trees and Spanning Trees (트리와 신장트리) : `사이클이 없는 연결 그래프. Spanning Trees는 원래 그래프의 모든 노드를 포함하면서도 최소한의 엣지로 구성된 트리`
        - Graph Algorithms (그래프 알고리즘) :`그래프 탐색(예:DFS, BFS), 최단 경로 찾기(Dijkstra, A*), 최소 신장 트리 찾기(Kruskal, Prim)`

    7. Differential Geometry (미분 기하학)
        - Manifolds (다양체) : `고차원 공간에서 곡선이나 곡면과 같이 연속적인 구조를 일반화한 개념`
        - Curvature (곡률) : `곡면이나 공간이 얼마나 휘어져 있는지를 측정` -> **<span style="background-color:#FFE6E6"> 자동차의 경로 계획에 중요한 정보 제공 </span>**
        - Geodesics (최단 경로) : `곡면 상에서 두 점을 잇는 가장 짧은 경로` -> **<span style="background-color:#FFE6E6"> 경로 계획에서 최적 경로 찾는데 사용 </span>**

    8. Riemannian Theory (리만 기하학)
        - Riemannian Metric (리만 행렬) : `다양체 내의 점들 사이의 거리를 측정하는 함수` -> **<span style="background-color:#FFE6E6"> 로컬 거리 정보 제공 </span>**
        - Connections (연결) : `다양체 상에서 벡터 필드의 방향을 어떻게 변화시킬지 정의` -> `경로의 곡률을 계산하는데 필요`
        - Ricci Curvature (리치 곡률) : `다양체의 곡률을 나타내는 또 다른 측정치로 공간의 전반적인 구조를 이해하는데 도움`

    9. Topology (위상수학)
        - Homeomorphisms (위상동형) : `한 공간을 다른 공간으로 연속적으로 변형할 수 있는지 여부를 나타냄`
        - Fundamental Groups (기본 군) : `공간의 구멍이나 비어있는 공간을 나타내는 대수적 구조` -> `공간의 연결성을 이해하는데 사용`
        - Compactness (콤팩트성) : `공간이 제한된 크기를 가지고 있는지의 여부를 나타내며, 계산 가능성이나 데이터 표현에 중요한 역할`

- Learning Order :

    Basic Mathemetical Foundations
    1. Linear Algebra
        - 벡터와 행렬 계산, 고유값과 고유벡터

    2. Calculus and Multivariable Calculus
        - 미분, 적분, 다변수 함수의 미적분 학습 -> 변화율, 최적화 문제의 기본, 연속적인 데이터 모델링에 대한 이해
    
    3. Probability and Statistics
        - 확률 이론, 확률 변수, 통계적 추정과 검정, 베이지안 추론 학습 -> 센서 데이터의 불확실성을 다루고, 노이즈 관리 능력 향상
    
    4. Optimization Theory
        - 최적화 문제의 정의, 경사 하강법, 볼록 최적화 -> **<span style="background-color:#FFE6E6"> 경로 계획, 센서 교정, 위치 추정 </span>**
    
    5. Differential Equations
        - 시스템의 동적인 행동 모델링, 시스템의 시간에 따른 변화 이해
    
    Advanced Methetical
    1. Non-linear Algebra
    
    2. Differential Geometry
        - 곡면, 다양체, 곡률 -> **<span style="background-color:#FFE6E6"> SLAM에서의 맵 생성, 경로 계획에서의 기하학적 개념 필요성 충족 </span>**
    
    3. Riemannian Geometry
        - 다양체 상의 거리와 각도 -> **<span style="background-color:#FFE6E6"> 복잡한 환경에서의 Localization and Mapping </span>**
    
    4. Graph Theory
        - 경로, 네트워크 흐름, 최소 신장 트리 -> SLAM에서의 데이터 연관성과 분석, 네트워크 기반 모델링
    
    5. Topology
        - 공간의 연속적인 속성, 위상동형, 기본 군 -> 데이터의 연속성과 공간적 특성 이해
    




#### Blah Blah,,,
- Camera, Lidar 각각 Detection 가능하도록 코드 작성
- Calibration 공부
    - 자동으로 calibration 가능한 알고리즘 먼저 해볼 것
        - camera, lidar가 장착되어 rosbag record한 데이터에 대해서 자동으로 calibration 값을 구해주는지
- 이후 두 센서를 어떻게 합칠 것인지 .... 
    - 기계관 107에 존재하는 차량 하나를 사용해서 데이터셋 확보(?)
        - 하나의 환경에서 고정된 두 센서를 활용한 데이터 수집 
    - 아니면 
- Lidar Segmentation (나중에)
