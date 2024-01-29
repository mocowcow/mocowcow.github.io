---
layout      : single
title       : LeetCode 3015. Count the Number of Houses at a Certain Distance I
tags        : LeetCode Medium Array Graph BFS PrefixSum
---
周賽381。

## 題目

輸入三個正整數 n, x 和 y。  

城市中，有 n 棟房子，編號分別從 1\~n，且有 n 條道路連接房子。  
對於滿足 1 <= i <= n - 1 的所有房子 i，都存在一條道路連接第 i 和第 i+1 棟房子。  
剩下最後一條道路是連接第 x 和第 y 棟房子。  

對於所有滿足 1 <= k <= n 的整數 k，你必須找到存在幾組房子(house1, house2)，從 house1 出發到 house2 所經過的最小道路數正好為 k。  

回傳長度 n，且索引從 1 開始的陣列 result，其中 result[k] 代表有多少組房子的最小街道數為 k。  

注意：x, y 可能相等。  

## 解法

從 1 開始數真的很煩。總之先把所有點減 1，把範圍調整成 [0, n-1]。  

其實一組房子所需經的**最小道路數**，就是兩點之間的**最短距離**，每條道路的距離都是 1。  
然後還要求任意兩點的最短距離，基本上就知道可以用 Floyd-Warshall 了。  

按照題意，依照每條道路建立雙向且距離為 1 的邊。  
執行 Floyd-Warshall，再枚舉所有組合，統計最短距離的出現頻率即可。  

時間複雜度 O(n^3)。  
空間複雜度 O(n^2)。  

```python
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = x-1, y-1
        fw = FloydWarshall(n)
        for i in range(1, n):
            fw.add(i, i-1, 1)
            fw.add(i-1, i, 1)
            
        fw.add(x, y, 1)
        fw.add(y, x, 1)
        fw.build()
       
        ans = [0]*n
        a = fw.dp
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                k = a[i][j]
                ans[k-1] += 1
                
        return ans
        
class FloydWarshall:
    def __init__(self, n):
        self.n = n
        self.dp = [[inf]*n for _ in range(n)]
        for i in range(n):
            self.dp[i][i] = 0

    def add(self, a, b, c):
        if c < self.dp[a][b]:
            self.dp[a][b] = c

    def get(self, a, b):
        return self.dp[a][b]

    def build(self):
        for k in range(self.n):
            for i in range(self.n):
                if self.dp[i][k] == inf:  # pruning
                    continue
                for j in range(self.n):
                    new_dist = self.dp[i][k]+self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist
```

直接枚舉出發點做 bfs 也可以，不管是時間還是空間都大有改善。  

時間複雜度 O(n^2)。  
空間複雜度 O(n)。  

```python
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = x-1, y-1
        g = [[] for _ in range(n)]
        g[x].append(y)
        g[y].append(x)
        for i in range(1, n):
            g[i].append(i-1)
            g[i-1].append(i)
         
        ans = [0]*n
        for i0 in range(n):
            # bfs from i0
            vis = [False]*n
            vis[i0] = True
            q = deque()
            q.append(i0)
            dist = 0
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    for j in g[i]:
                        if vis[j]:
                            continue
                        vis[j] = True
                        ans[dist] += 1
                        q.append(j)
                dist += 1
            
        return ans
```

n 的範圍高達 10^5 就很難辦了。  
先想想不存在 xy 這條額外路徑的話，要怎麼算距離貢獻？  

對於出發點 i 來說，他的左邊點有 [0, 1,.. i-2, i-1]，右邊點有 [i+1, i+2,.. n-2, n-1]：  

- 從 i 走到左邊點的距離分別是 1, 2,.. i-1, i  
- 從 i 走到右邊點的距離分別是 1, 2,.. n-2-i, n-1-i  

可以發現，如果 i 左邊有 cnt 個點，那麼對於 [1, cnt] 之間的所有距離都會貢獻一次；右邊同理。  
如此只需要支援**區間修改**的資料結構，枚舉出發點 i，就可以快速算出 i 對於其他點 j 的貢獻。  

我們只需要在所有修改結束後查詢總貢獻，因此**差分**是最佳選擇。  
每次計算貢獻是 O(1)，共 n 次，最後對差分做**前綴和**得出答案，複雜度 O(n)。  

---

加入一條額外的道路 xy，在某些情況下可以當作**捷徑**，把原先的路徑變得更短。  
那麼如何決定**何時該走捷徑 xy**？  

我看了好多篇題解，都不是很好懂，最後找到兩邊比較能夠看懂的：  

- <https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii/solutions/2613400/xiao-yang-xiao-en-dui-cheng-qing-kuang-d-i72g/>  
- <https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii/solutions/2619411/dui-xiao-yang-xiao-en-ti-jie-de-yi-xie-b-2rjp/>  

總之幾個關鍵重點：  

1. **對稱性**。(i, j) 和 (j, i) 是等價的：  
    在保證 i < j 的限制下，枚舉 i，並計算移動到右方 j 的最短距離，將答案乘 2 即可  
2. 還是對稱性。(x, y) 和 (y, x) 也是等價的：限制 x <= y  
3. xy 這條額外道路，用或不用的決策具有**單調性**：  
    若某個 (i, j)，走 (i, x, y, j) 比起 (i, j) 還要短，在 i 不變的情況下，(i, j+1) 肯定也是走 xy 更短  
    也就是說對於 i 右方的所有點 j，左半邊**不走捷徑**、右半邊要**走捷徑**  

---

我們限制了 i < j 且 x <= y，所以會有以下幾種可能的排列方式：  

- x y i j  
- x i y j  
- x i j y  
- i j x y  
- i x j y  
- i x y j  

這些排列隨便看看就好，不太重要。  
反正就是，使用 xy 做為捷徑，則路徑會經過 (i, x, y, j) 四個點，距離是 abs(i-x) + 1 + abs(y-j)。  
如果直接走 (i, y) 的距離比起 (i, x, y) 相同或更短，那**捷徑根本沒用**。  
對於某個 i 來說：  

- 如果**捷徑沒用**，直接按照上面講的差分做法，計算從 i 走到 [i+1, n-1] 所有點的貢獻。  
- 否則根據剛才提到的**單調性**，在某個**分界點**的左方都不走捷徑、右方都要走捷徑  

---

將分界點記做 sep。  
走捷徑 (i, x, y) 的距離 abs(i-x) + 1 記做 ixy_cost。  

在 sep 的左邊(含sep)都不走捷徑，直接從 i 走過來。距離公式 i - sep。  
在 sep 的右邊(不含sep)都走捷徑。距離公式 ixy_cost + (y - sep)。  

求**不走捷徑**小於等於**走捷徑**的分界點：  
> i - sep <= ixy_cost + (y - sep)  
> 2\*sep <= d + y + i  
> sep <= (ixy_cost + y + i) / 2  

介於 [i+1, sep] 區間的所有點 j，都不需要捷徑，可以直接抵達；其餘都要走捷徑 xy。  

從 sep+1 開始的點，分別位於捷徑出口 y 的左右兩方。基本的距離成本為**ixy_cost**。  
介於 [sep+1, y] 區間的所有點 j，都是走 ixy 之後**從 y 向左**走；  
反之，介於 [y+1, n-1] 區間的所有點 j，都是走 ixy 之後**從 y 向右**走。  

將這三段分別計算，大功告成。  

時間複雜度 O(n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = x - 1, y - 1
        if x > y:
            x, y = y, x
        
        diff = [0] * (n + 1)
        def add(s, e): # add every element between [s, e] by two
            diff[s] += 2
            diff[e + 1] -= 2
            
        for i in range(n):
            ixy_cost = abs(i - x) + 1 # i to x to y
            if ixy_cost >= abs(i - y): # no need path xy
                # go directly from i to j
                # for all j between [i + 1, n - 1] 
                # distance contribution range is [1, n - 1 - i]
                add(1, n - 1 - i)
                
            else: # sometimes need path xy
                # find the critical point "sep"
                # where directly move to y cost lesser than path xy
                # (i - sep) <= d + (y - sep)
                # 2sep <= d + y + i
                sep = (ixy_cost + y + i) // 2
                
                # case 1: no need path xy   
                # go directly from i to j
                # for all j between [i + 1, sep]    
                # distance contribution range is [1, sep - i]
                add(1, sep - i)            
                
                # case 2: use path xy to y, then go leftside from y
                # for all j between [sep + 1, y - 1]
                # distance contribution range is [1, y - (sep + 1)], plus ixy_cost
                add(ixy_cost + 1, ixy_cost + y - (sep + 1))
                
                # case 3: use path xy to y, then go rightside from y
                # for all j between [y, n - 1]
                # distance contribution range is [0, n - 1 - y], plus ixy_cost
                add(ixy_cost, ixy_cost + n - 1 - y)
                
        ps = list(accumulate(diff))
        return ps[1:]
```
