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

爬完一些文，幾乎都是什麼費馬小定理，模反元素之類的，強制離散數學補課。  
總而言之MOD運算只支援加減乘，如果除法要求餘的話要改用反元素，例如：  
> a/b % p  
> 等價於 a*(b^-1)  

詳細原理就不管了，只要記得某數x的模反元素為x的p-2次方模p，其中p為取餘用的質數，在這裡等同10^9+7。  

先預處理所有可能會用到的階乘，把分子和分母分開計算，最後將分母換成模反元素後相乘就是答案。  
python內建pow就是快速冪，又可以取餘數，真的是有夠噁心。  
順帶一題，pow(x, -1, p)可以直接求模反元素，等價於pow(x, p-2, p)。  

時間複雜度O(N + log(M) + log(p))，其中N為s長度，M為單字最大長度，p為質數10^9+7。字串只有26種字元，空間複雜度O(1)。

```python
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD=10**9+7
        f=[0]*100005
        f[1]=1
        
        for i in range(2,100005):
            f[i]=(f[i-1]*i)%MOD
            
        up=down=1
        for w in s.split():
            d=Counter(w)
            up=(up*f[len(w)])%MOD
            for k in d.values():
                down=(down*f[k])%MOD
                
        inv=pow(down,MOD-2,MOD)
        ans=(up*inv)%MOD
        return ans
```

換成golang自己手刻一次快速冪。  

```go
const MOD = 1e9+7

func countAnagrams(s string) int {
    ans:=1
    fact:=make([]int,100005)
    
    // precompute factorial table
    fact[0]=1
    for i:=1;i<100005;i++{
        fact[i]=(fact[i-1]*i)%MOD
    }
    
    words:=strings.Split(s," ")
    for _,w:=range words{
        ans=(ans*fact[len(w)])%MOD
        mp:=make(map[rune]int)
        for _,c:=range w{
            mp[c]+=1
        }
        for _,v:=range mp{
            ans=(ans*pow(fact[v],MOD-2))%MOD
        }
    }
    
    return ans
}

func pow(base,exp int) int {
    ans:=1
    for exp>0{
        if exp%2==1{
            ans=(ans*base)%MOD
        }
        exp/=2
        base=(base*base)%MOD
    }
    
    return ans
}
```