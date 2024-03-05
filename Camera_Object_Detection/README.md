# Camera Object Detection for just studying

## 1. YOLOv8

### Settings
1. Anaconda Envrionment Setting
    
    ```bash
    conda create -n vision python=3.11
    echo "alias cav='conda activate vision'" >> ~/.bashrc
    sb && cav
    pip install --upgrade pip
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
    pip install numpy opencv-python matplotlib
    ```
