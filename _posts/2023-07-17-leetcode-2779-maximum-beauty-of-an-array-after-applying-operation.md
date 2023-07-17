--- 
layout      : single
title       : LeetCode 2779. Maximum Beauty of an Array After Applying Operation
tags        : LeetCode Medium Array SlidingWindow TwoPointers Sorting BinarySearch
---
周賽354。一開始又看錯題目，浪費一些時間。  
最後用了次佳解，還挺擔心會不會TLE，好險沒有。  

# 題目
輸入整數陣列nums和非負整數k。  

每次操作，你可以：  
- 從[0, nums.length-1]間選擇一個**沒選過的**索引i。  
- 將nums[i]換成[nums[i]-k, nums[i]+k]之間的任意一個數。  

定義一個陣列的美麗值為**由單一元素組成的最長子序列**長度。  

求任意次操作後，nums的最大美麗值為多少。  

注意：每個索引只能執行一次操作。  

# 解法
x可以變成[x-k, x+k]之間的任意數。  
反過來說，介於[x-k, x+k]之間的數都可以變成x。  

能夠變成x的數字共有size=1+k\*2種。  
枚舉右邊界right，維護大小為size的滑動窗口。窗口內的所有元素都可以變成相同數，並組成子序列。  

時間複雜度O(N + MX)，其中MX為max(nums)。  
空間複雜度O(MX)。  

如果MX範圍太大，可能要考慮用雜湊表維護出現次數。  

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        MX=max(nums)
        size=k*2+1
        cnt=[0]*(MX+1)
        
        for x in nums:
            cnt[x]+=1
            
        ans=0
        left=0
        sm=0
        for right in range(MX+1):
            sm+=cnt[right]
            while right-left+1>size:
                sm-=cnt[left]
                left+=1
            ans=max(ans,sm)
            
        return ans
```

延續上述思路，若窗口最小值為x，則最大值為x+2\*k。  

將nums排序後，枚舉每個元素nums[i]，用二分搜找到最後一個nums[i]+2\*k的位置，這些元素全都屬於相同區間。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        
        for i,x in enumerate(nums):
            j=bisect_right(nums,x+k*2)-1
            ans=max(ans,j-i+1)
            
        return ans
```

或是不用二分，直接雙指針維護最大差不超過2\*k的滑動窗口也可以。  
雖然時間瓶頸依然在於排序，但是找區間的部分會快一些。  

```python
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        left=0
        
        for right,x in enumerate(nums):
            while x-nums[left]>2*k:
                left+=1
            ans=max(ans,right-left+1)
            
        return ans

```