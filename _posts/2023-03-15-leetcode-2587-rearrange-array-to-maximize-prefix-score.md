--- 
layout      : single
title       : LeetCode 2587. Rearrange Array to Maximize Prefix Score
tags        : LeetCode Medium Array PrefixSum Sorting Greedy
---
模擬周賽336。不知道為什麼一堆人拿WA，或許因為**0不是正數**。  

# 題目
輸入整數陣列nums。你可以將nums重新任意排序。  

令prefix為一個陣列，包含nums重新排列後的所有前綴和。也就是說，prefix[i]是第0到第i個元素之和。  
而nums的**分數**為prefix中正整數的個數。  

求可以得到的**最大分數**。  

# 解法
前綴和是從左方向右累加的。因此若要使得多個前綴和為正數，則應當將nums遞減排序，使得正數集中在左方，之後逐次加入較小的負數。  
在算前綴和的過程中，若為**正數**則將答案加1。注意正數指大於0的數。  

時間複雜度瓶頸為排序O(N log N)。空間複雜度O(1)。  

```python
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ps=0
        ans=0
        
        for n in nums:
            ps+=n
            if ps>0:
                ans+=1
                
        return ans
```
