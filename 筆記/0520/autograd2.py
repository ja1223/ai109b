import torch
x = torch.tensor([1.0,3.0], requires_grad=True)
n = x.norm()
f = n*n
f.backward()
print('f=', f.item())
print('x.grad=', x.grad)
