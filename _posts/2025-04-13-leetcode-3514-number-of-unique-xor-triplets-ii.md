---
layout      : single
title       : LeetCode 3514. Number of Unique XOR Triplets II
tags        : LeetCode Medium Math BitManipulation
---
biweekly contest 154。  
這題感覺有點尷尬，根據選擇資料結構和語言的差異，有些很容易超時。  

## 題目

<https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description/>

## 解法

這次 nums 裡面的數不固定了，但是 nums[i] 上限 1500。  
根據上一題的結論，可以知道 1500 的最高位 m = 11，運氣夠好的話可以造出最大值是 (1 << 11) - 1，即 2047。  

先枚舉 nums 中的任意兩個數求 x^y，至多可找到 2048 個數。  
然後枚舉剛找的 x^y，再從 nums 中枚舉第三個數 z，再，更新 x^y^z 的結果。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

注意：nums 沒去重有很高機率超時。原本沒去重，我交了 3 次才壓線過關。  

```python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        set_x = set(nums)  # dedup for efficiency
        set_xy = set(x ^ y for x in set_x for y in set_x)
        set_xyz = set(xy ^ z for z in nums for xy in set_xy)

        return len(set_xyz)
```

改成陣列寫法就快很多，甚至直接開 2048 大小的陣列都比集合快。  

題外話，不知道是不是本題時間比較緊湊，golang 用 map 過不了，一定要陣列寫法。  

```python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        set_x = set(nums)  # dedup for efficiency
        m = max(set_x).bit_length()
        sz = 1 << m

        set_xy = [False] * sz
        for x in set_x:
            for y in set_x:
                set_xy[x ^ y] = True

        set_xyz = [False] * sz
        for xy in range(sz):
            if set_xy[xy]:
                for z in set_x:
                    set_xyz[xy ^ z] = True

        return sum(set_xyz)
```
