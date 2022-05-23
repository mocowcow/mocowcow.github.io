--- 
layout      : single
title       : LeetCode 2281. Sum of Total Strength of Wizards
tags        : LeetCode Hard Array Stack MonotonicStack PrefixSum Math
---
周賽294。超級難的鬼東西，難點在於數學公式的推導。計算每個位置的貢獻值我還辦得到，測資小一點或許能過。

# 題目
你是一個王國的統治者，擁有一支巫師大軍。  
輸入索引從0開始的整數陣列strength，其中strength[i]代表第i個巫師的強度。一群**連續**的巫師(即子陣列)，其總強度定義為以下兩值的乘積：  
- 群組中最弱巫師的強度  
- 群組中所有巫師強度總和  

回傳所有巫師群組總強度之和。答案很大，先模10^9+7後再回傳。  
子陣列是陣列中元素的連續非空序列。  

# 解法
有點像是[907. sum of subarray minimums]({% post_url 2022-05-06-leetcode-907-sum-of-subarray-minimums %})，找出每個巫師i在多大範圍的子陣列中扮演著最弱的角色。  
lb陣列紀錄左邊界，初始化為-1；rb陣列紀錄右邊界，初始化為N。分別使用單調遞增堆疊由左向右、再由右向左處理一次。  

如此一來，我們便可以求出巫師i左方有i-lb[i]-1個元素，右方有rb[i]-i-1個元素，共有(i-lb[i])*(rb[i]-i)個子陣列。  
但是還要計算每個子陣列的總和，所以使用前綴和，將每個子陣列的總和乘上巫師i的強度，才加入答案。

```python
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD=10**9+7
        N=len(strength)
        # get left bound
        lb=[-1]*N
        st=[]
        for i,n in enumerate(strength):
            while st and strength[st[-1]]>=n:
                st.pop()
            if st:
                lb[i]=st[-1]
            st.append(i)
        
        # get right bound
        rb=[N]*N
        st=[]
        for i in range(N)[::-1]:
            n=strength[i]
            while st and strength[st[-1]]>n:
                st.pop()
            if st:
                rb[i]=st[-1]
            st.append(i)
            
        ps=[0]+list(accumulate(strength))
        ans=0
        for i,n in enumerate(strength):
            for l in range(lb[i]+1,i+1):
                for r in range(i,rb[i]):
                    ans+=(ps[r+1]-ps[l])*n
                    
        return ans%MOD
```

但是上面方法還不夠快，一下就TLE了。  
要再把前綴和簡化成**前綴和的前綴和**，對於每個巫師i只使用O(1)的時間求總和，總體時間複雜度O(N)。  

實際上的推導過程還搞不太懂，過幾天看能不能想通。

```python
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD=10**9+7
        N=len(strength)
        # get left bound
        lb=[-1]*N
        st=[]
        for i,n in enumerate(strength):
            while st and strength[st[-1]]>=n:
                st.pop()
            if st:
                lb[i]=st[-1]
            st.append(i)
        
        # get right bound
        rb=[N]*N
        st=[]
        for i in range(N)[::-1]:
            n=strength[i]
            while st and strength[st[-1]]>n:
                st.pop()
            if st:
                rb[i]=st[-1]
            st.append(i)
            
        ps=[0]+list(accumulate(strength))
        psps=[0]+list(accumulate(ps))
        ans=0
        for i,n in enumerate(strength):
            l=lb[i]+1
            r=rb[i]-1
            sm=(i-l+1)*(psps[r+2]-psps[i+1])-(r-i+1)*(psps[i+1]-psps[l])
            ans=(ans+n*sm)%MOD
            
        return ans
```
