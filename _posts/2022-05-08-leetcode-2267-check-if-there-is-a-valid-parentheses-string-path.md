--- 
layout      : single
title       : LeetCode 2267. Check if There Is a Valid Parentheses String Path
tags        : LeetCode Hard Array Matrix BFS DFS
---
周賽292。終於久違的又四題AK了，只是這次網站有點問題，搞不好不會計分，好難受。

# 題目
一個**括號字串**是一個非空且只包含'('和')'的字串。如果滿足下列任一條件，則這個括號字串就是**合法**的：  
- 字串是()  
- 字串可以表示為AB，代表A連接B，且A和B都是合法括號字串  
- 字串可以表示為(A)，且A是合法括號字串  

輸入M*N的括號矩陣grid。一個**合法的括號路徑**必須滿足以下條件：  
- 開始於最左上角(0,0)  
- 結束於最右下角(M-1,N-1)  
- 每次只會往右或是往下方移動  
- 路徑經過的格子所組成的括號字串是**合法**的  

如果grid中存在任何**合法括號路徑**，回傳true，否則回傳false。

# 解法
老實說第一段的合法括號解釋有點臭長，我直接跳過不管，看圖例就懂了。  
簡單講是要從左上角出發，走到右下角，途中經過的括號字串要能夠成功對上。  

一開始沒注意到只能往右或往下，想說這樣好像很難判斷哪些格子能不能走，浪費一些時間。  
重新看過題目，恍然大悟，不會出現回頭路就很簡單了，只要維護左括號的數量，直接dfs走到底就好。  

dfs寫好交出去，這垃圾網站伺服器掛掉，提交的時候只給我TLE，但是沒給測資，想說該不會dfs不行，就改用bfs去。  
結果還是TLE，仔細想想，可能是不同的路線抵達同樣位置，且擁有同樣的括號數量，造成多次重複計算，最後加set去重複就過了。

重點在於檢查路上的括號字串是否合法：左括號一定要先出現，才能配上右括號。  
我們維護變數left代表左括號的數量，每碰到左括號則+1，右括號則-1，如果left值哪天小於0，代表不合法，拋棄此路徑。  
最後抵達右下角時，還要再檢查一次是否每個左括號都有被關起來，此時left應為0。

```python
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])

        visited=set()
        q = deque([(0, 0, 0)])
        while q:
            r, c, left = q.popleft()
            if not (0 <= r < M and 0 <= c < N):
                continue
            if grid[r][c] == '(':
                left += 1
            else:
                left -= 1
                if left < 0:
                    continue
            if r == M-1 and c == N-1 and left == 0:
                return True
            if (r,c,left) not in visited:
                visited.add((r, c, left))
                q.append((r+1, c, left))
                q.append((r, c+1, left))

        return False
```

再寫一次dfs，2008ms，可能因為少走很多冤枉路，比上面的6781ms快了不少。

```python
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        visited=set()
        
        def dfs(r,c,left):
            if not (r<M and c<N) or (r,c,left) in visited:
                return False
            visited.add((r,c,left))
            if grid[r][c]=='(':
                left+=1
            else:
                left-=1
            if left<0:
                return False
            if r==M-1 and c==N-1 and left==0:
                return True
            return dfs(r+1,c,left) or dfs(r,c+1,left)
        
        return dfs(0,0,0)
```