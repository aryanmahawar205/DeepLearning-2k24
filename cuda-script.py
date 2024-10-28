import torch

print(torch.cuda.device_count()) # return GPU count

print(torch.cuda.get_device_name()) # return GPU specs
