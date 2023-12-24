---
layout      : single
title       : LeetCode 2970. Count the Number of Incremovable Subarrays I
tags        : LeetCode Easy Array Simulation
---
雙周賽120。這個incremovable還真不知道怎麼翻譯，中國站翻做**移除遞增**。  
想了半天，最後AC的時候比賽剛好結束，太苦了。  

## 題目

輸入正整數陣列nums。  

若nums某個子陣列被移除後，可以使得剩餘元素**嚴格遞增**，則稱為**移除遞增**子陣列。  
例如從[5, 3, 4, 6, 7]中移除[3, 4]後變成[5, 6, 7]，所以是**移除遞增**子陣列。  

求nums有多少**移除遞增**子陣列。  

注意：空陣列也視為嚴格遞增。  

## 解法

先來個暴力解，枚舉所有子陣列移除後的結果。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N=len(nums)
        
        def ok(i,j):
            sub=nums[:i]+nums[j+1:]
            for a,b in pairwise(sub):
                if a>=b:
                    return False
            return True
        
        ans=0
        for i in range(N):
            for j in range(i,N):
                if ok(i,j):
                    ans+=1
                    
        return ans
```

看看範例1，整個nums已經是有序的，那麼移除任意子陣列之後還是維持有序。  
答案就是子陣列的數量N\*(N+1)//2。  

再來範例2，可以把nums拆分成兩個遞增的區間[6]和[5,7,8]。  
如果把左區間刪光，右區間直接就是遞增，可刪可不刪。有[6],[6,5],[6,5,7],[6,5,7,8]共4種刪法。  
如果不刪左區間，右區間必須刪掉5，才能使得中間銜接的部分遞增，其餘的部分可刪可不刪。有[5],[5,7],[5,7,8]共3種刪法。  
答案共是4+3=7種。  

再看範例3，可拆分成四個區間[8],[7],[6],[6]。  
不管怎樣，最多只能保留最左的[8]和最右的[6]，中間部分全都要刪掉，否則不可能遞增。  
發現超過兩個區間，處理方式就和兩個區間相同。  

總之就是枚舉左區間保留的最大值x，並將右區間前半段小於等於x的元素刪掉，剩餘的元素可選可不選。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N=len(nums)
        grp=[]
        i=0
        while i<N:
            j=i
            while j+1<N and nums[j+1]>nums[j]:
                j+=1
            grp.append(nums[i:j+1])            
            i=j+1
            
        if len(grp)==1:
            return N*(N+1)//2
        
        a=grp[0]
        b=deque(grp[-1])
        
        ans=len(b)+1
        for x in a:
            while b and b[0]<=x:
                b.popleft()
            ans+=len(b)+1
            
        return ans
```
