---
layout      : single
title       : LeetCode 3171. Find Subarray With Bitwise AND Closest to K
tags        : LeetCode Hard Array TwoPointers SlidingWindow BitManipulation HashTable
---
周賽 400。更新答案少寫一行，虧一個 WA，好慘。  
LC 官方最近宣布使用**先進的作弊檢查計數**，嚴格禁止任何作弊行為，不知道效果如何。  
唯一確定的是這場伺服器有點問題，希望別又在我上分的時候 unrate。  

## 題目

輸入整數陣列 nums 和整數 k。  
你必須找到一個 nums 的子陣列，其做 AND 運算後的結果與 k 的**絕對差最小化**。  
也就是找到子陣列 nums[l..r]，滿足最小的 \| k - (nums[l] AND nums[l + 1] ... AND nums[r]) \|。  

求子陣列與 k 的**最小絕對差**。  

## 解法

複習 AND 的特性：只減不增。  

一個子陣列擴展邊界、增加元素時，其 AND 結果只可能變小，不可能增加；  
反之，縮減邊界、減少元素時，其 AND 結果只可能變大，不可能變小。  

---

子陣列問題通常可以透過**滑動窗口**解決。  

維護 left 作為窗口左端點，並枚舉右端點 right。  
如果窗口內子陣列的 AND 結果大於 k，需要等待加入新元素以降低結果；若小於 k，則要刪除左方元素，以提高結果。  

至於如何有效率維護窗口內的 AND 結果？  
回想到 AND 是只大不小，對於每個 bit 來說，只有所有元素對應的該位元都是 1，結果才會是 1；否則肯定是 0。  
因此只要分別維護各位元中出現 1 的次數，若出現次數等於窗口大小，則該位元在結果中會是 1。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        M = max(nums).bit_length()
        cnt = [0] * M
        
        def calc(sz):
            res = 0 
            for i in range(M):
                if cnt[i] == sz:
                    res |= (1 << i)
            return res
        
        def add(x, inc):
            for i in range(M):
                if x & (1 << i):
                    cnt[i] += inc
        
        ans = inf
        left = 0
        for right, x in enumerate(nums):
            add(x, 1)
            ans = min(ans, abs(calc(right-left+1) - k))
            while left < right and calc(right-left+1) < k:
                add(nums[left], -1)
                left += 1
                ans = min(ans, abs(calc(right-left+1) - k))
        
        return ans
```

我們在枚舉右端點的時候，會將原有的所有子陣列結果都 AND 上新的右端點 x。  
例如：  
> nums = [a,b,c,x]  
> 原本以 c 結尾的子陣列結果有 a&b&c, b&c, c  三種  
> 加上 x 之後，會變成 a&b&c&x, b&c&x, c&x, x  四種  

如果 c 和 x 是相同的元素，那麼這些子陣列的結果根本不會改變，所以結果的數量也不會變多；否則必定使原有的結果都**變小**。  
每次變小，都會失去一個 1 位元，最多只能失去 log(MX) = 30 次。  
也就是說，每個右端點所擁有的子陣列 AND 結果，**去除重複**後最多只會有 30 個。  

時間複雜度 O(N log MX)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        s = set()
        for x in nums:
            s = set(x & y for y in s) # AND x for all results
            s.add(x)
            for y in s:
                ans = min(ans, abs(k - y))
        
        return ans
```
