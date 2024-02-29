# PointPillars
## Environment
```bash
Ubuntu 22.04 humble
CUDA 11.8
cuDNN 8.7
pytorch 2.0.0
```

### CUDA Installation
```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run
echo 'export PATH="/usr/local/cuda-11.8/bin:$PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
```

### cuDNN Installation
```bash
[Download cuDNN v8.7.0 for CUDA 11.X => Local Installer for Linux x86_64 (Tar)] (https://developer.nvidia.com/rdp/cudnn-archive)
cd ~/Download && tar -xvf cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz
sudo cp cudnn-linux-x86_64-8.7.0.84_cuda11-archive/include/cudnn* /usr/local/cuda-11.8/include
sudo cp cudnn-linux-x86_64-8.7.0.84_cuda11-archive/lib/libcudnn* /usr/local/cuda-11.8/lib64
sudo chmod a+r /usr/local/cuda-11.8/include/cudnn.h /usr/local/cuda-11.8/lib64/libcudnn*

sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_ops_train.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8
sudo ln -sf /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8.7.0 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8
sudo ldconfig
```

### PyTorch Installation
```bash
conda create -n LOD python=3.8
conda activate LOD
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
