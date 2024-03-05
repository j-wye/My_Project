#### 2024-03-01
- Make Github and study how to use
- KITTI Dataset Setting [:link:](../LiDAR_Object_Detection/PointPillars/README.md#datasets)
- Customize python codes and settings [:link:](../LiDAR_Object_Detection/PointPillars/)
- Progress training with downloaded datasets [:link:](../LiDAR_Object_Detection/PointPillars/README.md#compile)

#### 2024-03-04
- Compare the pretrained model with the model I trained
- Pretrained model's performance is better than I did
- Progress evalutation, test and visualization [:link:](../LiDAR_Object_Detection/PointPillars/README.md#evaluation)

#### 2024-03-05
- ***<U>3D LiDAR Object Detection의 결과를 어떻게 활용해야 할지는 좀 더 고민해볼것..</U>***
- 지금까지 떠오른 생각은 아래와 같다
    
    1.
        ```
        Object Detection with LiDAR and Camera simultaneously and separately
        => Generate each accuracy result as a list
        => Create a new list from each of the two lists via dot product
        => Normalize the new list to generate the final accuracy list
        ```
        이렇게 만들어진 final accuracy list가 기존의 각각의 accuracy list와 비교해서 어떠할지 한번 시도..!
        - 비가오거나, 흐릿할 때 위의 결과가 더 나은 성능을 보인다면 성공적인 시도

    2. 


#### 2024-03-06
- Result of Detection with YOLOv8
    - Test with 