--- 
layout      : single
title       : LeetCode 2514. Count Anagrams
tags        : LeetCode Hard String Math HashTable
---
雙周賽94。之前看過atlassian考類似的題目，當時只想說：**這誰他媽面試做得出來**。沒想到兩個月內就來討債了。  

# 題目
輸入由一個或多個單字所組成的字串s。每個單字之間都由一個空格符號" "分隔。  

如果字串t中第i個單字的是s中第i個單字的**排列**，則稱之為**易位構詞**。  
- 例如"acb dfe"是"abc def"的易位構詞，但"def cab"和"adc bef"則不是  

求s有多少**不同**的易位構詞，答案可能很大，先模10^9+7後回傳。  

# 解法
從例題的s = "too hot"：  
> too排列 = too, oto, oot  
> hot排列 = hot, hto, oht, oth, hto, hot  
> 共3*6 = 18種  

可以看出來，每個單字之間都是相互獨立的：只要將s分割成數個單字，分別計算其不重複排列之後，以乘法原理相乘得到答案。  
對於一個長度為n的單字，全排列數量為n!。但要去除重複，所以某字元若出現v次，則要除以該字元全排列v!。  
以too為例：  
> too全排列 = 3! = 6  
> t全排列 = 1!  
> o全排列 = 2!  
> 3! / (1!2!) = 3
難點在於求字串不重複排列的時，不取餘數會溢位；取餘數又會造成除法結果錯誤，我就卡死了。  

雖說python支援超大數運算，但我還真沒想到直接暴力乘下去還在時間限制內。不知該說是python強還是測資爛，真是有夠傻眼。  

```python
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD=10**9+7
        ans=1
        
        for w in s.split():
            d=Counter(w)
            permu=factorial(len(w))
            for v in d.values():
                permu//=factorial(v)
            ans=(ans*permu)%MOD
            
        return ans
```

正統的解法之後再補。  