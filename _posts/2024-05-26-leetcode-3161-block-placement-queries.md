---
layout      : single
title       : LeetCode 3161. Block Placement Queries
tags        : LeetCode Hard Array SortedList BinarySearch SegmentTree BIT
---
雙周賽 131。好久不見的線段樹，調了半天沒調出來。賽後看到不同思路，照做就馬上秒了，原方法真的事倍功半。  

## 題目

有一個無限的數軸，原點為 0，朝 x 軸的正向延伸。  

輸入二維整數陣列 queries，由兩種操作組成：  

- 操作一，queries[i] = [1, x]：  
    在離原點距離 x 處放置一個路障。保證查詢當下 x 沒有障礙物。  

- 操作二，queries[i] = [2, x, sz]：  
    判斷在區間 [0, x] 內能否放得下寬度為 sz 的方塊。  
    若有障礙物和方塊重疊，則無法放置。但方塊的邊界可以和障礙物接觸。  
    注意：此操作只有查詢，並**不需放置**。  

回傳布林陣列 results，其中 results[i] 代表第 i 次操作二的查詢結果，若能放置為 true，否則為 false。  

## 解法

雖然說是無限延伸的數軸，實際上有給定最大值 min(5 \*10^4, 3\* queries.length)，以下記做 MX。  

本題的障礙物**只多不少**。每次放置新的障礙後，會與左右兩邊的障礙物各自形成一個區間 (如果有的話)。  
方便起見，設左邊界 0，右邊界為 R = MX + 5。想像 0 和 R 的位置都有障礙物，最初障礙物座標為 [0,R]  
例如在 x 點插入障礙，座標變成 [0,x,R]，並且分割成成 [0, x] 和 [x, R] 兩段區間。  

我們要求這些區間的的最大值，但是加入障礙物之後，區間大小只減不增，不太好處理。  

---

正難則反，試試逆向思維。  
先把所有障礙物加上去，倒敘處理查詢，操作一變成刪除障礙，區間大小就**只增不減**，這樣要維護最大值就方便了。  

假設最終的障礙物座標為 [0,7,10]，有大小為 7-0 和 10-7 的兩段區間。  
移除座標 7 的障礙，座標變成 [0,10]。而新的區間是由原本 7 左右的兩個障礙組成，也就是 10-0。  
為了有效率地查找、刪除障礙物座標，需要使用**有序容器**並搭配二分搜，並以新區間的右端點紀錄區間大小。  

再來看操作二的查詢。同樣以 [0,7,10] 為例，如果 x = 10，我們需要找到不超過 x 的最大障礙座標，剛好是 10。  
而 10 可以和他前一個障礙物 7 組成 10-7 的區間。  
這樣看來 x = 10, sz = 7 好像放不下，但其實可以拿 7 當作右端點，放在 7-0 這個位置。  
小於等於 x 的障礙物都可以當作右端點，也就是說，需要在 [0, x] 查詢**區間最大值**。  

注意有時候 x 可能沒有障礙物，除了 [0, x] 的段的區間最大值之外，x 和其左方的障礙物 prev 也可以組成一個區間 [prev, x]。  

---

障礙座標需要有序隨機存取，使用 sorted list。  
障礙區間大小需要單點修改，區間查詢，使用線段樹。但因為本題查詢左邊界都是 0，也可以用 BIT。  

最後別忘答案還要反轉一次。  

時間複雜度 O(Q log MX)，其中 MX = x 和 sz 的最大值。  
空間複雜度 O(MX)。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        Q = len(queries)
        MX = min(5 * (10**4), Q * 3) + 5
        sl = SL() # obstacle pos
        sl.add(0) # sential
        sl.add(MX) # sential
        for q in queries: # init obstacles
            if q[0] == 1:
                sl.add(q[1])
        
        seg = SegmentTree(MX) # init interval with adjacent obstacles
        for x, y in pairwise(sl):
            sz = y - x 
            seg.update(1, 0, MX - 1, y, sz)
            
        ans = []
        for q in reversed(queries):
            typ, x = q[0], q[1]
            if typ == 1: 
                # remove obstacle
                idx = sl.bisect_left(x)
                prev, next = sl[idx - 1], sl[idx + 1]
                sl.remove(x)
                
                # merge 2 intervals
                # [prev, x, next] becomes [prev, next]
                sz = next - prev 
                seg.update(1, 0, MX - 1, next, sz)
                continue

            # typ 2
            sz = q[2]
            idx = sl.bisect_right(x)
            prev = sl[idx - 1]
            res = seg.query(1, 0, MX - 1, 0, prev)
            ans.append(res >= sz or (x - prev) >= sz)
            
        return reversed(ans)


class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)

    def build(self, init, id, L, R):
        """
        初始化線段樹
        若無初始值則不需執行
        """
        if L == R:  # 到達葉節點
            self.tree[id] = init[L]
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return max(a, b)

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        res = 0
        M = (L+R)//2
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, val):
        """
        單點更新
        對索引i增加val
        """
        if L == R:  # 當前區間目標範圍包含
            self.tree[id] = val
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, val)
        else:
            self.update(id*2+1, M+1, R, i, val)
        self.push_up(id)
```
