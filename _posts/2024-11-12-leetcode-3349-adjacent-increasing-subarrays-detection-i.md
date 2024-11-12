---
layout      : single
title       : LeetCode 3349. Adjacent Increasing Subarrays Detection I
tags        : LeetCode Easy Simulation
---
weekly contest 423。  

## 題目

輸入長度 n 的整數陣列 nums，還有整數 k。  
判斷是否有兩個長度為 k 的**相鄰**的**嚴格遞增子陣列**。  

具體的說，檢查是否存在索引由 a 和 b 開始的子陣列 (a < b)，滿足以下條件：  

- 兩個子陣列 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是**嚴格遞增**。  
- 兩個子陣列相鄰，即 b = a + k。  

若能找到則回傳 true，否則回傳 false。  

## 解法

暴力解法，枚舉所有長度為 k 的子陣列當作左邊的，再檢查右邊的 k 個是否也滿足遞增。  

時間複雜度 O(NK)。  
空間複雜度 O(1)。  

```python
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        def ok(i):
            if i+k-1 >= N:
                return False
            return all(a < b for a,b in pairwise(nums[i:i+k]))
        
        for i in range(N):
            if ok(i) and ok(i+k):
                return True

        return False
```

先分割出所有遞增子序列，並記錄長度。  
長度為 x 的遞增子序列，還可以分割成若干個小於等於 x 的子陣列。  

因為找的是**相鄰**子陣列，並檢查倆倆相鄰的長度是否都大於等於 k 即可。  
例如：k = 3, [1,2,3], [1,2,3]。  

也可能單一個子陣列足夠長，可以分割成兩個
例如：k = 3, [1,2,3,4,5,6] 分割 [1,2,3], [4,5,6]。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        subs = []
        i = 0
        while i < N:
            j = i
            while j+1 < N and nums[j] < nums[j+1]:
                j += 1
            subs.append(j-i+1) # size of increasing subarray
            i = j+1

        for a, b in pairwise(subs):
            if a >= k and b >= k: # both subarrays are size of k
                return True

        return max(subs) >= k*2  # single subarray split into 2 size of k
```

只需要紀錄前一個子陣列的大小，就可以做到一次遍歷，以及常數空間。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        pre = 0 # size of previous subarray
        i = 0
        while i < N:
            j = i
            while j+1 < N and nums[j] < nums[j+1]:
                j += 1

            curr = j-i+1 # size of current subarray
            if pre >= k and curr >= k or curr >= k*2:
                return True

            pre = curr
            i = j+1

        return False
```
