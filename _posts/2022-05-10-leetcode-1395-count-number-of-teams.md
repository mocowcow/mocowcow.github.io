--- 
layout      : single
title       : LeetCode 1395. Count Number of Teams
tags        : LeetCode Medium Array BIT
---
忘記是哪題的相似題，加入代辦清單之後就不記得了，反正就是多寫幾次。

# 題目
有n個士兵排成一列，且每個士兵都被分配了一個獨特的等級值。  
你必須根據以下規則來將士兵分組：  
- 選擇三個士兵，索引分別為i,j,k，且i<j<k
- 必須滿足rating[i]<rating[j]<rating[k]或是rating[i]>rating[j]>rating[k]

求有多少可以分組的方法。

# 解法
要三個不同的數，呈現嚴格遞增或遞減，最簡單的方法是三個迴圈列舉(i,j,k)組合並判斷，複雜度O(N^3)。  
聽說一開始N只有100，所以還不會超時，現在變成1000，這種方法肯定是不行。  

將暴力法稍微改進一下，變成列舉中間點，然後分別計算左右大小數，倆倆相乘就是可行的組合數。  
題目有特別提到，每個數字都是獨特的，意味著不需要考慮數字相等的問題。因此，若左方較小數有x，那麼左方較大數則為(左方總數-x)。

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N=len(rating)
        ans=0
        
        for i in range(1,N-1):
            lsmall=rsmall=0
            for j in range(i):
                if rating[j]<rating[i]:
                    lsmall+=1
            for j in range(i+1,N):
                if rating[j]<rating[i]:
                    rsmall+=1
            lbig=i-lsmall
            rbig=N-i-1-rsmall
            ans+=(lsmall*rbig)+(lbig*rsmall)
            
        return ans
```

使用BIT來計算較小的數。  
lt和rt分別記錄左右方的數字，一開始要先遍歷一次rating，全部加入rt裡面做初始化。  
之後再遍歷一次rating的每個數字n，計算出可用的組合數量後，對lt加入n，對rt扣除n。

```python
class BinaryIndexedTree:

    def __init__(self, n):
        self.bit = [0]*(n+1)
        self.N = len(self.bit)

    def update(self, index: int, val: int) -> None:
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    def prefixSum(self, index: int) -> None:
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N=len(rating)
        lt=BinaryIndexedTree(10**5+5)
        rt=BinaryIndexedTree(10**5+5)
        ans=0
        
        for r in rating:
            rt.update(r,1)
        
        for i,n in enumerate(rating):
            lsmall=lt.prefixSum(n-1)
            rsmall=rt.prefixSum(n-1)
            lbig=i-lsmall
            rbig=N-i-1-rsmall
            ans+=(lsmall*rbig)+(lbig*rsmall)
            lt.update(n,1)
            rt.update(n,-1)
            
        return ans
```