import numpy as np
from numpy.linalg import norm

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):# 對 p 的每一個數做偏微分
        gp[k] = df(f, p, k, step)
    return gp # 得到一個向量(梯度)

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.01):
    p = p0.copy() # 把p0複製一份
    i = 0 # 計算第幾代
    while (True):
        i += 1
        fp = f(p)
        gp = grad(f, p) # 計算梯度 gp (梯度是一個向量)
        glen = norm(gp) # norm = 梯度的長度 (步伐大小)
        # norm([x,y]) = √(x^2 + y^2)
        print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
        #                         .3f 浮點數印到第3位
        if glen < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
            break
        gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
        # np.multiply 可以將向量跟常數相乘
        p +=  gstep # 向 gstep 方向走一小步
    return p # 傳回最低點！
