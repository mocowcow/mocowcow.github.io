--- 
layout      : single
title       : LeetCode 2344. Minimum Deletions to Make Array Divisible
tags        : LeetCode
---
周賽302。似乎是史上最簡單的的Q4，同時也是我第一次在30分鐘內完成四題，開心開心。  

# 題目
輸入兩個正整數陣列nums和numsDivide。  
你可以刪除nums中的任意個數字，使得nums中最小元素能夠整除numsDivide中所有元素。  
求最少的刪除次數，若不可能，則回傳-1。  

註釋：若y%x==0，則稱x整除y。

# 解法
一看nums和numsDivide<=10^5，馬上確定暴力法不可行，需要其他方式減少運算。  

我們只要使nums中的最小元素能夠整除numsDivide，而不管其他元素。換句話說，每次刪除一定是刪除最小元素，那麼可以先將nums遞增排序。  
若我們要找到某個數x，可以整除y1,y2,y3..，首先會想到的不正是最大公因數嗎？先求x為numsDivide所有數的共通gcd。而x的所有因數當然也可以整除numsDivide中所有數字。  

以上兩點加在一起，遍歷nums中所有數字n，若n為x的因數，則回傳刪除次數；否則刪除次數ans加1。  
若執行到最後則代表nums中沒有數字符合要求，則回傳-1。  

```python
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        x=numsDivide[0]
        for n in set(numsDivide):
            x=gcd(x,n)

        nums.sort()
        ans=0
        
        for n in nums:
            if x%n==0:
                return ans
            else:
                ans+=1
                
        return -1
        
```
