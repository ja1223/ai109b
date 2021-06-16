# 線性規劃
在數學中，線性規劃特指目標函數和約束條件皆為線性的最佳化問題。<br>
![](images/linearProgramming.png)
# 整數規劃
屬於線性規劃的一種。<br>
要求所有的未知量都為「整數」的線性規劃。<br>
# 圖形搜尋
圖形搜尋大致可以分為「深度優先搜尋 (Depth-First Search, DFS)、廣度優先搜尋 (Breath-First Search, BFS)、最佳優先搜尋 (Best-First Search, BestFS) 三類。
以下對此圖進行圖片搜尋<br>
![](images/graphSearch.jpg)
## 深度優先搜尋
往尚未訪問過的第一個鄰居節點走去。<br>
![](images/dfs.jpg)
紅色字為搜尋的順序<br>
## 廣度優先搜尋
從一個節點開始，將每個鄰居節點都一層一層的拜訪下去，深度最淺的節點會優先被拜訪的方式。<br>
![](images/bfs.jpg)
紅色字為搜尋的順序<br>
## 圖形搜尋的程式實作
利用[graph_search.py](03-02-search/graph_search.py)來進行圖形搜尋。<br>
執行結果:<br>
```
C:\Users\user\Desktop\ai\ai109b\0318\03-02-search>python graph_search.py
dfs:1 => 2 => 3 => 4 => 5 => 6 => 
bfs:1 => 2 => 5 => 3 => 4 => 6 => 
```
## 拼圖問題
將一個已經移動打亂過的拼盤，想辦法移動回原本樣子的問題。<br>
![](images/puzzle.jpg)
上圖為[puzzleSearch.py](03-03-puzzle/puzzleSearch.py)程式中的拼圖問題。<br>
在程式中用一個 3*3 的陣列來代表拼盤，並用 0 來代表空格，因此 2 移動到空格，其實是將 0 與 2 兩個數字位置交換。<br>
執行結果(呈現方式是將最後結果放在最前面，剛開始的拼盤放在最後面):<br>
```
C:\Users\user\Desktop\ai\ai109b\0318\03-03-puzzle>python puzzleSearch.py
bfs:found= True
======= backtrace =========
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]

[1, 0, 3]
[8, 2, 4]
[7, 6, 5]

[1, 3, 0]
[8, 2, 4]
[7, 6, 5]

[1, 3, 4]
[8, 2, 0]
[7, 6, 5]

[1, 3, 4]
[8, 2, 5]
[7, 6, 0]

[1, 3, 4]
[8, 2, 5]
[7, 0, 6]
```
