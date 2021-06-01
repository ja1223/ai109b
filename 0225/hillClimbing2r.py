import random

def hillClimbing(f, x, y, h=0.01):
    failCount = 0                    # 失敗次數歸零
    while (failCount < 10000):       # 如果失敗次數小於一萬次就繼續執行
        fxy = f(x, y)                # fxy 為目前高度
        dx = random.uniform(-h, h)   # dx 為左右偏移量，範圍在-0.01~0.01之間
        dy = random.uniform(-h, h)   # dy 為前後偏移量，範圍在-0.01~0.01之間
        if f(x+dx, y+dy) >= fxy:     # 如果移動後高度比現在高
            x = x + dx               #   就移過去
            y = y + dy
            print('x={:.3f} y={:.3f} f(x,y)={:.3f}'.format(x, y, fxy))
            failCount = 0            # 失敗次數歸零
        else:                        # 若沒有更高
            failCount = failCount + 1#   那就又失敗一次
    return (x,y,fxy)                 # 結束傳回 （已經失敗超過一萬次了）

def f(x, y):
    return -1 * ( x*x -2*x + y*y +2*y - 8 ) #求-x^2 + 2x - y^2 - 2y + 8 的最高點，也就是 x^2 - 2x + y^2 + 2y - 8 的最低點

hillClimbing(f, 0, 0)  # 以 x=0,y=0 為起點，開始呼叫爬山演算法
