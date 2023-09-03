---
layout      : single
title       : LeetCode 2842. Count K-Subsequences of a String With Maximum Beauty
tags        : LeetCode Hard String Math HashTable Greedy Sorting
---
雙周賽112。這題目很爛啊，給了一個無效範圍超大的k，害我一直懷疑是不是我沒有理解正確，結果還真沒錯。  
整題幾乎就沒什麼程式邏輯，全都在考組合數學。  

## 題目

輸入字串s和整數k。  

一個**k子序列**，必須是一個長度k的s的子序列，且所有字元都是唯一的。也就是每個字元只出現一。  

定義 f(c) 是字元c在s中出現的次數。  

**k子序列**的**美麗值**是所有 f(c) 的總和，其中c為k子序列中出現的所有字元。  

例如 s = "abbbdd" 且 k = 2：  

- f('a') = 1, f('b') = 3, f('d') = 2
- 有三個k子序列  
    "abbbdd" -> "ab" 美麗值 = f('a') + f('b') = 4  
    "abbbdd" -> "ad" 美麗值 = f('a') + f('d') = 3  
    "abbbdd" -> "bd" 美麗值 = f('b') + f('d') = 5  

求所有**k子序列**中的**最大美麗值**。答案可能很大，先模10^9+7後回傳。  

注意：  

- f(c) 是指c在字串s的出現次數，而不是在k子序列中  
- 兩個k子序列中只要有任意字元c的來源索引不同，則視為不同  

## 解法

首先，s裡面最多就26種字元，**k子序列**又要求字元只出現一次，所以k超過26都不可能有合法答案的k子序列。  
更準確地說，k不可以超過s中的字元種類數，否則答案必定為0。  

而**美麗值**是由k子序列中所有字元的出現次數相乘而來，為了最大化，要優先選出現次數較多的字元。  
把所有字元的出現次數由大到小排序，優先選k個最大的相乘。  

那如果有超過k個字元都是最大出現次數，要怎麼選？  
例如 s = "aabbcc", k = 2 ：  
> 有3種字元，每種各2個，要從k堆中各選一個  
> C(3,2) = 3 種選字元方式  
> 每種字元有2種選法，共 2^k = 4 種選法  
> 答案是3 \* 4 = 12  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD=10**9+7
        d=Counter(s)
        
        if k>len(d):
            return 0
        
        freq=Counter()
        for val in d.values():
            freq[val]+=1
            
        keys=sorted(freq.keys(),reverse=True)
        ans=1
        for key in keys:
            cnt=freq[key]
            if cnt<=k:
                ans*=pow(key,cnt,MOD)
                ans%=MOD
                k-=cnt
            else:
                ans*=math.comb(cnt, k)*pow(key,k)
                ans%=MOD
                break
            
        return ans
```
