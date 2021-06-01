import gd1 as gd

def f(p):
    [x,y] = p
    return x*x + y*y

p = [1.0, 3.0] # 從(1.0,3.0)開始找
gd.gradientDescendent(f, p)
