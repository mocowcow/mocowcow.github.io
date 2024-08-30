---
layout      : single
title       : LeetCode 3267. Count Almost Equal Pairs II
tags        : LeetCode Hard String HashTable
---
weekly contest 412。  

## 題目

輸入正整數陣列 nums。  

若兩個整數 x, y 在執行以下操作**最多兩次**後，能夠變得相等，則稱為**幾乎相等**：  

- 選擇 x 或 y，並將選擇整數中的兩個數位交換。  

求有多少滿足 i < j 的數對 (i, j) 且 nums[i] 和 nums[j] **幾乎相等**。  
注意：操作後的整數可以有前導零。  

## 解法

本題的操作次數從最多**一次**變成**兩次**。  
並且 nums 長度變成 5000，nums[i] 上限也變成 1e7。  
原本 O(N^2) 的方法大概是不會通過，只能沿用方法二，擴充第二次交換的結果。  

時間複雜度 O(N log N + N (log MX)^5)，其中 MX = max(nums)。  
空間複雜度 O(N + (log MX)^4)。  

```python
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        d = Counter()
        for x in nums:
            for pat in all_pattern(x):
                ans += d[pat]
            d[x] += 1

        return ans


def all_pattern(x):
    a = list(str(x))
    sz = len(a)
    res = {x}  # no swap

    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def build():
        res.add(int("".join(a)))

    # 1 swap
    for i in range(sz):
        for j in range(i + 1, sz):
            swap(i, j)
            build()
            # 2 swap
            for k in range(sz):
                for l in range(k + 1, sz):
                    swap(k, l)
                    build()
                    swap(k, l)
            swap(i, j)
    return res
```
