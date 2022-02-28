---
layout      : single
title       : LeetCode 228. Summary Ranges
tags 		: LeetCode Easy Array TwoPinters
---
每日題。沒注意到竟然會輸入空陣列，噴了WA，尷尬。

# 題目
輸入有序遞增的不重複整數陣列nums，將nums分為數個連續的區間。  
> Input: nums = [0,1,2,4,5,7]  
> Output: ["0->2","4->5","7"]

# 解法
維護串列t，用以保存各區間中的所有整數。  
遍歷每個整數n，當t為空時直接加入n；t最後一個元素+1若等於n時，也將n加入t；否則將t加入ans，並刷新t為空串列。  
跑完nums後再把最後的t也加入ans，處理輸出字串。  
遍歷ans中的每個串列x，若x長度為1則直接將唯一一個整數轉為字串；否則輸出x[0]+'->'+x[-1]。

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        t = []
        for n in nums:
            if not t:
                t.append(n)
            elif t[-1]+1 == n:
                t.append(n)
            else:
                ans.append(t)
                t = [n]

        ans.append(t)

        return [str(x[0]) if len(x) == 1 else str(x[0])+'->'+str(x[-1]) for x in ans]

```

雙指標方法，竟然比上面的慢，真奇怪。  
維護變數a和b代表區間最前和最後位置，初始為0。當b後面還有元素且nums[b]+1等於nums[b+1]，則將b後移一位。不能再移就依據a和b的位置做字串輸出，最後b再往右移1次，a移到b同位。

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        N = len(nums)
        a = b = 0
        while b < N:
            while b+1 < N and nums[b]+1 == nums[b+1]:
                b += 1
            if a == b:
                ans.append(str(nums[a]))
            else:
                ans.append(str(nums[a])+'->'+str(nums[b]))
            b += 1
            a = b

        return ans

```
