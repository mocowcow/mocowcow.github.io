--- 
layout      : single
title       : LeetCode 2576. Find the Maximum Number of Marked Indices
tags        : LeetCode Medium Array Sorting TwoPointers Greedy
---
周賽334。作法有點不直觀，卡了一陣子才想到。  

# 題目
輸入整數陣列nums。  

最初所有的索引都是未標記的。你可以執行以下動作任意次：  
- 選取兩個**不同**的**未標記索引**i和j，符合2 * nums[i] <= nums[j]，然後將i和j標記  

求最多可以標記多少索引。  

# 解法
如果有N個數字，每次標記兩個數，則最多可以有N/2對數對(i, j)。  
當N是奇數時，例如nums=[1,2,100]，選擇1或是2都可以和100配對，而選擇較小的數字更容易配對成功，所以只考慮將奇數陣列的中心元素歸到右半邊。  
排序後，前半段都是nums[i]的候選人，而後半段是nums[j]的候選人。  

維護雙指針i和j，分別指向前、後半段的開頭。如果nums[i]和nums[j]配對成功，則兩者都往右移動，答案增加2；否則只移動j，試著將nums[j]的值變大。  

瓶頸在於排序，時間複雜度O(N log N)。空間複雜度O(1)。  

```python
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        half=N//2
        i=0
        j=half
        ans=0
        
        while i<half and j<N:
            if nums[i]*2<=nums[j]:
                ans+=2
                i+=1
            j+=1
            
        return ans
```

甚至可以直接算出右半段的起點索引，只維護i。因為每次配對成功後i會加1，最後i停止的索引正好會等於配對的數量，直接乘2就是答案。  

```python
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        i=0
        j_start=(N+1)//2
        
        for j in range(j_start,N):
            if nums[i]*2<=nums[j]:
                i+=1
            
        return i*2
```