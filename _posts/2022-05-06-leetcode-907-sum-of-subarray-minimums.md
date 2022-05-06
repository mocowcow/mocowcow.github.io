--- 
layout      : single
title       : LeetCode 907. Sum of Subarray Minimums
tags        : LeetCode Medium Array Stack MonotonicStack
---
[2104. sum of subarray ranges]({% post_url 2022-05-06-leetcode-2104-sum-of-subarray-ranges %})相似題，原來我一年前就寫過，不知道那時候腦子是裝了什麼東西才想得出來。

# 題目
輸入字串arr，求arr所有**子字串中最小值**的總和。答案可能很大，先模10^9+7後再回傳。

# 解法
先在arr左右兩方加上-inf，方便處理邊界。  
維護單調遞增堆疊st，遍歷arr中所有數字n及索引right，若st頂端元素的值小於n，代表其無法作為最小值繼續出現，將其彈出處理：  
彈出值記為mid，再將st頂端索引記為left。mid左方可以連續找到(mid-left)個較大元素，右方可以連續找到(right-left)個較大元素。  
公式計算出mid作為最小值，會出現在(mid-left)*(right-left)個子陣列中，再乘上mid對應的值，即為其對答案的貢獻值。

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=0
        arr=[-math.inf]+arr+[-math.inf]
        st=[]
        for right,n in enumerate(arr):
            while st and n<arr[st[-1]]:
                mid=st.pop()
                left=st[-1]
                ans+=(mid-left)*(right-mid)*arr[mid]
            st.append(right)
                
        return ans%(10**9+7)
```
