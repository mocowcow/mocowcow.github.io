---
layout      : single
title       : LeetCode 3312. Sorted GCD Pair Queries
tags        : LeetCode Hard Math BinarySearch PrefixSum
---
weekly contest 418。  

## 題目

輸入長度 n 的整數陣列 nums，還有整數陣列 queries。  

gcdPairs 陣列是由 nums 中所有滿足 0 <= i < j < n 的數對 (nums[i], nums[j]) 的 gcd 升序排序而成。  

對於每個查詢 queries[i]，你必須找到 gcdPairs 中索引為 queries[i] 的元素。  

回傳整數陣列 answer，其中 answer[i] 為 gcdPairs[queries[i]] 的值。  

## 解法

n 高達 10^5，要暴力算出整個 gcdPairs 是不可能的。  

設 g = gcd(a, b)，代表 a 和 b 都是 g 的倍數。  
若我們事先知道 nums 中有 cnt 個元素是 g 的倍數，則可以推斷出**至多**有 comb(cnt, 2) 組數對的 gcd 是 g。  

為什麼說是**至多**呢？  
當兩個數都是 g 的倍數、但都不等於 g 時，則 gcd 便不是 g。舉例：  
> g = 2, a = 4, b = 8  
> gcd(a, b) = gcd(4, 8) = 4  

---

定義 cnt_pair[i] 為 gcd **正好**是 i 的數對組數。  
comb(cnt, 2) 相當於 cnt_pair[i] + cnt_pair[2i] + cnt_pair[3i] + ..。  
根據**排容原理**，還需要扣除所有滿足 j 是 i 的倍數的 cnt_pair[j]，才能得到正確的 cnt_pair[i]。  
因此必須逆序計算 cnt_pair[i]。  

之後再對 cnt_pair 做**前綴和**，其中 ps[i] 代表 gcd 小於等於 i 的組數。  
最後以二分搜回答查詢即可。  

注意：查詢問的是從 0 開始的**索引**，而前綴和是**數量**，要補加 1 的偏移量。  

---

1 到 MX 的倍數共有 1 + 1/2 + 1/3 + .. + 1/MX**調和級數** O(MX log MX)。  
共 Q 次查詢，每次二分 O(log MX)，共 O(Q log MX)。  

時間複雜度 O(N + (Q + MX) log MX)，其中 MX = max(nums)。  
空間複雜度 O(MX)。  

```python
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MX = max(nums)
        d = Counter(nums)

        cnt_pair = [0] * (MX + 1)
        for i in reversed(range(1, MX + 1)):
            cnt = 0
            dup = 0
            for j in range(i, MX + 1, i):
                cnt += d[j]
                dup += cnt_pair[j]
            cnt_pair[i] = comb(cnt, 2) - dup

        ps = list(accumulate(cnt_pair))
        ans = []
        for q in queries:
            i = bisect_left(ps, q+1)
            ans.append(i)

        return ans
```
