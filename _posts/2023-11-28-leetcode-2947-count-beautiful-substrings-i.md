---
layout      : single
title       : LeetCode 2947. Count Beautiful Substrings I
tags        : LeetCode Medium Array PrefixSum Math
---
周賽373。寫完題解才發現，本次周賽的主軸是modulo，貫穿了Q124。  

## 題目

輸入字串s和正整數k。  

定義vow和con分別代表字串中母音和子音的個數。  

一個**美麗**的字串滿足：  

- vow == con  
- (vow \* con) % k == 0，換句話說，vow和con的乘積能被k整除  

求字串s中有多少**非空**的**美麗子字串**。  

## 解法

先來個暴力解，枚舉所有子字串，並維護母音子音個數，滿足條件答案就+1。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
vowel=set("aeiou")

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        N=len(s)
        ans=0
        for i in range(N):
            vow=0
            con=0
            for j in range(i,N):
                if s[j] in vowel:
                    vow+=1
                else:
                    con+=1

                if vow==con and (vow*con)%k==0:
                    ans+=1
                    
        return ans
```

先考慮子母音相同的條件。把母音視作1，子音視作-1，只要和為0就是**平衡**。  
可以聯想前綴和的常見套路：若s[:i]的總和是x，只要扣掉s[:j]同樣為x、且滿足j<i的子字串，必定可以平衡。  
例如：  
> s = "aaaba"，對應數字[1,1,1,0,1]  
> "aaaba"的平衡值為3，代表多三個母音，因此要刪掉平衡值同為3的子字串  
> "aaa"平衡值剛好為3，故"aaaba" - "aaa" = "ba"  
> "ba"是平衡子字串  

枚舉子字串右邊界i、計算前綴和的過程中，以平衡值作為鍵值計數，就可以O(1)求出以i結尾的平衡子字串數量。  
麻煩的問題在於我們現在沒有子母音的計數，那(vow \* con) % k == 0這東西怎麼搞？  

在子字串平衡的前提下，vow和con必然相等，而子字串長度L = vow + con。  
將L帶入式子，得到(L/2)^2 % k == 0。  
子字串長度L可以透過前綴和一起求出，好像有點線索。但每個L平方很麻煩，再想想有沒有辦法把它弄掉。  

關鍵在**同餘**性質，若某個L剛好能被k整除，那兩倍、三倍..只要是整數倍的L同樣也能被k整除。  
如果我們能找到滿足條件的最小L，那麼只要是平衡、且長度是L倍數的子字串就是**美麗的**。  

題目要求非空，那麼子字串長度至少為1。但又必須平衡，所以L必須是偶數。  
從2開始向上枚舉偶數L，直到第一個滿足條件的L出現為止。  
那怎麼知道子字串長度是L的倍數？就和前綴和求平衡值一樣，刪除同樣餘數的部分。例如長度為2L+3的子字串，可以扣掉3或是L+3的子字串。  

將**平衡值**和**長度和L求餘**兩項同時作為雜湊的鍵值，以前綴和計算即可。  

時間複雜度O(N + k)。  
空間複雜度O(N)。  

```python
vowel=set("aeiou")

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # L = vow + con
        # (L/2)^2 % k == 0
        # (L^2)/4 % k == 0
        # (L^2) % 4k ==0
        
        # find smallest L
        for L in range(2,1005,2):
            if L*L%(4*k)==0:
                break
                
        ans=0
        cnt=0 # vow-cont
        d=Counter()
        d[(0,0)]=1 # [cnt, size%L]
        for size,c in enumerate(s,1):
            cnt+=1 if c in vowel else -1
            key=(cnt,size%L)
            ans+=d[key]
            d[key]+=1
            
        return ans
```
