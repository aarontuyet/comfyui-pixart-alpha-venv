# version_report.py
import torch
import diffusers
import transformers
import platform
import os

report = {
    "Python version": platform.python_version(),
    "Platform": platform.platform(),
    "CUDA available": torch.cuda.is_available(),
    "Torch version": torch.__version__,
    "Torch CUDA version": torch.version.cuda,
    "Diffusers version": diffusers.__version__,
    "Transformers version": transformers.__version__,
    "CUDA Memory Config": os.environ.get("PYTORCH_CUDA_ALLOC_CONF", "Not set")
}

with open("__README_ZIP_STUFF__\\environment_version_report.txt", "w") as f:
    for k, v in report.items():
        f.write(f"{k}: {v}\n")