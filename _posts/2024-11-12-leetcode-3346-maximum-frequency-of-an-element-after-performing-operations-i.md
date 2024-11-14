---
layout      : single
title       : LeetCode 3346. Maximum Frequency of an Element After Performing Operations I
tags        : LeetCode Medium PrefixSum HashTable Sorting BinarySearch SlidingWindow
---
biweekly contest 143。  
這題還真有夠難的，差點沒做出來，但是寫得有夠醜。  
不過我還真沒做出 Q3，好慘。  

## 題目

輸入整數陣列 nums 還有兩個整數 k 和 numOperations。  

你必須執行以下操作 numOperations 次：  

- 選擇一個**沒被選過**的索引 i。  
- 對 nums[i] 增加 [-k, k] 之間的整數值。  

求操作後，任意元素在 nums 中的**最大**可能出現頻率。  

## 解法

對於 nums[i] = x 來說，操作後他的位置可以在 [x-k, x+k] 之間。  
因此把每個 x 對應的區間索引都加 1，之後再找哪個索引的重疊次數最高。  

這部分可以使用**差分陣列**來實現。  

---

但是操作次數受限於 numOperations。  

假設有：  
> nums = [1,2,3], k = 1000, numOperations = 0。  

即使三個元素都可以調整到同一個位置，但卻沒有操作次數，因此答案為 1。  

為了知道每個索引 i 可以**操作增加**多少頻率，我們還需要知道 i 原有的頻率，記做 freq[i]。  
若對差分做前綴後之後，i 的前綴和為 ps，則實際上可以增加的頻率為 inc = min(numOperations, ps - freq[i])。  
也就是說，經過操作，索引 i 的頻率至多變成 freq[i] + inc。  

---

為避免 x-k 出現負數，姑且將 nums 中每個數都加上 k。  
之後遍歷所有可能的索引，以 freq[i] + inc 更新答案最大值。  

時間複雜度 O(N + MX + k)，其中 MX = max(nums)。  
空間複雜度 O(MX + k)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = [x+k for x in nums] # offset avoid negative index
        MX = max(nums)
        diff = [0] * (MX + k + 5)
        for x in nums:
            diff[x-k] += 1
            diff[x+k+1] -= 1

        freq = Counter(nums)
        ps = 0
        ans = 1
        for i in range(MX+1):
            ps += diff[i]
            inc = min(ps - freq[i], numOperations)
            ans = max(ans, freq[i] + inc)

        return ans
```

仔細分析問題的本質，發現答案只有兩種情形：  

1. 答案出現在 nums **原有**的索引上。  
2. 答案出現在 nums **沒有**的索引上。  

我們在做差分的時候，只有在 x-k, x+k+1 頻率會變化。只需檢查這兩個位置，就可以覆蓋情形一的答案。  
至於情形二當然就是 nums 原有的 x。  

---

對於 Q3 來說，MX 高達 10^9，不可能直接開陣列。  
但 N 依然是 10^5，每個 x 對應到 [x-k, x, x+k+1]，可以把用到的索引進行**離散化**，剩餘步驟相同。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        pos = set()
        for x in nums:
            pos.add(x)
            pos.add(x-k)
            pos.add(x+k+1)

        mp = {x:i for i, x in enumerate(sorted(pos))}
        N = len(mp)
        diff = [0] * (N + 5)
        freq = Counter()
        for x in nums:
            diff[mp[x-k]] += 1
            diff[mp[x+k+1]] -= 1
            freq[mp[x]] += 1

        ps = 0
        ans = 1
        for i in range(N+1):
            ps += diff[i]
            inc = min(ps - freq[i], numOperations)
            ans = max(ans, freq[i] + inc)

        return ans
```

其實根本不用離散化，直接用雜湊表就行，畢竟本來就是拿來存不連續的資料。  
注意要把 nums 中的 x 也加入雜湊表的鍵值中。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        diff = Counter()
        for x in nums:
            diff[x] += 0 # original pos
            diff[x-k] += 1
            diff[x+k+1] -= 1

        freq = Counter(nums)
        ps = 0
        ans = 1
        for i in sorted(diff.keys()):
            ps += diff[i]
            inc = min(ps - freq[i], numOperations)
            ans = max(ans, freq[i] + inc)

        return ans
```

不知道差分的同學也可以用二分搜來做。  

同樣地，先對每個 x 找出對應的 [x-k, x, x+k] 做為最高頻率的候選索引。  
再將 nums 排序，枚舉候選索引 x，找到第一個大於等於 x-k 的索引 lo、以及最後一個小於等於 x+k 的索引 hi。  
此區間大小扣掉 freq[x] 後，再與 numOperations 取最小值，即為可增加的頻率 inc。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        freq = Counter(nums)
        pos = set()
        for x in nums:
            pos.add(x)
            pos.add(x-k)
            pos.add(x+k)

        ans = 1
        for x in pos:
            # [x-k, x+k]
            # nums[lo] >= x-k 
            lo = bisect_left(nums, x-k)
            # nums[hi] <= x+k
            hi = bisect_right(nums, x+k) - 1
            t = hi - lo + 1

            # update answer
            inc = min(t - freq[x], numOperations)
            ans = max(ans, freq[x] + inc)

        return ans
```

答案在 nums 中的情況，隨著選索引 x 遞增，lo 和 hi 同步遞增。可以用**雙指針**優化。  

不在 nums 中的情況，位於 [x, x+2k] 區間內的元素都可以移動到相同位置，可以用**滑動窗口**計算。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        N = len(nums)
        nums.sort()
        ans = 1

        # case: answer index not in nums
        left = 0
        for right, x in enumerate(nums):
            if nums[left] < x - k*2:
                left += 1
            ans = max(ans, min(numOperations, right-left+1))

        # case: answer index in nums
        freq = Counter(nums)
        lo = 0
        hi = 0
        for x in nums:
            # [x-k, x+k]
            # nums[lo] >= x-k
            while nums[lo] < x-k:
                lo += 1

            # nums[hi] <= x+k
            while hi+1 < N and nums[hi+1] <= x+k:
                hi += 1

            t = hi - lo + 1
            inc = min(numOperations, t-freq[x])
            ans = max(ans, freq[x] + inc)

        return ans
```
