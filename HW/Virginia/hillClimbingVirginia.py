from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionVirginia import SolutionVirginia # 引入平方根解答類別

# 執行爬山演算法 (開始尋找, 最多十萬代、失敗一千次就跳出。
hillClimbing(SolutionVirginia(), 100000, 1000)
