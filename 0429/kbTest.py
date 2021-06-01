
from kb import KB

# 在主程式中直接寫知識庫
code = "A<=B. B<=C&D. C<=E. D<=F. E. F. Z<=C&D&G."
kb1 = KB()
kb1.load(code) # 載入知識庫
kb1.forwardChaining() # 開始進行前向推論
