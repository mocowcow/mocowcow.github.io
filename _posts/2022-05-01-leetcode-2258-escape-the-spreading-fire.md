--- 
layout      : single
title       : LeetCode 2258. Escape the Spreading Fire
tags        : LeetCode Hard Array Matrix BFS BinarySearch
---
雙周賽77。堪稱最近幾次Q4中最難的，排行榜前50名的人七成都噴過WA。  
本來還以為我算擅長二分搜，結果兩次Q4碰到二分搜都沒有察覺，敏銳度有待加強。  

# 題目
輸入M*N的矩陣grid，其中0代表草地，1代表火，2代表牆壁。  
你從左上角(0,0)出發，要逃到最右下角(M-1,N-1)的安全屋。
每1分鐘，你可以移動到相鄰的一格。隨後，所有火源會向四周蔓延一格。  
求你最多可以在起點發呆幾分鐘，且還能成功逃到安全屋。如果不可能抵達安全屋，則回傳-1；若發呆多久都是安全的，則回傳10^9。  

注意：如果你先進入安全屋後，火勢隨即蔓延過來，也算做安全抵達；若在草地上，被火碰到則算死亡。  
**\*題目沒說清楚**：安全屋會起火。你還沒進入安全屋，但是安全屋先起火，之後就不能再進入了。

# 解法
安全屋會起火！  
安全屋會起火！
安全屋會起火！
因為很重要所以說三次。大概很多人都是被這個害死。  
本來以為安全屋是完全防火，所以牆壁和安全屋形成死角包覆火源的話，可以從另一個方向進入是其實是不行，只通過51/55測資。  

當時我是維護火源和人的位置，每經過一回合各向外擴散一次。若起點還沒起火，加入一個延遲為t的人，不同延遲的人擁有各自的set來確保不走回頭路，但是全部人共用一個火源。就算誤解安全屋的起火設定，碰到最大測資也不一定會AC就是。  

後來看看別人解法，清一色都是二分搜。仔細想想，說不定**保證安全的10^9**就是二分搜的提示？而且若能成功發呆X分鐘，則小於X的時間也都一定是安全的，完全就是函數型二分搜。  

知道概念就很簡單了，只是寫起來一大串，還是很累人。  
若完全無法活著逃出，需回傳-1，先暫定下界為-1。上界就設10^9，反正m\*n<=2\*10^4，再怎樣也不可能發呆這麼久也被燒到。  
考慮縮減到下界-1，上界0的情況，如果取左中位數的話mid會變成-1，無法正確計算，所以改取右中位數。

再來寫用計算是否可以安全逃出的函數canDo(delay)。
初始化地圖、火和人的佇列，若佇列中還有活人，則重複BFS：  
1. 大部分情況下，火和人不能同時存在，因此先讓火擴散  
2. 火若停止擴散，則將人的發呆時間歸0，節省計算次數(不然可能要減10^9次)  
3. 若尚有發呆時間則不動作，否則有三種狀況：
   當前為安全屋，先進屋才被燒算safe，所以碰到安全屋直接回傳true  
   不在安全屋卻被燒，此位置不處理  
   不在安全屋但沒被燒，向四周走一格  
4. 最後檢查安全屋是否起火，若起火直接回傳false，反正以後都進不去了  

佇列中的人走完全部可行路徑，但是也沒被燒死，這種情況就是沒有火的死路，也回傳false。


```python
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        fires = []
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fires.append((r, c))

        def canDo(delay):
            g = []
            for row in grid:
                g.append(row[:])
            q = deque([(0, 0)])
            visited = set()
            f = deque(fires)
            while q:
                # fire go
                for _ in range(len(f)):
                    r, c = f.popleft()
                    g[r][c] = 1
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if (0 <= nr < M and 0 <= nc < N) and g[nr][nc] == 0:
                            f.append((nr, nc))
                if not f:
                    delay=0
                # ppl go
                if delay > 0:
                    delay -= 1
                else:
                    for _ in range(len(q)):
                        r, c = q.popleft()
                        if r == M-1 and c == N-1:
                            return True
                        if g[r][c] == 1:  # got fired
                            continue
                        visited.add((r, c))
                        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                            if (0 <= nr < M and 0 <= nc < N) and g[nr][nc] == 0 and (nr, nc) not in visited:
                                q.append((nr, nc))

                if g[-1][-1] == 1:
                    break
            return False

        lo = -1
        hi = 10**9
        while lo < hi:
            mid = (lo+hi+1)//2
            if not canDo(mid):
                hi = mid-1
            else:
                lo = mid

        return lo 
```
