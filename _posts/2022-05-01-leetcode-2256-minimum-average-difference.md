--- 
layout      : single
title       : LeetCode 2256. Minimum Average Difference
tags        : LeetCode Medium Array PrefixSum
---
雙周賽77。誤會題目WA一次，邏輯錯誤WA一次，提交的時候手不小心敲到鍵盤RE一次，好慘。

# 題目
輸入陣列nums，求nums的**最小平均差**在哪個索引位置。  
**平均差**指的是在某個位置i，將前i+1個數字分到左半邊，剩下的在右半邊，兩邊**平均值**向下取整，相減後的絕對值。  
如果有多個位置平均差相同，則選擇索引最小者。

例：  
> nums = [2,5,3,9,5,3]  
> i=0 絕對差=abs((2/1)-(5+3+9+5+3)/5)=3  
> ..  
> i=5 絕對差=abs((2+5+3+9+5+3)/6-0)=4

# 解法
i=0時左方1個數字，右方N-1個數字，i=N-2時左方N-1個數字，右方1個數字，這個範圍可以用迴圈處理。  
注意i=N-1時，所有數字都會被分到左方，右方為空，沒注意到的話會出現分母0錯誤。  
我想說一開始就先處理，結果忘記要優先選較小的索引，吃了一次WA。  

用lc,rc紀錄左右方的數字數量，ls,rs紀錄左右方的總和，倆倆相除得到平均值，再拿去算絕對差。  
因為要選擇較小的索引，所以只有在當前i絕對差更小時才更新答案。

比賽時趕時間，還改了兩次，用最暴力的方法，還多了些不必要處理AC程式碼。  

```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N=len(nums)
        if N==1:
            return 0
        lc=0
        ls=0
        rc=N
        rs=sum(nums)
        ans=None
        mn=math.inf
        for i in range(N-1):
            n=nums[i]
            ls+=n
            lc+=1
            rs-=n
            rc-=1
            la=ls//lc
            ra=rs//rc
            aa=abs(la-ra)
            if aa<mn:
                mn=aa
                ans=i
            
        if sum(nums)//N<mn:
            ans=N-1
        
        return ans
```

其實左右兩邊的數量不必自己計算，明明題目就有告訴你左方是i+1個，右方是N-i-1個。

```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        ls=0
        rs=sm=sum(nums)
        ans=mn=math.inf
        for i in range(N-1):
            ls+=nums[i]
            rs-=nums[i]
            diff=abs(ls//(i+1)-rs//(N-i-1))
            if diff<mn:
                mn=diff
                ans=i
                
        if sm//N<mn:
            return N-1
        else:
            return ans
```