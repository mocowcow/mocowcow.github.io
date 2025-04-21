---
layout      : single
title       : LeetCode 3523. Make Array Non-decreasing
tags        : LeetCode Medium Greedy
---
weekly contest 446。

## 題目

<https://leetcode.com/problems/make-array-non-decreasing/description/>

## 解法

操作只能去掉連續區間內的**非**最大值。  

舉幾個例子觀察：  
[1,2,3] 是非遞減的，不須操作。  
[3,2,1] 是遞減的，但只能去掉非最大值，操作後剩下 [3]。  

再來看看 [2,3,1,4]。  
中間 [3,1] 這段呈遞減。第一種方案很直覺的方案是刪掉 1，變成 [2,3,4]。  
那如果不想刪 1，改刪 3 可以嗎？  
想刪掉 3 必須要等到右方的 4 出現，而且還是會把 1 也一起刪掉，變成 [2,4]，不可能得到更好的結果。  

設答案陣列最後一個數為 last。  
遍歷 nums 過程中，每找到大於等於 last 的數就保留並更新 last 值。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0
        last = 0
        for x in nums:
            if x >= last:
                ans += 1
                last = x

        return ans
```
