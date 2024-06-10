# Install specific cuda version with conda
conda install nvidia/label/cuda-11.8.0::cuda-toolkit -c nvidia/label/cuda-11.8.0

## Deepspeed problem
To fix AttributeError: 'DeepSpeedCPUAdam' object has no attribute 'ds_opt_adam', do conda install gxx_linux-64
