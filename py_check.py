import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

if torch.cuda.is_available():
    torch.set_default_tensor_type(torch.cuda.FloatTensor)