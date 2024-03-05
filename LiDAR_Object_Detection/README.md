# 3D LiDAR Object Detection for just studying

## 1. PointPillars

### Settings
1. Anaconda Environment Setting
    ```bash
    conda create -n lidar python=3.8
    echo "alias cal='conda activate lidar'" >> ~/.bashrc
    sb && cal
    pip install --upgrade pip
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
    ```