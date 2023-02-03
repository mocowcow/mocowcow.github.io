--- 
layout      : single
title       : LeetCode 2552. Count Increasing Quadruplets
tags        : LeetCode Hard Array PrefixSum
---
周賽330。想好多天終於想通，這題不管是思維還是測資範圍剛好都是我的死穴。  

# 題目
輸入大小為n的整數陣列nums，其中1\~n各出現一次。求有多少**遞增四元組**。  

如果一個四元組(i, j, k, l)符合以下條件，則稱為遞增：  
- 0 <= i < j < k < l < n  
- 且 nums[i] < nums[k] < nums[j] < nums[l]  

# 解法
一開始被名稱騙了，想說遞增應該就是ijkl遞增，然而並不是。  

和[2242. maximum score of a node sequence]({% post_url 2022-04-17-leetcode-2242-maximum-score-of-a-node-sequence %})有點相似。四個點不好處理，先預處理對於每個點左右較大、較小的數字，最後可以窮舉中間兩點(j, k)，以乘法原理得出(i, l)的數量。  

>                 /l
>          /j\   /
>        /    \k/   
>     i/

(i, j, k, l)的關係其實是這樣。  
首先處理對於所有nums[k]來說，位於右方且大於x的元素有幾個。因為x只可能為1\~n的數字，所以我們只要開n+1大小的陣列。  
維護二維陣列greater，其中greater[k][x]代表索引k右方有多少元素大於x。假設在索引k右方有y個元素大於x，那麼在索引k-1至少也有y個元素大於x，所以要倒著遍歷nums，也就是求後綴。  
相反的，維護二維陣列less，其中less[j][x]代表索引j左方有多少元素小於x，這次要正著遍歷nums。  

預處理完前後綴之後，只要窮舉中間的(j, k)，如果nums[j]>nums[k]，則找出j左邊有多少元素小於nums[k]，然後k右邊有多少元素大於nums[j]，兩者相乘就是當前(i, k)所可以產生的上升四元組，將其加入答案。  

時間複雜度O(N^2)。空間複雜度O(N^2)。  

不過這邊N高達4000，對於python來講N^2其實是很抖的，況且其實是三次N^2。我提交了三次有一次TLE，兩次都執行99XXms，實在對python不友善。  

```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N=len(nums)
        greater=[[0]*(N+1) for _ in range(N)] # greater[k][x] = 索引k右邊有幾個大於x
        less=[[0]*(N+1) for _ in range(N)] # less[j][x] = 索引j左邊有幾個小於x  
        
        for k in range(N-2,-1,-1):
            for x in range(1,N+1):
                if nums[k+1]>x:
                    greater[k][x]=greater[k+1][x]+1
                else:
                    greater[k][x]=greater[k+1][x]
        
        for j in range(1,N):
            for x in range(1,N+1):
                if nums[j-1]<x:
                    less[j][x]=less[j-1][x]+1
                else:
                    less[j][x]=less[j-1][x]
                    
        ans=0
        for j in range(1,N):
            for k in range(j+1,N-1):
                if nums[j]>nums[k]:
                    ans+=less[j][nums[k]]*greater[k][nums[j]]
        
        return ans
```
