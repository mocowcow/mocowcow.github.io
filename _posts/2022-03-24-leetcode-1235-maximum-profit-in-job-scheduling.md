---
layout      : single
title       : LeetCode 1235. Maximum Profit in Job Scheduling
tags 		: LeetCode Hard DP Sorting
---
和[2008]({% post_url 2022-03-24-leetcode-2008-maximum-earnings-from-taxi %})同一個概念，只是沒有很親切提供終點在哪，比較容易當成背包問題考慮。

# 題目
你有n項工作，起始、結束、利潤分別存在對應的startTime, endTime, profit陣列裡面。如何安排工作排程並將利潤最大化，求最大利潤為多少。

# 解法
先將三個陣列綁起來，並以結束時間排序。
有N項工作，dp(i)代表處理完第i項工作後的最大利潤。  
dp(0)沒有和其他衝突，直接就是第0項工作的利潤。其他剩餘的工作i，有三種情況：  
1. 放棄不做，最大利潤維持跟dp(i-1)一樣  
2. 做，但是會卡掉先前所有工作，只剩下一筆利潤  
3. 做，但先前有部分工作不能做，只能從前面某項工作dp(j)接著做

所以對每個i先以狀況1和2較大者初始化，之後再往前找哪項工作j可以在i工作開始前結束，以dp(j)+profit[i]更新dp(i)。  
最後dp[N-1]就是答案。

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:    
        jobs=sorted(zip(startTime,endTime,profit),key=itemgetter(1))
        N=len(jobs)
        dp=[0]*N
        dp[0]=jobs[0][2]
        
        for i in range(1,N):
            dp[i]=max(dp[i-1],jobs[i][2])
            for j in range(i)[::-1]:
                if jobs[j][1]<=jobs[i][0]:
                    dp[i]=max(dp[i],dp[j]+jobs[i][2])
                    break
            
        return dp[-1]
```

