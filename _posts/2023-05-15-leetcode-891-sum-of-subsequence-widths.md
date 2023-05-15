--- 
layout      : single
title       : LeetCode 891. Sum of Subsequence Widths
tags        : LeetCode Hard Array Sorting DP
---
相似題[2681. power of heroes]({% post_url 2023-05-14-leetcode-2681-power-of-heroes %})。  

# 題目
一個序列的**寬度**指的是序列中最大值和最小值的差。  

輸入整數陣列nums，求nums中所有**非空子序列**的**寬度**總和。答案很大，先模10^9+7後回傳。  

# 解法
順序不影響答案，總之先排序。  

遍歷排序好的nums，窮舉每個nums[i]作為最大值，並維護先前出現過的最小值貢獻。  
以[1, 2, 3, 4]為例：  
- 加入1，mn = []  
- 加入2，mn = [1\*2<sup>0</sup>]  
- 加入3，mn = [1\*2<sup>1</sup> + 2\*2<sup>0</sup>]  
- 加入4，mn = [1\*3<sup>1</sup> + 2\*2<sup>2</sup> + 3\*2<sup>0</sup>]  

發現一個規律，每加入一個新的元素x，上一次的mn會先變成兩倍再加上x。  
每當我們加入nums[i]，這時以nums[i]為最大值的子序列會有2<sup>i</sup>個，扣除掉其本身，對最大值貢獻應是nums[i] \* 2<sup>i</sup>。  
維護最小值貢獻mn以及最大值貢獻次數cnt，一邊遍歷nums一邊更新答案。  

瓶頸是排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD=10**9+7
        nums.sort()
        
        ans=0
        mn=0
        cnt=1
        for x in nums:
            ans+=cnt*x-x-mn
            ans%=MOD
            cnt*=2
            cnt%=MOD
            mn=mn*2+x
            mn%=MOD
            
        return ans
```
