# Standard Settings before Project
### Environment
```
Ubuntu 22.04 humble
nvidia-driver-525
CUDA 11.8
cuDNN 8.7
pytorch 2.0.0
```

### Humble Installation
```
mkdir -p A
cd ~/A
wget https://raw.githubusercontent.com/blu-y/turtle/main/autoset.sh
bash autoset.sh
sudo apt-get install nvidia-driver-525 -y
source ~/.bashrc
```

### CUDA Installation
```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run
echo 'export PATH="/usr/local/cuda-11.8/bin:$PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
```

### cuDNN Installation
[Download cuDNN v8.7.0 for CUDA 11.X => Local Installer for Linux x86_64 (Tar)](https://developer.nvidia.com/rdp/cudnn-archive)
```bash
tar -xvf ~/Download/cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz -C ~/A/ && cd ~/A
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

### Verify CUDA, cuDNN Settings
```bash
ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn

cat /usr/local/cuda-11.8/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
```

### Conda Environment Settings
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
sha256sum Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh
echo 'export PATH="/opt/anaconda3/bin:$PATH" >> ~/.bashrc'
source ~/.bashrc
```

`cd anaconda3/envs/LOD/lib/python3.8/site-packages/torch && gedit functional.py => find VF.meshgrid => indexing='jf' 추가하기`

### Make Clean Directory
`sudo rm -rf ~/A`