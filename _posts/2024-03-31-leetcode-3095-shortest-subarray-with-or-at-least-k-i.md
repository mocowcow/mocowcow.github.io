---
layout      : single
title       : LeetCode 3095. Shortest Subarray With OR at Least K I
tags        : LeetCode Easy Array BitManipulation SlidingWindow TwoPointers
---
雙周賽 127。手殘把 -1 打錯，得到免費 WA。  

## 題目

輸入非負整數陣列 nums 和整數 k。  

如果對一個陣列的所有元素做位元 OR 的結果至少有 k，則稱為**特殊的**。  

求 nums 中**最短**的**特殊非空**子陣列長度。  
若不存在則回傳 -1。  

## 解法

暴力法，由長度小到大，枚舉所有子陣列並求 OR 後的結果。  
若滿足 k 則回傳當前長度。  

時間複雜度 O(N^3)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        for size in range(1, N + 1):
            for left in range(N - size + 1):
                val = reduce(ior, nums[left:left + size])
                if val >= k:
                    return size
        
        return -1
```

對於更大的測資，絕對不可能枚舉子陣列。  

OR 運算的特性是**只增不減**。因此對一個子陣列增加元素，只有可能使得結果**變大**或**不變**。  
例如：nums[i..j] 的結果滿足 k，則以 j + 1 結尾的子陣列，其左邊界至多為 i。  

並且，同一個位元最多只能在結果中出現一次。  
例如：nums[i] = 10 = 0b1001，則結果中的第 0 個、第三個位元必定是 1。  

---

我們可以從左到右枚舉子陣列的右邊界，並維護子陣列元素對於**各個位元**的**出現次數**。  
枚舉所有位元，有出現就加入當前結果。  
只要結果滿足 k，則以當前子陣列大小更新答案，並收縮左邊界。  

注意：需要對 k = 0 特判，或是在收縮邊界時檢查左邊界是否有效，否則會報錯。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = inf
        left = 0
        d = [0] * 30
        
        def f():
            res = 0
            for i in range(30):
                if d[i] > 0:
                    res |= (1 << i)
            return res
        
        for right, x in enumerate(nums):
            # add bit
            for i in range(30):
                if x & (1 << i):
                    d[i] += 1
            
            while left <= right and f() >= k:
                ans = min(ans, right - left + 1)
                # del bit
                y = nums[left]
                left += 1
                for i in range(30):
                    if y & (1 << i):
                        d[i] -= 1

        if ans == inf:
            return -1
        
        return ans
```
