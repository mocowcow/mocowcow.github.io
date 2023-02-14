--- 
layout      : single
title       : LeetCode 2563. Count the Number of Fair Pairs
tags        : LeetCode Medium Array Sorting BinarySearch
---
周賽332。稍微繞了一點遠路，後來仔細研究發現這題其實滿有趣的。  

# 題目
輸入長度為n的整數陣列nums，以及整數lower和upper，求有多少**公平的數對**。  

一個**公平的數對**(i, j)必須符合：  
- 0 <= i < j < n  
- lower <= nums[i] + nums[j] <= upper  

# 解法
其實有點像是哩扣第一題的two sum，窮舉所有j，並找到符合的i，差別在於現在要找的目標是一個區間。  
如果選定了nums[j]，則要找的區間變成lower - nums[j] <= nums[i] <= upper - nums[j]。  

試想：  
> nums = [0,1,7,4,4,5], lower = 3, upper = 6  
> 當j = 3, nums[j] = 4時  
> nums[i]的最小可能值為3-4 = -1，而最大可能值為6-4 = 2
> 而可選的nums[i]有[0,1,7]三個，符合條件的有[0,1]兩個  

但是在窮舉j時，左方所出現過的數字並不一定有序，所以我們必須將其保存在有序的結構中，才使用二分搜找出適當的區間。  
維護一個sorted list，在處理完每個j之後將其值加入，以供二分搜。  

如此一來，對於每個nums[j]的最大值mx以及最小值mn，找到最後一個小於等於mx的索引right，以及第一個大於等於mn的索引left。這段區間中共有right-left+1個合法的nums[i]，將其加入答案中。  

時間複雜度O(N log N)。空間複雜度O(N)。  

```python
from sortedcontainers import SortedList

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl=SortedList()
        ans=0
        
        for n in nums:
            mx=upper-n
            mn=lower-n
            right=sl.bisect_right(mx)-1
            left=sl.bisect_left(mn)
            ans+=right-left+1
            sl.add(n)
 
        return ans
```

其實更簡單的方式是：**直接排序nums**。  

假設：  
> nums = [10, 5], lower = -100, upper = 100  
> (0, 1)是公平數對，實際對應的數字為(10, 5)  
> 排序後nums = [5, 10]  
> (0, 1)還是公平數對，實際對應的數字為(5, 10)  

答案數量並沒有改變，可見兩種方法是等價的。  

時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        a=[]
        ans=0
        
        for n in nums:
            mx=upper-n
            mn=lower-n
            right=bisect_right(a,mx)-1
            left=bisect_left(a,mn)
            ans+=right-left+1
            a.append(n)    
            
        return ans
```

直接在nums中自訂上下界來搜索，可以達到O(1)空間複雜度。  

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        a=[]
        
        def lower_bound(lo,hi,target):
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]<target:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        def upper_bound(lo,hi,target):
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]<=target:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        
        for i,n in enumerate(nums):
            mx=upper-n
            mn=lower-n
            right=upper_bound(0,i,mx)-1
            # right=bisect_right(nums,mx,lo=0,hi=i)-1
            left=lower_bound(0,i,mn)
            # left=bisect_left(nums,mn,lo=0,hi=i)
            ans+=right-left+1
            a.append(n)
            
        return ans
```