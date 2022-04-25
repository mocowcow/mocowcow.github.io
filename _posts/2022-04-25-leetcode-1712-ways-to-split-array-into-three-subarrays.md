---
layout      : single
title       : LeetCode 1712. Ways to Split Array Into Three Subarrays
tags 		: LeetCode Medium Array BinarySearch PrefixSum TwoPointers
---
二分搜學習計畫。這題也差不多快要hard難度，而且最佳解也不是二分搜，而是雙指針。

# 題目
輸入整數陣列nums，你要把nums分割成三個**非空**子陣列，由左到右分別為left, mid, right，且mid總和必須大於等於left總和，而right總和必須大於等於mid總和。  
求有幾種分割的方法。

# 解法
把nums切成三段，需要兩刀，切出來區段稱為L,M,R，須符合L<=M<=R。  
既然要一直重複使用區段加總，可以先計算前綴和psum，降低之後查詢成本。  
枚舉所有i，0<=i<=(N-3)，第一刀切在i的右方，使得nums[0]\~nums[i]成為L。  
之後找出第二刀的最左位置j，使psum(i+1,j)為M，且L<=M。仔細想一下，這兩個區間是連續的，要使M不小於R，只要找到第一個j使psum(0,j)至少是兩倍的psum(0,i)就行。  
然後再找第二刀個最右k，使psum(i+1,k)為M，同時還要M<=R保持成立。若當前psum(i+1,k)<=psum(k+1,最後位)，則k+1，終止後k-1就第二刀最右方的位置。  
最後的最後，(k-1)-j+1即是以i為第一刀時，可以產生的分割方法。

```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N=len(nums)
        psum=[0]
        j=k=0
        ans=0
        for n in nums:
            psum.append(psum[-1]+n)
        for i in range(N-2):
            while j<=i or (j<N-1 and psum[j+1]<psum[i+1]*2):
                j+=1
            if j==N-1: # no remaining element for R
                break
            while k<j or (k<N-1 and psum[k+1]-psum[i+1]<=psum[N]-psum[k+1]):
                k+=1
            ans+=k-j # (k-1)-j+1
            
        return ans%(10**9+7)
```

回來試試二分搜解法，第一刀的最左位置很好想，但是最右位置有夠難想，比賽碰到我八成是做不出來。  
看了好多人的文章，終於搞懂差別在哪：因為我的前綴和多了一格的[0]，所以在二分搜的位置實際上要扣掉1。  

一樣枚舉第一刀的位置i，二分搜找第二刀的最左位置L，再找第二刀的最右位置R。  
要注意的是L位置要比i大，且R的位置要比N-1小。  

參考資料：  
https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays/solution/5643-jiang-shu-zu-fen-cheng-san-ge-zi-sh-fmep/  
https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-1712-ways-to-split-array-into-three-subarrays/  
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/999157/Python3-binary-search-and-2-pointer  

```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N=len(nums)
        psum=[0]
        ans=0
        for n in nums:
            psum.append(psum[-1]+n)
        for i in range(N-2):
            L=bisect_left(psum,psum[i+1]*2)-1
            L=max(L,i+1)
            R=bisect_right(psum,psum[i+1]+(psum[-1]-psum[i+1])//2)-1-1
            R=min(R,N-2)
            ans+=max(0,R-L+1)
                        
        return ans%(10**9+7)
```

把前綴和第一個[0]砍掉，比較方便計算的二分搜版本。  

```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N=len(nums)
        psum=list(accumulate(nums))
        j=k=0
        ans=0
        for i in range(N-2):
            L=bisect_left(psum,psum[i]*2)
            L=max(L,i+1)
            R=bisect_right(psum,psum[i]+(psum[-1]-psum[i])//2)-1
            R=min(R,N-2)
            ans+=max(0,R-L+1)
                        
        return ans%(10**9+7)
```

把前綴和第一個[0]砍掉，比較方便計算的雙指針版本。  
這個版本執行1170ms，擊敗98.58%的提交。

```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N=len(nums)
        psum=list(accumulate(nums))
        j=k=0
        ans=0
        for i in range(N-2):
            while j<=i or (j<N-1 and psum[j]<psum[i]*2):
                j+=1
            if j==N-1: # no remaining element for R
                break
            while k<j or (k<N-1 and psum[k]-psum[i]<=psum[-1]-psum[k]):
                k+=1
            ans+=k-j # (k-1)-j+1
            
        return ans%(10**9+7)
```