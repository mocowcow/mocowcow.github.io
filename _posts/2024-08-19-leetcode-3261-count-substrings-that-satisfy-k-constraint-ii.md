---
layout      : single
title       : LeetCode 3261. Count Substrings That Satisfy K-Constraint II
tags        : LeetCode Hard String SlidingWindow TwoPointers SegmentTree
---
weekly contest 411。  

## 題目

輸入**二進位**字串 s，以及整數 k。  

若一個二進位字串滿足以下**任一**條件，則稱其 **k 約束**。  

- 字串中最多 k 個 0。  
- 字串中最多 k 個 1。  

求 s 有幾個 **k 約束** 子字串。  

另外輸入二維整數陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

回傳整數陣列 answer，其中 answer[i] 代表 s[l<sub>i</sub>..r<sub>i</sub>] 中有幾個 **k 約束** 子字串。  

## 解法

Q1 最優解，對於一個固定的範圍 s[0..N-1] 可以達到 O(N) 的時間複雜度。  
在本題卻要處理高達 10^5 次的查詢，直接套用同方法會是 O(N^2)，肯定會超時。  

本題每次查詢都是**相互獨立**的，不須按照給定的順序處理。  
並且不像互動題型需要每次查詢後立刻回復答案，所以可以**預先知道**所有查詢的內容，也就是**離線查詢**。  

---

設每次查詢的左右邊界為 ql, qr。  

原始方法是**枚舉右端點**，並找到左端點的**合法區間**，區間內的每個點都和右端點產生一個 **k 約束**。  
因此只要按照枚舉右端點 right 後，再回答 ql = right 的所有查詢，即保證所有找到的答案都不超過 right。  

為滿足左邊界限制，需紀錄產生的 **k 約束**是**在哪個左端點**，並還要查詢 [ql..qr] 的數量，因此需要**線段樹**。  
找到距離 right 最遠的左端點 left 後，[left..right] 區間的每個位置都貢獻一個答案，因此將 [left..right] 區間都加 1。  
之後查詢再填入 [ql..right] 的加總即可。  

時間複雜度 O(N + Q log N)。  
空間複雜度 O(N + Q)。  

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        N = len(s)
        Q = len(queries)

        # sort queries by right bound
        qs = [[] for _ in range(N)] 
        for qid, (_, qr) in enumerate(queries):
            qs[qr].append(qid)
        
        ans = [0]*Q
        seg = SegmentTree(N)
        left = cnt1 = cnt0 = 0
        for right, x in enumerate(s):
            if x == "1":
                cnt1 += 1
            else:
                cnt0 += 1

            # find left-most left bound
            while cnt1 > k and cnt0 > k:
                if s[left] == "1":
                    cnt1 -= 1
                else:
                    cnt0 -= 1
                left += 1

            # [left..right] can be left bound with right
            seg.update(1, 0, N-1, left, right, 1)
            for qid in qs[right]:
                ql = queries[qid][0]
                ans[qid] = seg.query(1, 0, N-1, ql, right)

        return ans

class SegmentTree:

    def __init__(self, n):
        self.tree = [0]*(n*4)
        self.lazy = [0]*(n*4)

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def push_down(self, id, L, R, M):
        """
        將區間懶標加到答案中
        下推懶標記給左右子樹
        """
        if self.lazy[id]:
            self.tree[id*2] += self.lazy[id]*(M-L+1)
            self.lazy[id*2] += self.lazy[id]
            self.tree[id*2+1] += self.lazy[id]*(R-M)
            self.lazy[id*2+1] += self.lazy[id]
            self.lazy[id] = 0

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
        M = (L+R)//2
        self.push_down(id, L, R, M)
        res = 0
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i, j, val):
        """
        區間更新
        對[i, j]每個索引都增加val
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            self.tree[id] += val * (R - L + 1)
            self.lazy[id] += val
            return
        M = (L+R)//2
        self.push_down(id, L, R, M)
        if i <= M:
            self.update(id*2, L, M, i, j, val)
        if M < j:
            self.update(id*2+1, M+1, R, i, j, val)
        self.push_up(id)
```
