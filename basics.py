import torch
import numpy as np

x = torch.tensor([[1, 2], [3, 4]])
print(x, x.shape, x.dtype, sep="\n")

print("--------------------------------------------------")

x = torch.tensor([[1.0, 2, 3, 4]])
print(x, x.shape, x.dtype, sep="\n")

print("--------------------------------------------------")

x = torch.arange(9)
y = torch.eye(3, dtype=torch.bool)
z = torch.randn(size=[2, 3, 3])
print(x, y, z, sep="\n")

print("--------------------------------------------------")

mixed_list = [42, 3.14, 'a', True]
try:
    tensor = torch.tensor(mixed_list)
    print(tensor)
except Exception as e:
    print(f"Error: {e}")

x = torch.tensor([1, 2.0, True, False])
print(x)

print("--------------------------------------------------")

bit_tensor = torch.randint(low=0, high=2, size=(2, 3, 4, 5), dtype=torch.uint8)
print(bit_tensor)

print("--------------------------------------------------")

