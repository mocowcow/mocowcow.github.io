---
layout      : single
title       : LeetCode 2958. Length of Longest Subarray With at Most K Frequency
tags        : LeetCode Medium Array TwoPointers SlidingWindow HashTable
---
雙周賽119。非常簡單，但是測資好像有點爭議。  
題目保證了1 <= k <= nums.length，但聽說有好幾筆測資出現大於nums長度的k，害某些人噴錯。  
可能有人拿k和len(nums)取最小值，反而被這個爛東西坑了。  

## 題目

輸入整數陣列nums，還有整數k。  

一個元素x的**頻率**，指的是x在nums中的出現次數。  

若一個陣列中的每個元素頻率都**小於等於**k，則稱為**好的**。  

求最長的**好的子陣列**。  

## 解法

很經典的滑動窗口。  

從左往右枚舉索引right作為右邊界，並維護左邊界left。  
每當右邊界擴展時，會加入新元素x=nums[right]，並使其頻率增加。也就是說，頻率唯一有可能超過k的元素只有x。  
若x頻率大於k，不斷縮減左邊界。停止縮減後，以當前窗口大小更新答案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0
        d=Counter()
        left=0
        
        for right,x in enumerate(nums):
            d[x]+=1
            while d[x]>k:
                d[nums[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
            
        return ans
```
