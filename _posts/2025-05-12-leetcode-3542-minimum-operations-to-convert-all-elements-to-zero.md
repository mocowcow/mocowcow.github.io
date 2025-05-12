---
layout      : single
title       : LeetCode 3542. Minimum Operations to Convert All Elements to Zero
tags        : LeetCode Medium DevideAndConquer SegmentTree BinarySearch
---
biweekly contest 156。  
挺難的，應該是能算上前幾難的 Q2。  

## 題目

<https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/>

## 解法

可以選 nums 的任意子陣列，把其中所有最小值變成 0。求最少需要幾次操作。  
注意：若子陣列中最小值為 0，則操作沒有任何意義。  

第一步操作很直覺，對整個 nums 操作，把所有最小值變成 0。  
操作後 nums 一定會有 0，以 0 為邊界劃分出若干個**不為 0 的子陣列**。  
得到規模更小的子問題，可以用遞迴分治解決。  

---

對於子問題 nums[l..r]，我們需要：  

- 找區間**最小值** mn  
- 找 nums[l..r] 哪些個索引是 mn，記做 pos  

查詢區間最小值可以用**線段樹**。  
mn 的位置只需要先預處理，按照 nums[i] 分組，然後二分找第一個 / 最後一個位置。  

找到 pos 後，枚舉相鄰的兩個索引 a, b，其子問題為 nums[a+1..b-1]。  
注意：若 pos[0] 不為 l，則有子問題 nums[l..pos[0]-1]；對於 r 同理。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)

        mp = defaultdict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)

        def find_pos(x, l, r):
            pos = mp[x]
            i = bisect_left(pos, l)
            j = bisect_right(pos, r)
            return pos[i:j]

        seg = SegmentTree(N)
        seg.build(nums, 1, 0, N-1)

        def solve(l, r):
            if l > r:
                return 0

            mn = seg.query(1, 0, N-1, l, r)
            pos = find_pos(mn, l, r)
            cnt = 1 if mn > 0 else 0
            for a, b in pairwise(pos):
                cnt += solve(a+1, b-1)
            if pos[0] != l:
                cnt += solve(l, pos[0]-1)
            if pos[-1] != r:
                cnt += solve(pos[-1]+1, r)
            return cnt

        return solve(0, N-1)


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
        return min(a, b)

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
        res = inf
        M = (L+R)//2
        if i <= M:
            res = self.query(id*2, L, M, i, j)
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res
```
