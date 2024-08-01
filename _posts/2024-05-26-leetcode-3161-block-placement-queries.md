---
layout      : single
title       : LeetCode 3161. Block Placement Queries
tags        : LeetCode Hard Array SortedList BinarySearch SegmentTree BIT
---
雙周賽 131。好久不見的線段樹，調了半天沒調出來。賽後看別人題解才發現想錯了。  

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
方便起見，設左邊界 0，右邊界為 R = MX + 5。想像 0 和 R 的位置都有障礙物，最初障礙物索引有 [0,R]  
例如在 x 點插入障礙，索引變成 [0,x,R]，並且分割成成 [0,x] 和 [x,R] 兩段區間。  

操作一需要有序插入、還要查詢相鄰的障礙物索引，需要使用有序容器 sorted list，並搭配二分搜。  
每次操作直接在 x 新增障礙即可。  

---

再來看操作二。  

以 [0,1,7,10] 為例：  
> 給定 x = 8, sz = 6  
> 可用**完整的區間**只有 [0,1], [1,7] 兩段  
> 可用的**不完整區間**有 [7,8] 這段  
> sz = 6 可以放在 [1,7] 這段  

所有處於查詢範圍 [0,x] 之內的障礙物，都可做為**右端點**提供完整的區間。  
若索引 x 沒有障礙，則可和**小於等於 x** 的第一個障礙物 prev 提供 [prev,x] 的不完整區間。  

只有在右端點被包含時才能提供完整區間，故以右端點做鍵值儲存區間長度。  
同時還要支援 [0, x] 的區間最大值查詢，這邊選用**線段樹**。  
每次操作先找出 prev，判斷 x-prev 或 [0, x] 的區間最大值是否滿足 sz。  

時間複雜度 O(Q log MX)，其中 MX = x 和 sz 的最大值。  
空間複雜度 O(MX)，答案空間不計入。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        Q = len(queries)
        MX = min(5 * (10**4), Q * 3) + 5
        
        sl = SL([0, MX]) # obstacle pos with sentinel
        seg = SegmentTree(MX) # maintain interval size
        ans = []
        for q in queries:
            typ, x = q[0], q[1]
            idx = sl.bisect_right(x)
            prev = sl[idx - 1] 
            if typ == 1: 
                next = sl[idx]
                # insert obstacle
                sl.add(x)
                # update interval size
                # [prev, next] becomes [prev, x, next]
                seg.update(1, 0, MX - 1, next, next - x) # [x, next]
                seg.update(1, 0, MX - 1, x, x - prev) # [prev, x]
            else: # typ 2
                sz = q[2]
                res = seg.query(1, 0, MX - 1, 0, prev) 
                # max interval between [0, prev]
                # or [prev, x]
                ans.append(res >= sz or (x - prev) >= sz)
            
        return ans


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
        return a if a > b else b

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

另一種思路是逆向操作，倒序處理查詢。  
先把所有障礙物加上去，然後慢慢刪除障礙。  
區間長度變成**只增不減**，而且本題剛好**只查詢前綴**，資料結構可以改用更有效率的 BIT。  

操作一改成刪除後，會將 x 前後的兩個區間合併成更大的區間。  
以 [0,1,7,10] 為例：
> x = 7  
> 刪除 7 之後剩下 [0,1,10]  
> [1,7],[7,10] 兩個區間合併成新的區間 [1,10]  
> 以 10 為鍵值更新區間大小為 9  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        Q = len(queries)
        MX = min(5 * (10**4), Q * 3) + 5
        
        # init obstacle and interval
        sl = SL([0, MX]) # obstacle pos with sentinel
        bit = BIT(MX) # maintain interval size
        for q in queries:
            if q[0] == 1:
                sl.add(q[1])
                
        for x, y in pairwise(sl):
            sz = y - x 
            bit.update(y, sz)
        
        ans = []
        for q in reversed(queries):
            typ, x = q[0], q[1]
            if typ == 1: 
                # update interval size
                # [prev, x, next] becomes [prev, next]
                idx = sl.bisect_left(x)
                prev, next = sl[idx - 1], sl[idx + 1]
                sl.remove(x)
                bit.update(next, next - prev)
            else: # typ 2
                sz = q[2]
                idx = sl.bisect_right(x)
                prev = sl[idx - 1] 
                res = bit.query(prev) 
                # max interval between [0, prev]
                # or [prev, x]
                ans.append(res >= sz or (x - prev) >= sz)
            
        return reversed(ans)

    
class BIT:
    """
    tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
    offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
    注意：只能查前綴極值。若求max則tree[i]值只能增、不能減。
    """

    def __init__(self, n, offset=1):
        self.offset = offset
        self.tree = [-inf]*(n+offset)

    def update(self, pos, val):
        """
        將tree[pos]設成val
        """
        i = pos+self.offset
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)

    def query(self, pos):
        """
        查詢[1, pos]的max
        """
        i = pos+self.offset
        res = -inf
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & (-i)
        return res
```
