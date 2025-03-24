---
layout      : single
title       : LeetCode 1953. Maximum Number of Weeks for Which You Can Work
tags        : LeetCode Medium Greedy
---

## 題目

<https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/>

## 解法

有若干種任務，數量各不同。  
連續選擇的任務不可相同，求最多能選幾個。  

---

設 S = sum(milestone)。  

最佳情況下是 S 個全選完。  
但範例 2 告訴我們，若某任務數量過高，則無法全選：  
> milestone = [5,2,1]  

若某任務有 x 個，則至少需要 x-1 個不同的任務做間隔，才能全部完成。  

---

那同一種任務最多能選幾次？  
題目限制不能相鄰相同，**貪心**地從最左開始放，每放一個就空一格，放置的索引是偶數 0,2,4,...。  
值到偶數都放完，繼續奇數才會出現相鄰相同。  

分類討論 [0..S-1] 有幾個偶數索引：  

- S 是奇數，有 ceil(S / 2) 個偶數索引  
- S 是偶數，有 floor(S / 2) 個偶數索引  

因此同一種任務至多能選 ceil(S / 2) 次。  

---

根據**鴿巢原理**，只有某個任務數 x 超過 ceil(S / 2) 才會相鄰相同。  
並且也只有數量最多的那一種任務能夠超過。  

設 MX = max(milestone)。  
分類討論 MX 是否能放完：  

- 若 MX 超 ceil(S / 2)，則沒辦法全部放完。  
    這時其他的任務有 S - MX 個，用做間隔，能夠搭配 (S - MX) + 1 個最多的任務。  
    共能放 (S - MX) \* 2 + 1 個。  
- 若 MX 不超過 ceil(S / 2)，則隨便放都能放完。  
    能 S 個全放。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        S = sum(milestones)
        MX = max(milestones)

        if MX > (S+1) // 2:
            return (S - MX) * 2 + 1
        else:
            return S
```
