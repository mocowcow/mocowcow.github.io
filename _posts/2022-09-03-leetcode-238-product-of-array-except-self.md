--- 
layout      : single
title       : LeetCode 238. Product of Array Except Self
tags        : LeetCode Medium Array PrefixSum
---
隨機練習題。好像只有以前才會出這種限制運算規則的題，雖然他也沒有在oj裡面去禁止就是了。

# 題目
輸入整數陣列nums，回傳數組answer，使得answer[i]等於nums中除了nums[i]以外的所有元素乘積。  

你必須使用O(N)的演算法，且不可使用除法運算。  

# 解法
本來看完題目名稱就想好解法了：先算出nums連乘總和，而answer[i]就是總乘積除以nums[i]。  
結果最後一行告訴我們**不能用除法**。  

試想以下情況，底線\_代表不乘：  
> nums = [1,2,3]  
> ans[0] = [\_,2,3]  
> ans[1] = [1,\_,3]  
> ans[2] = [1,2,\_]  

可以發現ans[i]=**開頭到i-1為止的連乘**乘上**i+1開始到結尾的連乘**。  
那麼我們可以做兩次前綴和，分別是從左到右連乘，和從右到左連乘(或許該說後綴和?)，能夠在O(1)的時間內求出ans[i]，進而符合整體O(N)的要求。  

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        l_sum=nums[:]
        r_sum=nums[:]
        ans=[0]*N
        
        for i in range(1,N):
            l_sum[i]*=l_sum[i-1]
            
        for i in range(N-2,-1,-1):
            r_sum[i]*=r_sum[i+1]
            
        for i in range(N):
            prod=1
            if i>0:
                prod*=l_sum[i-1]
            if i+1<N:
                prod*=r_sum[i+1]
            ans[i]=prod
            
        return ans
```

follow up要求：以O(1)空間複雜​​度解決問題。ans陣列不算入額外空間。  
那麼只要直接在ans陣列上做修改，不儲存左右前綴和結果即可。  

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[1]*N
        
        ps=1
        for i in range(1,N):
            ps*=nums[i-1]
            ans[i]=ps
            
        ps=1
        for i in range(N-2,-1,-1):
            ps*=nums[i+1]
            ans[i]*=ps
            
        return ans
```
