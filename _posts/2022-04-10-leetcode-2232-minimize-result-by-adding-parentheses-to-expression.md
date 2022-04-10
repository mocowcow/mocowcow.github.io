---
layout      : single
title       : LeetCode 2232. Minimize Result by Adding Parentheses to Expression
tags 		: LeetCode Medium String
---
周賽288。和前一題差不多機車，看到當下差點崩潰。  

# 題目
輸入字串expression，代表**數字1+數字2**的算式。  
試著在**加號左方**插入左括號，在**加號右方**插入右括號，形成一個新的合法算式，並回傳可以將運算結果最小化的新算式。若有多種算式可以達到最小值，任選其中之一即可。  

例：  
> Input: expression = "247+38"  
> Output: "2(47+38)"  
> Input: expression = "12+34"  
> Output: "1(2+3)4"  
> Input: expression = "999+999"  
> Output: "(999+999)"  

# 解法
總之先將兩個數字拆開吧。加號左邊為n1，右邊為n2。位數分別為M和N。  
先將括號不影響的狀態當作預設值，mn紀錄算式最小結果，pat紀錄最小算式。  

再來處理括號會出現乘法的情況，通過觀察，可以確定幾個規則：  
- n1**不**被左括號包含的數字，最少0個，最多M-1。以下稱為L  
- n1被左括號包含的數字，至少1個，最多M。以下稱為Lmid  
- n2被右括號包含的數字，至少1個，最多N。以下稱為Rmid  
- n2**不**被左括號包含的數字，最少0個，最多N-1，以下稱為R  

新算式的組成大致上長成這樣： L*(Lmid+Rmid)*R
特別需要注意的是，如果L或R的長度為0時，需要特別設成1，否則結果會被汙染成0。  
新算式的計算結果暫存為t，若t比mx更小，則更新mx為t，並產生新的算式。  
建立算式的時候，先建造中間(Lmid+Rmid)的部分，如果L和R長度不為0再另外加上乘法部分。  

重要，如果以L>1或是R>1來當作是否加上左右乘法的依據，會出現錯誤，例如：  
> Input: "12+34"  
> Output: "(2+3)4"  
> Expected: "1(2+3)4"  

這種情況會不小心把原本算式的1吃掉，得到一個免費WA。

```python
class Solution:
    def minimizeResult(self, expression: str) -> str:
        ss = expression.split('+')
        n1, n2 = ss[0], ss[1]
        M, N = len(n1), len(n2)
        mn = int(n1)+int(n2)
        pat = '('+expression+')'

        for l_size in range(0, M):
            for r_size in range(1, N+1):
                L = 1 if l_size == 0 else int(n1[:l_size])
                R = 1 if r_size == N else int(n2[r_size:])
                Lmid = 0 if l_size == M else int(n1[l_size:])
                Rmid = 0 if r_size == 0 else int(n2[:r_size])
                t = L*R*(Lmid+Rmid)
                if t < mn:
                    mn = t
                    pp = '('+str(Lmid)+'+'+str(Rmid)+')'
                    if l_size > 0:
                        pp = str(L)+pp
                    if r_size != N:
                        pp = pp+str(R)
                    pat = pp

        return pat
```

