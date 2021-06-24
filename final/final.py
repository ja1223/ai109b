import random
import sys

# 寫黑白棋遊戲的基本邏輯，棋子共'●','○'兩種
class Reversi():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.board = [[' ']*self.height for i in range(self.width)]
    
    # 初始化棋盤
    def iniBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j]=' '
        W, H = self.width//2 , self.height//2
        self.board[W-1][H-1]='●' # 預設棋盤中間4格的棋子
        self.board[W-1][H]='○'
        self.board[W][H-1]='○'
        self.board[W][H]='●'
        
    def drawBoard(self, hints = None) -> None: # 畫出棋盤
        HLINE =  ' ' * 3 + '----' * self.width  + ' ' # 橫的格線
        VLINE = (' ' * 3 +'|') *  (self.width +1) # 直的格線
        title = '     1'
        for i in range(1,self.width):
            title += ' ' * 3 +str(i+1)
        print(title) # title是棋盤上方的1234
        print(HLINE) # 畫出橫的格線
        for y in range(self.height): # 畫出棋子、合法棋步及直的格線
            print(y+1, end='  ')
            for x in range(self.width):
                if hints and [x,y] in hints: # 合法棋步
                    print(f'| √', end=' ')
                else:
                    print(f'| {self.board[x][y]}', end=' ') # 棋子
            print('|')
            print(HLINE) # 畫出橫的格線
    
    def isOnBoard(self, x, y): # 規定棋子可以放的範圍(棋盤大小)
        return 0 <= x < self.width and 0 <= y < self.height

    #檢查tile放在某個座標是否為合法棋步，如果是則回傳被翻轉的棋子
    def isValidMove(self, tile, xstart, ystart):
        if not self.isOnBoard(xstart, ystart) or self.board[xstart][ystart]!=' ':
            return [] # 如果 (xstart, ystart) 不在棋盤範圍內就回傳合法棋步為 []
        self.board[xstart][ystart] = tile # 暫時放置棋子
        otherTile = '○'  if tile == '●' else '●'
        tilesToFlip = [] # 合法棋步
        dirs = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]] # 定義八個方向
        for xdir, ydir in dirs:
            x, y = xstart+xdir, ystart+ydir
            while self.isOnBoard(x, y) and self.board[x][y] == otherTile:
                x += xdir
                y += ydir
                # 夾到對手的棋子了，回頭記錄被翻轉的對手棋子
                if self.isOnBoard(x, y) and self.board[x][y] == tile:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == xstart and y == ystart:
                            break
                        tilesToFlip.append([x, y])
                        
        self.board[xstart][ystart] = ' ' # 重設為空白
        return tilesToFlip

    # 若將tile放在xstart, ystart是合法行動，放置棋子
    # 回傳被翻轉的棋子(用來電腦算棋時可以把棋子翻回來)
    def makeMove(self, tile, xstart, ystart):
        tilesToFlip = self.isValidMove(tile, xstart, ystart)
        if tilesToFlip:
            self.board[xstart][ystart] = tile
            for x, y in tilesToFlip:
                self.board[x][y] = tile
        return tilesToFlip

    # 回傳現在盤面輪到tile走的所有合法棋步
    def getValidMoves(self, tile):
        return [[x, y] for x in range(self.width) for y in range(self.height) if self.isValidMove(tile, x, y)]
    
    # 計算當前比分
    def getScoreOfBoard(self)-> dict:
        scores = {'●':0, '○':0}
        for x in range(self.width): # 逐一檢查每一格的棋子顏色，如果是 ○ 就 ○ 加1分，反之就 ● 加1分
            for y in range(self.height):
                tile = self.board[x][y]
                if tile in scores:
                    scores[tile] += 1
        return scores
    # 計算當前比分(佔領的角落數量)
    def getScoreOfCorner(self)-> dict:
        scores = {'●':0, '○':0}
        if self.board[0][0] == '●':                         # 檢查左上角有沒有被 ● 佔領，有的話 ● 就加1分
            scores['●'] += 1
        if self.board[0][self.width-1] == '●':              # 檢查左下角有沒有被 ● 佔領，有的話 ● 就加1分
            scores['●'] += 1
        if self.board[self.width-1][0] == '●':              # 檢查右上角有沒有被 ● 佔領，有的話 ● 就加1分
            scores['●'] += 1
        if self.board[self.width-1][self.width-1] == '●':   # 檢查右下角有沒有被 ● 佔領，有的話 ● 就加1分
            scores['●'] += 1
        if self.board[0][0] == '○':                         # 檢查左上角有沒有被 ○ 佔領，有的話 ○ 就加1分
            scores['○'] += 1
        if self.board[0][self.width-1] == '○':              # 檢查左下角有沒有被 ○ 佔領，有的話 ○ 就加1分
            scores['○'] += 1
        if self.board[self.width-1][0] == '○':              # 檢查右上角有沒有被 ○ 佔領，有的話 ○ 就加1分
            scores['○'] += 1
        if self.board[self.width-1][self.width-1] == '○':   # 檢查右下角有沒有被 ○ 佔領，有的話 ○ 就加1分
            scores['○'] += 1
        return scores

# 電腦ai下棋的邏輯
class ReversiAI(Reversi):
    def __init__(self, board, height, width):
        super().__init__(height, width)
        self.board = board

    def isOnCorner(self, x, y):
        return x in {0, self.width-1} and y in {0, self.height-1}
 
    # 給定盤面board，回傳電腦的選擇
    def getComputerMove(self, computerTile):
        possibleMoves = self.getValidMoves(computerTile)
        random.shuffle(possibleMoves) # 隨機性
        
        # 若能占角為優先
        for x, y in possibleMoves:
            if self.isOnCorner(x, y):
                return [x, y]
            
        # 找能夠吃子最多的棋步
        bestScore, bestMove = -1, None
        for x, y in possibleMoves:
            flips = self.makeMove(computerTile, x, y)
            score = self.getScoreOfBoard()[computerTile]
            if score > bestScore:
                bestScore, bestMove = score, [x, y]
            # 還原棋盤
            self.board[x][y] = ' '
            otherTile = '○'  if computerTile == '●' else '●'
            for x, y in flips:
                self.board[x][y] = otherTile
        return bestMove


# 寫互動程式的邏輯
class Game(Reversi):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.turn = 'player'
        self.ai = ReversiAI(self.board,self.height, self.width)

    # 詢問玩家是否再玩一次
    def playAgain(self)-> bool:
        return input('你想再玩一次嗎?(輸入y或n)').lower().startswith('y')

    # 取得玩家的行動，回傳棋步[x, y](或'hints', 'quit'))
    def getPlayerMove(self, playerTile):
        DIGITS = [str(i) for i in range(1,10)]
        while True:
            move = input('請輸入棋步(先輸入x座標再輸入y座標)，例如11是左上角。(或輸入hints或quit)').lower()
            if move in {'quit', 'hints'}:
                return move
            if len(move) == 2 and move[0] in DIGITS and move[1] in DIGITS:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if self.isValidMove(playerTile, x, y):
                    break
            print('非合法棋步，請再試一次')
        return [x, y]

    # 顯示目前比分
    def showPoints(self, playerTile, computerTile):
        scores = self.getScoreOfBoard()
        print(f'You have {scores[playerTile]} points. The computer has {scores[computerTile]} points.')

    # 顯示目前比分(佔領的角落數量)
    def showPointsCorner(self, playerTile, computerTile):
        scores = self.getScoreOfCorner()
        print(f'You have {scores[playerTile]} points. The computer has {scores[computerTile]} points.')

    def gameloop(self,type):
        print("歡迎玩黑白棋(玩家的棋子為'●')")

        while True:
            # 初始化棋盤
            self.iniBoard()
            playerTile, computerTile = ['●', '○']
            showHints = False
            print('玩家先手' if self.turn == 'player' else '電腦先手')
            
            while True:
                playerValidMoves = self.getValidMoves(playerTile)
                computerValidMoves = self.getValidMoves(computerTile)
                # 若無人可行動，結束遊戲
                if not playerValidMoves and not computerValidMoves:
                    break
                if type == 2: # 在佔領角落模式時需額外檢查的結束遊戲條件
                    scoresC = self.getScoreOfCorner()
                    if scoresC['○'] >= 3 or scoresC['●'] >= 3:
                        break # 其中一方佔到三個角落就結束遊戲
                    elif scoresC['○'] == 2 and scoresC['●'] == 2:
                        break # 雙方各佔領2個角落(平手)就結束遊戲
                if self.turn == 'player' and playerValidMoves:
                    if showHints:
                        self.drawBoard(playerValidMoves)
                    else:
                        self.drawBoard()
                    if type == 1:
                        self.showPoints(playerTile, computerTile)
                    elif type == 2:
                        self.showPointsCorner(playerTile, computerTile)
                    move = self.getPlayerMove(playerTile)
                    if move == 'quit':
                        print('Thanks for playing!')
                        sys.exit() # terminate the program
                    elif move == 'hints':
                        showHints = not showHints
                        continue
                    else:
                        self.makeMove(playerTile, move[0], move[1])
                elif self.turn == 'computer' and computerValidMoves:
                    self.drawBoard()
                    if type == 1:
                        self.showPoints(playerTile, computerTile)
                    elif type == 2:
                        self.showPointsCorner(playerTile, computerTile)
                    input('按enter看電腦的下一步')
                    x, y = self.ai.getComputerMove(computerTile)
                    self.makeMove(computerTile, x, y)
                self.turn = 'player' if self.turn=='computer' else 'computer'
                        
            
            # 顯示最後結果
            self.drawBoard()
            if type == 1: # 正統黑白棋
                scores = self.getScoreOfBoard()
                print(f"X scored {scores['●']} points. ○ scored {scores['○']} points.")
                if scores[playerTile] > scores[computerTile]:
                    print("恭喜你贏電腦了")
                elif scores[playerTile] < scores[computerTile]:
                    print("你輸了")
                else:
                    print('平手')
            elif type == 2: # 佔領角落模式
                scores = self.getScoreOfCorner()
                print(f"X scored {scores['●']} points. ○ scored {scores['○']} points.")
                if scores[playerTile] > scores[computerTile]:
                    print("恭喜你贏電腦了")
                elif scores[playerTile] < scores[computerTile]:
                    print("你輸了")
                else:
                    print('平手')
                
            if not self.playAgain():
                break


size = int(input("請輸入想使用的棋盤大小:"))
type = int(input("請輸入想遊戲的方式:(正統黑白棋(輸入1)/占到最多角落獲勝(輸入2))"))
reversi = Game(size,size)
reversi.gameloop(type)