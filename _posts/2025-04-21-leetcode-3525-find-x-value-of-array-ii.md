---
layout      : single
title       : LeetCode 3525. Find X Value of Array II
tags        : LeetCode Hard Math SegmentTree
---
weekly contest 446。  
出題者正常發揮，描述的依舊很爛，一直在不重要的細節鑽牛角尖。  

## 題目

<https://leetcode.com/problems/find-x-value-of-array-ii/description/>

## 解法

和 Q3 差別在由詢問指定刪除前綴 nums[..start-1]，我們只能刪後綴。  
相當於求左端點為 start、右端點為 [start..N-1] 的子陣列，有幾個滿足 prod % k = x。  

注意：每次查詢前會先修改 nums[idx] = val，並持續影響接下來的查詢。  

---

我們需要單點修改、區間查詢乘積，可以用**線段樹**維護。  

那要怎麼求左端點為 start 的子陣列乘積個數？  
答案也是**線段樹**。個人覺得不太好想，可能因為我做過的線段樹題比較少。  

設區間 [L,R] 維護 nums[L..R] 的乘積，以及左端點為 L 的子陣列乘積個數 cnt。  
已知兩個更小的區間 data1 = [L,M], data2 = [M+1,R]，如何合併兩者得到 [L,R]？  

prod 很簡單，即 data1.prod \* data2.prod。  

cnt 就比較麻煩一點。  
data1 包含的子陣列左端點已經都是 L，可直接沿用。  
data2 包含的子陣列左端點是 M+1 ，需要在左邊加上 nums[L..M] 這段，才能夠轉成由 L 開頭。  
所以要將 data2.cnt 中每個餘數乘上 [L,M] 的乘積 (即 data1.prod) 後再進行合併。  

---

主要難度在線段樹的實作，可將合併邏輯提取成函數 merge_data() 會比較好維護。  

時間複雜度 O(k \* (N + Q) log N)。  
空間複雜度 O(Nk)。  

```python
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        N = len(nums)
        seg = SegmentTree(N, k)
        seg.build(nums, 1, 0, N-1)

        ans = []
        for idx, val, start, x in queries:
            seg.update(1, 0, N-1, idx, val)
            _, cnt = seg.query(1, 0, N-1, start, N-1)
            ans.append(cnt[x])

        return ans


class SegmentTree:

    def __init__(self, n, k):
        self.tree = [0]*(n*4)
        self.k = k

    def new_data(self, val):
        x = val % self.k
        cnt = [0] * self.k
        cnt[x] = 1
        return [x, cnt]  # prod, cnt sub

    def merge_data(self, data1, data2):
        if data1 is None:
            return data2
        prod1, cnt1 = data1
        prod2, cnt2 = data2
        new_prod = prod1 * prod2
        new_cnt = cnt1.copy()
        for x in range(self.k):
            new_cnt[x*prod1 % self.k] += cnt2[x]
        return [new_prod, new_cnt]

    def build(self, init, id, L, R):
        """
        初始化線段樹
        若無初始值則不需執行
        """
        if L == R:  # 到達葉節點
            self.tree[id] = self.new_data(init[L])
            return
        M = (L+R)//2
        self.build(init, id*2, L, M)
        self.build(init, id*2+1, M+1, R)
        self.push_up(id)

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.merge_data(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        M = (L+R)//2
        res = None
        if i <= M:
            res = self.query(id*2, L, M, i, j)
        if M+1 <= j:
            res = self.merge_data(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, val):
        """
        單點更新
        對索引 i 改成val
        """
        if L == R:  # 當前區間目標範圍包含
            self.tree[id] = self.new_data(val)
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i, val)
        else:
            self.update(id*2+1, M+1, R, i, val)
        self.push_up(id)
```
