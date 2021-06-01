from hillClimbing import hillClimbing # 引入解答類別
from solution import Solution
import random


class SolutionVirginia(Solution):
    def neighbor(self): # 單變數解答的鄰居函數。
        key1 = self.v.copy()
        len = key1.length
        i = random.randrange(0, len)
        key1[i] = random.randint(0, 255)
        return SolutionVirginia(key1) # 建立新解答並傳回。

    def height(self):               # 能量函數
        key1 = self.v
        # 比對文章，看看出現多少次常用字，這就是分數
        score = fit(key, text)
        return score

    def str(self): # 將解答轉為字串，以供印出觀察。
        return "key={} score={}".format(self.v, self.height())
