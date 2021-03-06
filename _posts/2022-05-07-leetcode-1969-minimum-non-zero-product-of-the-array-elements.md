--- 
layout      : single
title       : LeetCode 1969. Minimum Non-Zero Product of the Array Elements
tags        : LeetCode Medium Math Greedy
---
去年剛開始打周賽碰到的，很噁心的分析題，好不容易算對卻因為不懂快速冪而超時。  

# 題目
輸入整數p，你會獲得一個由1到2^(p-1)的的二進位整數陣列nums。你可以多次執行以下動作：  
- 選擇兩個不同的數字x和y  
- 將x和y相應位置的位元交換  

例如：  
> x=11**0**1, y=00**1**1  
> 交換從右方數來第二個位元  
> x=11**1**1, y=00**0**1  

求nums進行任意次交換動作後，可以得到的最小**非零**乘積。此成績模10^9+7後回傳。

# 解法
當p=1時只有一個數字1，直接輸出。  

試著找看看有沒有什麼規律：  
> p會產生2^(p-1)個數字    
> p=3, nums=[001, 010, 011, 100, 101, 110, 111]  
> 發現每個位置的1都出現(2^p)-1次  

這些位元都可以任意換位置，但要維持非零乘積，所以每個數字裡面至少要有一個1位元。  
那要怎樣換位才可以使乘積最小？試想一個數字10要拆開成兩個數字相乘：5\*5=25和1\*9=9，很明顯是拆成極大和極小的數字，可以使乘積最小化。  
再來考慮怎麼分配各(2^p)-1位元給2^(p-1)個數字：  
> p=3 每個位置有4個1位元，分給7個數字  
> 剛才說要數字盡可能大，先將一個數字塞滿1，得到'111'  
> 每個位置剩下3個1位元，分給剩下6個數字  
> 組成三個'111'，這樣會把位元1用完，剩下三個數字變成0，不合法  
> 把最後一個1位元分出去，變成'110'和'001'各三個  
> '111'加上'110'和'001'各三個=7\*6\*6\*6=1512  

最後歸納出長度為comb的nums陣列組成為：  
- 1個**全部為1**  
- (comb-1)/2個**p-1個1位元加上1個0**  
- (comb-1)/2個**p-1個0位元加上1個1**  

使用快速冪將001和100數字連乘完，再乘上111就是答案。

```python
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p==1:
            return 1
        MOD=10**9+7
        n=(2**p)-1 # n
        x=(n-1)//2 # 拆成x個1..10和0..01 再加上一個1..1
        allOnes=int('1'*p,2) # 1..1
        others=int('1'*(p-1)+'0',2)     # 1..10乘0..01
        others=pow(ans,x,MOD)
        return (others*allOnes)%MOD
```

自己做快速冪，也不用字串生成數字的版本。

```python
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p==1:
            return 1
        
        def fastPow(base,p):
            ans=1
            while p:
                if p&1:
                    ans=(ans*base)%MOD
                p//=2
                base=(base*base)%MOD
            return ans
        
        MOD=10**9+7 
        n=fastPow(2,p)-1 #共有n個數字 同時也是最大的數字
        return (n*fastPow(n-1,n//2))%MOD
```