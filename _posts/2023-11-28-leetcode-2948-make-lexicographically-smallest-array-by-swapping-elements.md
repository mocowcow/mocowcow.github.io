---
layout      : single
title       : LeetCode 2948. Make Lexicographically Smallest Array by Swapping Elements
tags        : LeetCode Medium Array Sorting
---
周賽373。

## 題目

輸入正整數陣列nums，還有正整數limit。  

每次操作，你可以選擇兩個滿足|nums[i] - nums[j]| <= limit的索引i, j，並交換nums[i]和nums[j]的值。  

求通過任意次操作後，可以得到**字典序最小**的陣列。  

## 解法

只要兩個數的絕對差不超過limit就可以交換。  

舉個簡單的例子：  
> nums = [3,2,1], limit = 1  
> 先2和1換，得到[3,1,2]  
> 再3和1換，得到[1,3,2]  
> 最後3和2換，得到[1,2,3]  

可以發現這是一個類似連通圖的結構，只要在同一個相連區域的數字，就可以透過特定順序來任意排序。  
繼續擴展剛才的例子：  
> nums = [3,101,2,100,1], limit = 1  
> [3,2,1]三個數互相連通，最後排序是[1,2,3]  
> 填入原本的位置，nums = [1,_,2,_,3]  
> [101,100]兩個數互相連通，排序後是[100,101]  
> 填入原本的位置，nums = [_,100,_,101,_]  
> 合併起來就是[1,100,2,101,3]  

那如何找到連通塊？絕對差越小的兩個元素，越容易連通，所以先將元素帶著原始索引一起排序。  
排序後，只要相鄰的兩者絕對差不超過limit，則屬於同一個連通塊。  
將同個連通塊中的索引排序，由小到大填入元素值。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N=len(nums)
        a=[[x,i] for i,x in enumerate(nums)]
        a.sort()
        ans=[0]*N
        
        def fill(ele,idx):
            idx.sort()
            for i,e in zip(idx,ele):
                ans[i]=e
        
        ele=[]
        idx=[]
        prev=-inf
        for x,i in a:
            # new block, fill old one
            if x-prev>limit: 
                fill(ele,idx)
                ele=[]
                idx=[]
            # connect
            ele.append(x)
            idx.append(i)
            prev=x
            
        # fill last block
        fill(ele,idx)
            
        return ans
```

這邊也可以使用**分組循環**的技巧，外層迴圈紀錄左端點、處理分組後的邏輯，內層迴圈負責找右端點。  
除了寫起來簡潔，也不用怕忘記特判最後一組。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N=len(nums)
        ans=[0]*N
        
        a=sorted(enumerate(nums),key=itemgetter(1))
        i=0
        while i<N:
            idx=[a[i][0]]
            j=i
            # find group
            while j+1<N and a[j+1][1]-a[j][1]<=limit:
                j+=1
                idx.append(a[j][0])
            # fill elements
            idx.sort()
            for j in idx:
                ans[j]=a[i][1]
                i+=1
                
        return ans
```
