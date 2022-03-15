---
layout      : single
title       : LeetCode 2195. Append K Integers With Minimal Sum
tags 		: LeetCode Medium Array Math Sorting BinarySearch Greedy
---
周賽283。那時候想用兩個相鄰數區間+梯形公式求值，可惜一直搞錯邊界噴了四次，最後也沒做出來。今天找到更好的解法，開心。

# 題目
求k個不重複正整數最小值，且不可以在數列nums中出現過。  
> nums = [1,4,25,10,25], k = 2
> ans = sum[2,3] = 5  
> nums = [5,6], k = 6  
> ans = sum[1,2,3,4,7,8] = 25  

# 解法
與其梯形公式，不如用求和公式1+2+..+n-1+n = n*(n+1)/2。  
題目需要k個數，假設不受nums影響，也至少需要1+2+..+k = k*(k+1)/2，最後一個用到的數字是k。  
先把nums去重複排序，從頭開始檢查每個數n，若n小於等於k，代表n不可使用，ksum先扣回這個n，再加上k的下一個數字。

```python
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ksum=k*(k+1)//2
        nums = sorted(set(nums))
        for n in nums:
            if n<=k:
                k+=1
                ksum+=k-n
            else:
                break
        
        return ksum
```

第一個方法概念是多退少補，現在改成先找出最後一個數求和，再扣掉所有不可使用的部分。  
去重複+排序後nums長度為N，需要k個數，若所有n都在k以內，則答案為1+..+k扣除所有n。  
那如果nums有數字非常大，根本不會在k+N個內碰到怎辦？好朋友二分搜來了，找出需要扣掉幾個n。  
例：  
> nums =[1,4,25,10,25], k = 2  
> 去重排序nums = [1,4,10,25] 長度4  

用值+索引推出實際上有多少可用數字：  
> nums[0]=1，1~1扣掉(1本身+前面還有0個禁止數字[])，可用數0  
> nums[1]=4，1~4扣掉(4本身+前面還有1個禁止數字[1])，可用數2  
> nums[2]=10，1~10扣掉(10本身+前面還有2個禁止數字[1,4])，可用數7  
> nums[3]=25，1~25扣掉(25本身+前面還有3個禁止數字[1,4,10])，可用數21  
 
二分搜得到low=1，表示需要加上k後的1個數，並扣掉nums從左數來的1個數，得到(2+1)*(2+1+1)/2-(1) = 6-1 = 5。

```python
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=sorted(set(nums))
        N=len(nums)
        #all nums between range
        if nums[-1] < k+N:
            return (k+N)*(k+N+1)//2 - sum(nums)
        
        #binary search for proper index
        low=0
        high=N-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]-mid-1<k:
                low=mid+1
            else:
                high=mid
                
        return (k+low)*(k+low+1)//2 - sum(nums[:low])
```
