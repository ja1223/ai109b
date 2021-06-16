def truthTable(n): # 主函數
	p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
	return tableNext(n, p) # 呼叫 tableNext 遞迴下去排出所有可能

def tableNext(n, p):# n : n個變數的真值表, p :代表已經排下去的
	i = len(p)
	if i == n:  # 全部排好了
		print(p)  # 印出排列
		return
	binary=[0,1]  # 二進位只有0跟1
	for x in binary:
		p.append(x)     # 把 x 放進表
		#print("append:",p)
		tableNext(n, p) # 繼續遞迴尋找下一個排列
		p.pop()         # 把 x 移出表
		#print("pop:",p)
	

#truthTable(2)
truthTable(3)
