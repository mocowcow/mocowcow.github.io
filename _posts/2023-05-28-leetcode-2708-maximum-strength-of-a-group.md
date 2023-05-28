--- 
layout      : single
title       : LeetCode 2708. Maximum Strength of a Group
tags        : LeetCode
---
雙周賽105。這題還挺微妙的，因為測資範圍很小，所以方法也很多種，而且每種的實現難度都有一段差距。  

# 題目
輸入整數陣列nums，代表每個學生的考試分數。  
老師想要組一個**非空**的學生團體，使得這個團體的**實力**最大化。實力的定義為團體中所有成員分數的乘積。  

求團體的最大實力值。  

# 解法
雖然看到學生最多才13個，確定可以用回溯法。但實力是相乘，如果初始實力代0會算錯，代1又沒辦法判斷空集合，卡住一陣子。  
後來才想通只要在全域紀錄各學生的選擇狀態，更新答案的時候遍歷就知道是不是空集合。  

維護回溯函數bt(i)，代表第i個學生選或不選，如果要選就把used[i]設成true。當i等於N時代表都處理完，把所有選到的學生成績相乘，得到實力值後更新答案。  

N個元素可選可不選，共有2^N種選法，每次構造答案需要O(N)。時間複雜度O(2^N\*N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        N=len(nums)
        used=[False]*N
        ans=-inf
        
        def bt(i):
            nonlocal ans
            if i==N:
                if sum(used)==0: # empty
                    return
                score=1
                for i in range(N):
                    if used[i]:
                        score*=nums[i]
                ans=max(ans,score)
                return
            bt(i+1)
            used[i]=True
            bt(i+1)
            used[i]=False
            
        bt(0)
        
        return ans
```

後來想想，根據回溯函數bt的順序，如果總是先嘗試**不選**，之後才嘗試**選**的話，第一個被構造出的答案一定是空集合。  
那麼可以先保存所有實力值，取第一個結果以外的實力值就可以。  

時間複雜度O(2^N\*N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans=-inf
        N=len(nums)
        ans=[]
        
        def bt(i,score):
            nonlocal ans
            if i==N:
                ans.append(score)
                return
            bt(i+1,score)
            bt(i+1,score*nums[i])
        
        bt(0,1)
        
        return max(ans[1:])
```