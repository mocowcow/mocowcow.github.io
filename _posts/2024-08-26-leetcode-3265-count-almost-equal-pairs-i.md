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

上面方法會對同一個 nums[i] 重複處理好幾次，不太有效率。  
每個元素是否能只處理一次？  
試著從左到右枚舉 nums[j]，暴力生成所有交換方式，並檢查是否存在於先前處理過的 nums[i] 之中。  

注意先前提過的**前導零**問題，因此必需先排序，以利較小的元素優先處理。  

時間複雜度 O(N log N + N (log MX)^3)，其中 MX = max(nums)。  
空間複雜度 O(N + (log MX)^2)。  

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
            swap(i, j)
    return res
```
