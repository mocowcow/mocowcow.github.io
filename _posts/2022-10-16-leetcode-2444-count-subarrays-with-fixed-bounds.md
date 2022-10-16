--- 
layout      : single
title       : LeetCode 2444. Count Subarrays With Fixed Bounds
tags        : LeetCode Hard Array SlidingWindow TwoPointers
---
周賽315。雖然沒有昨晚雙周賽的Q4那麼難，通關人數也不少，但我卻做不出來，真是碰上知識盲點了。  

# 題目
輸入一個整數陣列nums，及兩個整數minK和maxK。  

nums的**定界子陣列**指的是滿足以下條件的子陣列：  
- 子陣列中的最小值等於minK  
- 子陣列中的最大值等於maxK  

回傳定界子陣列的數量。  

# 解法
雖然有猜到是滑動窗口，卻不知道怎麼做。看了許多大神題解才搞懂其一二。  

維護變數l作為子陣列左邊界，還有mn和mx代表minK和maxK最後一次的出現位置。  
窮舉nums中每個索引r作為子陣列右邊界，如果nums[r]超出k的範圍，則不可能以r作為子陣列元素，直接將左邊界更新到r+1；否則依照nums[r]的值更新minK和maxK的最後出現位置。  

對於右邊界r來說，要在l\~r中有多少個索引可以作為合法的左邊界。因為minK和maxK都要出現，所以取idx=min(minK,maxK)，左邊界的收縮範圍就是l\~idx，所以要在答案中加上idx-l+1。因為有可能產生負數，所以得到的結果要先和0取max。  

時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mn=mx=-1
        l=0
        ans=0
        
        for r,n in enumerate(nums):
            if minK<=n<=maxK:
                if n==minK:
                    mn=r
                if n==maxK:
                    mx=r
                idx=min(mn,mx)
                ans+=max(0,idx-l+1)
            else:
                l=r+1
            
        return ans
```
