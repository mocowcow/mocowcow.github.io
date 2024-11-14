---
layout      : single
title       : LeetCode 3346. Maximum Frequency of an Element After Performing Operations I
tags        : LeetCode Medium PrefixSum HashTable Sorting BinarySearch
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

但對於 Q3 來說，MX 高達 10^9，不可能直接開陣列，因此必須改用雜湊表。  
雜湊表可以接受負數索引，就不必對 nums 加上偏移量。  

差分構造完之後，我們只需要將出現過的索引位置排序後做前綴和即可。  

注意：某些情況答案會出現在 nums 中原有的索引，例如：  
> nums = [10,11], k = 5, numOperations = 1。  
> diff 中的鍵值只有 [10-5, 10+5+1, 11-5, 11+5+1]  
> = [5, 16, 6, 17]  

但正確答案應該是把其中一個移到 10 或 11 上。因此原有的索引位置也須列入考慮。  

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
再將 nums 排序，枚舉候選索引 x，找到第一個大於等於 x-k 的索引、以及最後一個小於等於 x+k 的索引。  
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
            # [x-k, x-k]
            # first index >= x-k
            left = bisect_left(nums, x-k)
            # last index <= x+k
            right = bisect_right(nums, x+k) - 1
            t = right - left + 1

            # update answer
            inc = min(t - freq[x], numOperations)
            ans = max(ans, freq[x] + inc)

        return ans
```
