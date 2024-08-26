---
layout      : single
title       : LeetCode 3265. Count Almost Equal Pairs I
tags        : LeetCode Medium String HashTable
---
weekly contest 412。  

## 題目

輸入正整數陣列 nums。  

若兩個整數 x, y 在執行以下操作**最多一次**後，能夠變得相等，則稱為**幾乎相等**：  

- 選擇 x 或 y，並將選擇整數中的兩個數位交換。  

求有多少滿足 i < j 的數對 (i, j) 且 nums[i] 和 nums[j] **幾乎相等**。  
注意：操作後的整數可以有前導零。  

## 解法

前導零還挺麻煩的，例如 3 無法操作出其他結果，但是 30 可以操作成 03。  
乾脆把整數轉成字串並補上前導零 (本題至多 7 位數字)，這樣比較方便處理。  

只有在兩字串的字元出現次數完全相等，且只有 0 或 2 個位置的字元不同時，才有可能相等。  

時間複雜度 O(N^2 \* log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            s = str(x).zfill(7)
            for y in nums[:i]:
                t = str(y).zfill(7)
                diff = sum(c1 != c2 for c1, c2 in zip(s, t))
                if Counter(s) == Counter(t) and diff <= 2:
                    ans += 1

        return ans
```
