--- 
layout      : single
title       : LeetCode 2598. Smallest Missing Non-negative Integer After Operations
tags        : LeetCode Medium Array HashTable Math
---
周賽337。用了次佳解邊界範圍算錯WA一次，好慘。而且竟然連續兩次Q4都放Medium。  

# 題目
輸入整數陣列nums和整數value。  

每一次操作中，你可以將任一元素增加或減少value。  
- 例如nums = [1,2,3], value = 2，可以把nums[0]減掉value，而後nums = [-1,2,3]  

MEX(minimum excluded)指的是不存在陣列中的的最小非負整數。  
- 例如[-1,2,3]的MEX為0，而[1,0,3]的MEX為2  

求nums執行**任意次操作**後的**最大**MEX。  

# 解法
如果兩個元素差值不為value的倍數，則無法通過操作變得相等；反之，可以透過若干次操作變成同一個數。  
所以我們可以將每個元素對value求餘，依照餘數將所有元素分組，例如：  
> nums = [1,2,3,4,5], value = 2  
> 餘0的有[2,4]，餘1的有[1,3,5]  
> 將[2,4]轉成[0,2]，所以變成[0,1,2,3,5]  
> MEX為4  

遍歷nums將元素依照餘數分組後，對每個餘數k從k開始標記，每次遞增value直到滿足出現次數為止。  
最後從0開始往上找MEX，找到一個沒出現過的元素就是答案。  

時間複雜度O(N)。最差情況下每個數都不同餘，空間複雜度O(N)。  

```python
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d=Counter()
        for n in nums:
            d[n%value]+=1
            
        s=set()
        for k,v in d.items():
            for _ in range(v):
                s.add(k)
                k+=value
                
        for i in range(10**5+5):
            if i not in s:
                return i
```

其實不需要維護集合s來標記出現過的數，在窮舉MEX的時候檢查餘數i%value的餘數是否有剩，若為0次代表無法轉換，直接回傳i。  

時間複雜度O(N)。空間複雜度O(min(N,value))。  

```python
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d=Counter()
        for n in nums:
            d[n%value]+=1
            
        for i in range(10**5+5):
            r=i%value
            if d[r]==0:
                return i
            d[r]-=1
```
