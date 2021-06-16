import random

def hillClimbing(f, x, y, h=0.01):
    while (True):
        fxy = f(x, y)
        print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        if f(x+h, y) >= fxy: #如果右邊的高度 f(x+h, y) 比目前的高度 fxy 高，那就往右邊移動
            x = x + h 
        elif f(x-h, y) >= fxy: #如果左邊的高度 f(x+h, y) 比目前的高度 fxy 高，那就往左邊移動
            x = x - h
        elif f(x, y+h) >= fxy: #如果上面的高度 f(x+h, y) 比目前的高度 fxy 高，那就往上面移動
            y = y + h
        elif f(x, y-h) >= fxy: #如果下面的高度 f(x+h, y) 比目前的高度 fxy 高，那就往下面移動
            y = y - h
        else:
            break
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x - 2*x + y*y + 2*y - 8 ) #求-x^2 + 2x - y^2 - 2y + 8 的最高點，也就是 x^2 - 2x + y^2 + 2y - 8 的最低點

hillClimbing(f, 0, 0)  # 以 x=0,y=0 為起點，開始呼叫爬山演算法