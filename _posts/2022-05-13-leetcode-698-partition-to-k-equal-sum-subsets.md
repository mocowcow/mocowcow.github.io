--- 
layout      : single
title       : LeetCode 698. Partition to K Equal Sum Subsets
tags        : LeetCode Medium Array Backtracking 
---
複習以前寫過比較難搞的回溯題。加了新測資，舊方法直接變成TLE，只好找找別的出路。

# 題目
輸入整數陣列nums和整數k，如果可以把nums分成k個總和相等的非空子集合，則回傳true。

# 解法
先講舊方法，複雜度為O(k^N)，現在已經TLE，無法使用。  

要想平分成k個子集合，得先確認nums的總和是否能被k整除，若無法整除直接回傳false。  
建立長度k的陣列sub，代表各個子集合，使用回溯法暴力搜尋，試著將每個數字nums[i]加到各個子集合中。  
nums長度為N，從i=0開始進入，直到i等於N時，代表所有數字都已經分配到不同子集合中，這時檢查k個子集合是否都為平均值avg，若是則更新答案為true。

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        avg = sum(nums)//k
        N = len(nums)
        sub = [0]*k
        flag = False

        def bt(n):
            nonlocal flag
            if n == N:
                for x in sub:
                    if x != avg:
                        return
                flag = True
            else:
                for i in range(k):
                    if sub[i]+nums[n] <= avg:
                        sub[i] += nums[n]
                        bt(n+1)
                        sub[i] -= nums[n]

        bt(0)

        return flag
```

上面的回溯一次嘗試組成k個子集合，指數上去成長太快了。  
參考了[這篇](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-x-2)的第一個方法，改成一次只組成一個總合為avg的子集合，成功後才嘗試下一個，直到滿足k個為止。  

我們不在乎子集合的組成與順序，只要他總和等於avg就行，那麼可以先將nums以遞減排序，盡可能先使用較大的數，減少無謂的分支。  
其實這有點像是top down dp的感覺了。
定義回溯函數bt(i,curr,k)：i為nums中的起始索引，curr為當前子集合總和，k為剩下需要的子集合。  
base case：k為1時，剩下的數字剛好可以湊成avg，直接回傳true。  
否則從索引i開始，試著將i\~N-1的未使用數字加入當前子集合中。子集合總和剛好為avg時，則遞迴建立下一個子集合。  

和其他回溯題型一樣，本題也有關鍵的剪枝加速點：  
因為我們是從nums[0]開始循序嘗試到nums[N-1]，若nums[i]和nums[i-1]數值都是5，且5可以用來組成子集合的話，nums[i-1]一定會先被使用掉。  
所以碰到nums[i]等於nums[i-1]，且nums[i-1]沒被使用的情況下，可以知道nums[i-1]無法加入子集合，那麼和nums[i-1]同值的nums[i]當然也無法被加入，所以直接不處理nums[i]。

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm=sum(nums)
        if sm%k!=0:
            return False
        N=len(nums)
        nums.sort(reverse=1)
        used=[False]*N
        avg=sm//k
        
        def bt(i,curr,k):
            if k==1:
                return True
            if curr==avg:
                return bt(0,0,k-1)
            for j in range(i,N):
                if used[j] or curr+used[j]>avg:
                    continue
                if j>0 and nums[j]==nums[j-1] and not used[j-1]:
                    continue
                used[j]=True
                if bt(j+1,curr+nums[j],k):
                    return True
                used[j]=False
            return False
                
        return bt(0,0,k)
```

更新bitmask DP解法。看了中文站才發現遺漏一個重要的剪枝條件：nums中不可以有超過avg的數字。  

以bitmask表示那些數字已經用過了，從0開始bottom up，每次挑一個沒用過數字試著加入。  
當前子集合的總和記錄在val陣列裡面，對val[mask]的值模avg，可以計算出當前正在組成的子集合總和。  

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm=sum(nums)
        if sm%k!=0: # 剪枝，必須能夠整除
            return False
        avg=sm//k
        for x in nums: # 剪枝，數字不可超過avg
            if x>avg:
                return False
        nums.sort()
        N=len(nums)
        dp=[False]*(1<<N)
        dp[0]=True
        val=[0]*(1<<N)
        
        for mask in range(1<<N):
            if not dp[mask]: # 須以合法的組合為基礎
                continue
            for i in range(N):
                newMask=mask|(1<<i)
                if newMask!=mask: # 沒用過的數字
                    subSum=(val[mask]%avg)+nums[i] 
                    if subSum<=avg: # 且可以放入集合
                        dp[newMask]=True
                        val[newMask]=subSum
                    else: # 剪枝，後面元素都不可用了
                        break
        
        return dp[-1]
```
