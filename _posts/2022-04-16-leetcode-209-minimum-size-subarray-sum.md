---
layout      : single
title       : LeetCode 209. Minimum Size Subarray Sum
tags 		: LeetCode Medium Array SlidingWindow TwoPointers BinarySearch PrefixSum
---
二分搜學習進化第二版。不知道怎麼吐槽了，這題真的很難想到二分搜。

# 題目
輸入數列nums和整數target，求總和**等於或大於**target的連續子陣列最小長度。若無符合的答案則回傳-1。

# 解法
通常看到連續子陣列都會先想到滑動視窗。  
維護一個queue作為視窗本體，以及整數sm為視窗加總值。  
遍歷nums中的數n，每次將n加入視窗後，在滿足target的情況下，盡可能將左方多餘的數字彈出，並以現在長度更新ans。  
若最後ans沒被動過，則代表無此答案，回傳-1。

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window=deque()
        sm=0
        ans=math.inf
        for n in nums:
            window.append(n)
            sm+=n
            while window and sm-window[0]>=target:
                sm-=window.popleft()
            if sm>=target and len(window)<ans:
                ans=len(window)
        
        return ans if ans!=math.inf else 0
```

改成雙指標寫法。

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sm=0
        ans=math.inf
        for right in range(len(nums)):
            sm+=nums[right]
            while left<right and sm-nums[left]>=target:
                sm-=nums[left]
                left+=1
                
            if sm>=target:
                ans=min(ans,right-left+1)
        
        return ans if ans!=math.inf else 0
```

看了官方解答才懂二分搜要搜什麼鬼，原來是搜前綴和。  
根據這種思路，前綴和其實就是由0出發，長度不同的連續子陣列總和，而不從頭出發的連續子陣列，則可以透過兩個前綴和相減得到。  
對於每個right，以其前綴和減掉target，得到可以扣減的前綴和最大長度overflow，再以二分搜找到合適位置left。  

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N=len(nums)
        psum=[0]*(N+1)
        for i in range(N):
            psum[i+1]=psum[i]+nums[i]
            
        ans=math.inf
        for right in range(N):
            if psum[right+1]>=target:
                overflow=psum[right+1]-target
                left=bisect_right(psum,overflow)-1
                ans=min(ans,right-left+1)

        return ans if ans!=math.inf else 0
```