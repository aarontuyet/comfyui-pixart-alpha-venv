@echo off
cd /d C:\DevProjects\ComfyUI
call venv\Scripts\activate.bat
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
python main.py --lowvram --cuda-device 0
pause