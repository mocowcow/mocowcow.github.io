---
layout      : single
title       : LeetCode 3419. Minimize the Maximum Edge Weight of Graph
tags        : LeetCode Medium Graph BinarySearch
---
weekly contest 432。  
這題也是很妙，卡了我快一小時，差點沒做出來。  

## 題目

輸入兩個整數 n 和 threshold，有個 n 節點的有向權重圖，邊號分別從 0 到 n - 1。  
輸入二維整數陣列 edges，其中 edges[i] = [A <sub>i</sub>, B <sub>i</sub>, W <sub>i</sub>] 代表 A <sub>i</sub> 到 B <sub>i</sub> 的路徑，其權重為 W <sub>i</sub>。  

你可以刪除任意路徑 (也可能不刪除)，使得此圖滿足以下條件：  

- 任意節點出發都可抵達節點 0。  
- 剩餘邊的**最大**邊權要盡可能小。  
- 每個節點**至多** threshold 條**出邊**。  

求刪除必要的邊之後，**最大邊權**的**最小值**。  
若無法滿足條件，則回傳 -1。  

## 解法

看到關鍵字**最大值最小化**，大概就可以往**二分答案**去思考。  
若最大邊權 x 可以滿足條件，那麼 x+1 也可以；反之，若 x 不行，則 x-1 也不行。  

---

每個點都要可達 0，最暴力的方法是從每個點出發 dfs 一次，複雜度 O(N^2)。  
但是反向思考，從 0 出發把有向邊**反向**著 dfs，判斷是否能抵達所有節點，更有效率。  

---

最後的問題在於這個 threshold，我想了很久，一直想不出在多條邊的情況下，怎麼判斷走誰最好。  
例如：  
> n = 3, threshold = 1  
> edges = [1,0], [2,1], [2,0]  

很明顯 [2,1] 是多餘的，但是沒有直觀的方法判斷，似乎只能暴力枚舉刪或不刪。  

---

但仔細想想，實際上 dfs 的時候，每個點**至多訪問一次**。  
我們是**反向**走，所以每個節點的**出邊**同樣至多只需要一條。  
因此 threshold 不管多少都無所謂，與 threshold = 1 並無差異，可以直接忽略。  

定義 ok(limit)，反向 dfs 邊權小於等於 limit 的邊，判斷所有節點是否抵達。  
進行二分即可。  

時間複雜度 O()。  
空間複雜度 O()。  

```python
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[b].append([a, w])

        def ok(limit):
            vis = [False] * n
            def dfs(i):
                vis[i] = True
                for j, w in g[i]:
                    if not vis[j] and w <= limit:
                        dfs(j)
            dfs(0)
            return all(vis)

        lo = 1
        hi = 10 ** 6
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid

        if not ok(lo):
            return -1

        return lo
```
