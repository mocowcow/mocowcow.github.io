--- 
layout      : single
title       : LeetCode 2342. Max Sum of a Pair With Equal Sum of Digits
tags        : LeetCode Medium Array HashTable Sorting
---
周賽302。一開始被nums[i]上限的10^9嚇到，結果只是虛驚一場。  

# 題目
輸入整數陣列nums。你可以選擇兩個索引i和j，其中i!=j，且nums[i]的位數和等於nums[j]的位數和。  
回傳nums[i]+nums[j]所有可能中的最大值。  

# 解法
只能選擇位數和相同的兩個數字，意味著必須先將數字以位數和分組。  

首先撰寫雜湊函數f，用以計算出數字n的位數和。遍歷nums，將所有n以其雜湊值裝到雜湊表d中。  
分類完成後，查看d中所有分類好的數字，如果各分類中的數字滿足2個以上，才有可能用來組成答案中的nums[i]+nums[j]。這時將該組別的數字排序，取出最大兩者，相加後更新答案。  

```python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def f(n):
            h=0
            while n>0:
                h+=n%10
                n//=10
            return h
        
        ans=-1
        d=defaultdict(list)
        for n in nums:
            h=f(n)
            d[h].append(n)
            
        for v in d.values():
            if len(v)>1:
                v.sort(reverse=True)
                ans=max(ans,v[0]+v[1])
        
        return ans
```

雜湊函數也可以換成以下的寫法，看起來比較短，但不一定比較好理解。  

```python
def f(n):
    h=0
    while n>0:
        n,r=divmod(n,10)
        h+=r
    return h

def f(n):
    return sum(map(int,str(n)))
```