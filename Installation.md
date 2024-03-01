## PointPillars

### Environment
```bash
Ubuntu 22.04 humble
CUDA 11.8
cuDNN 8.7
pytorch 2.0.0
```

#### CUDA Installation
```bash
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run
echo 'export PATH="/usr/local/cuda-11.8/bin:$PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
```

#### cuDNN Installation
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

#### Verify Settings
```bash
ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn

cat /usr/local/cuda-11.8/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
   `result`
       * #define CUDNN_MAJOR 8
       * #define CUDNN_MINOR 7
       * #define CUDNN_PATCHLEVEL 0
```

#### Construction Environment
```bash
conda create -n LOD python=3.8
conda activate LOD
pip install --upgrade pip
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
pip install matplotlib numba pandas scipy tqdm open3d opencv-python tensorboard
python setup.py develop
```

cd anaconda3/envs/LOD/lib/python3.8/site-packages/torch && gedit functional.py
find VF.meshgrid => indexing='jf' 추가하기
