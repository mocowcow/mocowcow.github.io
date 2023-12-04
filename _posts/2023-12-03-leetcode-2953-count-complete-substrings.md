---
layout      : single
title       : LeetCode 2953. Count Complete Substrings
tags        : LeetCode Medium String SlidingWindow TwoPointers HashTable
---
周賽374。昨晚才練習分組循環，今天就給我碰上。  

## 題目

輸入字串s，以及整數k。  

一個**完整**的子字串s滿足：  

- 每種在s中出現的字元都**正好**出現k次  
- 每兩個相鄰的字元，其絕對差最多為2  

求word有多少**完整**的子字串。  

## 解法

只要有兩個相鄰字元絕對差超過2，那麼就可以不管怎樣，子字串都不可能超過這個邊界。  
例如："...a|d..."，可是看做兩個獨立的字串"...a"和"d..."，分別在裡面找字元正好出現k次的子字串。  

總共只有26種字母，如果只包含一種，那子字串長度就是k，兩種就是2k，以此類推。  
對於剛才分組完的字串中，只要在裡面以滑動窗口分別找長度為k\~26k的子字串即可。  
先用一個雜湊表d做窗口內字元的出現次數，另外一個變數ok記錄**正好k次的字元個數**。如果ok等於字元種類，則答案加1。  

順帶一提，如果某字元c出現超過k次，這時候ok不需要特別去減少也沒關係。因為窗口大小正好是k\*字元種類，當c多佔用了其他字元的出現次數，必定使得其他字元c'無法達到k次。  

時間複雜度O(N \* 26)。  
空間複雜度O(26)。  

```python
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        N=len(word)
        
        def f(s,e,char_cnt): # char_cnt different chars appear k times
            size=char_cnt*k
            if e-s+1<size:
                return 0
            res=0
            d=Counter()
            ok=0 # appear exactly k times
            left=s
            for right in range(s,e+1):
                c=word[right]
                d[c]+=1
                if d[c]==k:
                    ok+=1
                if right-left+1==size:
                    if ok==char_cnt: # all k times
                        res+=1
                    if d[word[left]]==k:
                        ok-=1
                    d[word[left]]-=1
                    left+=1
            return res
        
        ans=0
        i=0
        while i<N:
            j=i
            while j+1<N and abs(ord(word[j])-ord(word[j+1]))<=2:
                j+=1
            for char_cnt in range(1,27): # find k ~ 26k in s[i, j]
                ans+=f(i,j,char_cnt)
            i=j+1
                
        return ans
```
