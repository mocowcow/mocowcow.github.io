--- 
layout      : single
title       : LeetCode 2597. The Number of Beautiful Subsets
tags        : LeetCode Medium Array Backtracking Sorting HashTable DP
---
周賽337。好像有一段時間沒出過回溯法。如果測資大一些就是Hard題了。  

# 題目
輸入正整數陣列nums和正整數k。  

如果一個子集中沒有任意兩數絕對差為k，則稱為**美麗的**。  

求nums有幾個**非空美麗子集**。  

# 解法
N不大，最多才20，可以用回溯法暴力窮舉每個元素拿或不拿，最多2^20，差不多是10^6，還可接受。  

原本nums是無序的，選擇一個元素x時要檢查x+k和x-k有沒有拿過。把nums遞增排序後就只要檢查x-k。  
維護一個雜湊表d，記錄各元素的出現次數。而回溯函數bt(i)計算nums[i]拿或不拿，到i等於N時，所有元素都處理完畢。  
如果x-k沒有拿過，則可以選擇拿x，將d[x]加1後遞迴，然後恢復原狀。  

注意題目求的是非空子集，所以最後答案要扣掉空集合的1。  

時間複雜度O(2^N)。空間複雜度O(N)。  

```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ans=0
        d=Counter()
        
        def bt(i):
            nonlocal ans
            if i==N:
                ans+=1
                return
            bt(i+1)
            x=nums[i]
            if d[x-k]==0:
                d[x]+=1
                bt(i+1)
                d[x]-=1
        
        bt(0)
        
        return ans-1
```

如果nums中的元素不同餘於k，則**不可能差值為k**。例如：  
> nums = [1,2,3,4,5], k = 2  
> 可看作是兩個獨立的子問題  
> [1,3,5]差不為k的子集有[], [1], [3], [5], [1,5]五種  
> [2,4]差不為k的子集有[], [2], [4]三種  
> 根據乘法原理，共有5\*3 = 15種差不為k的子集  
> 扣掉空集1，答案為14種  

所以根據同餘分組g，個別用dp求出子集數量。例如：  
> g = [1,2,3,5], k = 1  
> 1可選可不選，子集有[], [1]  
> 2選了就不能選1，子集有[], [1], [2]  
> 3選了就不能選2，子集有[], [1], [2], [3], [1,3]  
> 但5和3差值不為k，所有子集都可以加上5  
> 得到[], [1], [2], [3], [1,3], [5], [1,5], [2,5], [3,5], [1,3,5]  

但nums中會出現重複元素。例如：  
> g = [1,1,2,5], k = 1  
> 所以要拿1的話共有2^freq[1]種方式(含空集)  
> 但是2和1的差為k，所以要拿2的話不能拿1  
> 只能從空集合和2^freq[2]-1種方式(不含空集)搭配，加上不拿2的方式  
> 最後的5和2差不為k，所以每個方式都可以搭配2^freq[5]種方式  

定義dp(i)為：考慮分組g中0\~i個元素時，差值不為k的子集數量。  
轉移方程式：如果g[i]和g[i-1]差值為k，則dp(i) = dp(i-1) + dp(i-2)\*(2^freq[g[i]]-1)；  
若g[i]和g[i-1]差值不為k，則dp(i) = dp(i-1)\*2^freq[g[i]]  
base cases：當i<0時，代表沒有元素，只有空集合一種。當i=0時，考慮g[i]共有2^freq[g[i]]種拿法  

每次dp的時間為O(M)，其中M為分組中的獨特元素數量。  
但最差情況下每個元素都是獨特且同餘，nums中N個元素會全部集中排序，整體時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        grp=defaultdict(list)
        for n in nums:
            grp[n%k].append(n)
            
        ans=1
        for g in grp.values():
            freq=Counter(g)
            keys=sorted(freq)
            
            @cache
            def dp(i):
                if i<0:return 1 # empty set
                x=keys[i]
                powerset=pow(2,freq[x]) 
                if i==0:return powerset # first element
                if keys[i]-keys[i-1]==k:
                    return dp(i-1)+dp(i-2)*(powerset-1)
                else:
                    return dp(i-1)*powerset
        
            ans*=dp(len(keys)-1)
            
        return ans-1
```

改成bottom up寫法。每個同餘組中至少會有一個元素，所以有兩個base case：
- dp[0]代表空集合  
- dp[1]代表只考慮第一個元素的所有拿法  

```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        grp=defaultdict(list)
        for n in nums:
            grp[n%k].append(n)
            
        ans=1
        for g in grp.values():
            freq=Counter(g)
            keys=sorted(freq)
            M=len(keys)
            dp=[0]*(M+1)
            dp[0]=1 # empty set
            dp[1]=pow(2,freq[keys[0]]) # first element
            
            for i in range(2,M+1): # start from 2nd element
                powerset=pow(2,freq[keys[i-1]])
                if keys[i-1]-keys[i-2]==k:
                    dp[i]=dp[i-1]+dp[i-2]*(powerset-1)
                else:
                    dp[i]=dp[i-1]*powerset
            
            ans*=dp[M]
            
        return ans-1
```