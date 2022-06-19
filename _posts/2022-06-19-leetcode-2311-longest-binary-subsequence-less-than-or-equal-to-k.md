--- 
layout      : single
title       : LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K
tags        : LeetCode Medium String Greedy
---
周賽298。這題還真的有點腦筋急轉彎，想了一陣子才通。  
題外話，我好像常常把子序列類型的題目誤會成子陣列，今天又是寫完sliding window才發現不對。  

# 題目
輸入二進位字串s和正整數k。  
找出s的最長子序列，且符合以下規則：  
- 子序列可以有前導0  
- 空序列視為0  
- 其對應的二進位數字不超過k  

# 解法
子序列可以有前導0，當然是越多越好，畢竟全都是0，還可以增加長度。  
可是一旦有了1，後方每多一個數字都會使前方的1成長兩倍，很快就會超出k的限制，那麼何時開始拿1就是個大問題。  

看看例題1：  
> s = "1001010", k = 5  
> "00010" = 2  
> "00100" = 4  
> "00101" = 5  
> 最大長度5  

怎麼"00010"的二進值這麼小，卻可以達到最大長度？再看看例題2：  
> s = "00101001", k = 1  
> "000001" = 1  
> 最大長度6  

這次二進位值還是很小，我便猜想用貪心法由後往前遍歷，有什麼就拿什麼，只要總和不超過k就行。  
最後總結出一個簡單的貪心證明：如果你拿了某數，序列長度會立刻+1，但是前方能拿的1會減少一個；不拿，長度不變，晚點可以多拿一個。拿了也不會比不拿還虧，那就一直拿吧。  

s的長度N最多只有1000，可以先算出N個數字全都是1的大小，如果不超過k就提早回傳N。  

```python
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N=len(s)
        
        if pow(2,N)-1<=k:
            return N
        
        sm=0
        mul=1
        ans=0
        for i in range(N-1,-1,-1):
            inc=(s[i]=='1')*mul
            if inc+sm<=k:
                sm+=inc
                ans+=1
            mul*=2  

        return ans
```