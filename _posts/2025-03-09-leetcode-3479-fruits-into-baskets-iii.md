---
layout      : single
title       : LeetCode 3479. Fruits Into Baskets III
tags        : LeetCode Medium SegmentTree BinarySearch
---
weekly contest 440。  
競爭激烈，現在連 Q3 中等題都要用上線段樹了。  
這次無 BUG 一次過，給自己一個讚。  

## 題目

<https://leetcode.com/problems/fruits-into-baskets-iii/description/>

## 解法

在考慮水果 x 要放哪時，如果 baskets 全部都小於 x，肯定不能放，答案加 1。  

---

baskets 的最大值大於等於 x，我們要找到最靠左、且依然大於等於 x 的那個元素在哪。  
當前區間 baskets[L..R] 最大值滿足 x，確定有答案。分類討論：  

- 若左半邊 baskets[L..M] 最大值依然滿足 x，為了找最靠左的籃子，答案肯定在左半邊。  
- 否則答案肯定在右半邊 baskets[M+1..R]。  

為了將 baskets 分割成若干的**區間**，並維護**最大值**，需要使用**線段樹**。  
直接在線段樹上進行二分，找到第一個大於等於 x 的索引 i，並將 baskets[i] 改成 0。  

相似題 [2286. booking concert tickets in groups]({% post_url 2022-05-30-leetcode-2286-booking-concert-tickets-in-groups %})。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        seg = SegmentTree(N)
        seg.build(baskets, 1, 0, N-1)
        ans = 0
        for x in fruits:
            if seg.tree[1] < x:
                ans += 1
                continue

            i = seg.bisect(1, 0, N-1, x)
            seg.update(1, 0, N-1, i, 0)

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

    def update(self, id, L, R, i, val):
        """
        單點更新
        索引i改成val
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

    def bisect(self, id, L, R, target):
        if L == R:
            return L
        M = (L+R)//2
        if self.tree[id*2] >= target:
            return self.bisect(id*2, L, M, target)
        else:
            return self.bisect(id*2+1, M+1, R, target)
```
