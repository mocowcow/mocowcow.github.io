---
layout      : single
title       : LeetCode 3134. Find the Median of the Uniqueness Array
tags        : LeetCode Hard Array TwoPointers SlidingWindow BinarySearch HashTable
---
周賽395。剩兩分鐘才想通，差點吃土，好刺激。  
上次題目沒講清楚要選左還右中位數，被罵得很慘，這次終於記得了。  

## 題目

輸入整數陣列 nums。  
一個陣列的**獨特陣列**是一個遞增排序的陣列，由 nums 所有非空子陣列中**不同元素的個數**組成。  
換句話說，就是所有 0 <= i <= j < nums.length 的 distinct(nums[i..j]) 組成的遞增陣列。  

其中 distinct(nums[i..j]) 指的是子陣列 nums[i..j] 中**不同元素的個數**。  

求 nums 的**獨特陣列**的**中位數**。  

注意：中位數指的是有序遞增陣列的的中間元素。若有兩個中間元素，則選擇較小者。  

## 解法

長度 N 的陣列共有 tot = N \* (N + 1) / 2 個子陣列，每個陣列會產生一個值。  
所以中位數應該是從 1 開始數來第 target =  (tot + 1) / 2 個值。  

---

但是 N 很大，要直接生成所有子陣列肯定會超時。  

我們只在乎子陣列中**不同元素的個數**，以下簡稱**獨特值**。  
對於一個獨特值為 k 的子陣列，他必定包含其他獨特值為 k - 1 的子陣列，以此類推。  
因此能夠在枚舉子陣列的時候，找到所有**獨特值小於等於 k** 的子陣列個數。  

設 f(k) 為：獨特值小於等於 k 的子陣列個數。  
基於這個特性，只需要從 1 開始枚舉 k，只要 f(k) 滿足 target 個，就代表找到中位數，且中位數就是 k。  

---

但是暴力枚舉 k 依然很沒效率，還需要繼續優化。  

仔細觀察發現，如果 f(k) 滿足 target，則 f(k + 1) 或者更大的值也必定滿足；反之，f(k) 不滿足，則 f(k - 1) 必定不滿足。  
答案具有**單調性**，可以透過二分搜找到第一個滿足的位置。  

子陣列獨特值最小為 1，下界 lo = 1；最大為 N，上界 hi = N。  
若 f(mid) 不滿足則更新 lo = mid + 1；否則更新 hi = mid。  
最後答案就是下界 lo。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        N = len(nums)
        tot = N * (N + 1) // 2
        target = (tot + 1) // 2
        
        def ok(limit):
            cnt = 0
            d = Counter()
            left = 0
            k = 0
            for right, c in enumerate(nums):
                d[c] += 1
                if d[c] == 1:
                    k += 1
                while k > limit:
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        k -= 1
                    left += 1
                cnt += right - left + 1
            return cnt >= target
        
        lo = 1
        hi = N
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid
            
        return lo
```
