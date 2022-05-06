--- 
layout      : single
title       : LeetCode 828. Count Unique Characters of All Substrings of a Given String
tags        : LeetCode Hard String DP
---
忘記在哪看到人家說是[2262. total appeal of a string]({% post_url 2022-05-01-leetcode-2262-total-appeal-of-a-string %})的相似題，但至少和我的解法不同，不是很確定相似在哪裡。

# 題目
定義函數countUniqueChars(s)，會回傳s中有幾個**只出現一次的字元**。例如countUniqueChars("LEETCODE")，只出現一次的字元有["L","T","C","O","D"]，所以回傳5。  
輸入字串s，對s的所有子字串傳入countUniqueChars，並回傳加總值。

# 解法
我用的是和[2104. sum of subarray ranges]({% post_url 2022-05-06-leetcode-2104-sum-of-subarray-ranges %})相同的概念，計算每個位置字元的貢獻值。  
與其計算子字串能產生的值，不如計算每個位置的字元能提供多少值。  

先遍歷一次s，依字元將索引分類，再對每個分類好的索引計算貢獻值，例：  
> s='abacba'  
> a的索引=[0,2,5]  
> 位於0的a左邊有0個元素，右邊有1個元素可以組成子陣列，共1*2=2  
> 位於2的a左邊有1個元素，右邊有2個元素可以組成子陣列，共2*3=6  
> 位於5的a左邊有2個元素，右邊有0個元素可以組成子陣列，共3*1=3  
> b的索引=[1,4]  
> 位於1的b左邊有1個元素，右邊有2個元素可以組成子陣列，共2*3=6  
> 位於4的b左邊有2個元素，右邊有1個元素可以組成子陣列，共3*2=6  
> c的索引=[3]  
> 位於3的c左邊有3個元素，右邊有2個元素可以組成子陣列，共4*3=12  
> 總答案為2+6+3+6+6+12=35

```python
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        N=len(s)
        d=defaultdict(list)
        for i,n in enumerate(s):
            d[n].append(i)
        
        ans=0
        for k in d:
            idx=[-1]+d[k]+[N]
            for i in range(1,len(idx)-1):
                ans+=(idx[i]-idx[i-1])*(idx[i+1]-idx[i])
                
        return ans
```
