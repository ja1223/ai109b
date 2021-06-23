import torch
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)
f = x*x+y*y
f.backward()     # automatically calculates the gradient
print(x.grad)    # ∂f/∂x = 2
print(y.grad)    # ∂f/∂y = 6
print(f.item())