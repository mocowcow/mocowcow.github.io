--- 
layout      : single
title       : LeetCode 2338. Count the Number of Ideal Arrays
tags        : LeetCode Hard Array Math
---
周賽301。花了一個禮拜才一知半解，最大的收穫可能還是觀察出數列規則的方法，會不會做出排列組合反而不是重點。  

# 題目
輸入兩個整數n和maxValue，用來生成**理想陣列**。

若長度n的陣列arr滿足以下條件，則稱為是**理想陣列**：
- 每個arr[i]是一個從1到maxValue的值，0 <= i < n  
- 每個arr[i]都可以被arr[i-1]整除，0 < i < n  

回傳長度為n的不同**理想數組**的數量。答案可能非很大，先模10^9+7後回傳。  

# 解法
原本只想出單純的dp方法，對於長度為n，最末端數值為v的陣列，可以透過加總長度n-1且最末端數值為v因數求出。  
複雜度為O(n*maxValue^2)，若兩者代入1000，大概是10^9，當然是超時的。  

```python
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(n,v):
            if n==1:
                return 1
            cnt=dp(n-1,v)
            for i in range(1,v//2+1):
                if v%i==0:
                    cnt+=dp(n-1,i)
            return cnt%MOD

        ans=0        
        for i in range(1,maxValue+1):
            ans=(ans+dp(n,i))%MOD
    
        return ans
```

[參考解答](https://leetcode.cn/problems/count-the-number-of-ideal-arrays/solution/shu-lun-zu-he-shu-xue-zuo-fa-by-endlessc-iouh/)提到，以數字x結尾的長度n陣列，會將x個質因數分散在n個位置中。  
這相當於把問題拆分成x個[隔板法](https://zh.wikipedia.org/zh-mo/%E9%9A%94%E6%9D%BF%E6%B3%95)子問題。  

例如以8結尾，長度為4的陣列，要將質因數2,2,2塞在任意四個位置，所以有C(4+3-1,3)種放法。若有多種質因數，因為不會互相干擾，直接相乘即可。  

不過質因數分解的方法也很重要，我自己寫的分解法只通過46/47測資，換成和題解一樣的寫法才過。  

```python
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD=10**9+7
        
        def prime(n):
            freq=[]
            p=2
            while p*p<=n:
                if n%p==0:
                    cnt=1
                    n//=p
                    while n%p==0:
                        cnt+=1
                        n//=p
                    freq.append(cnt)
                p+=1
            return freq+(n>1)*[1]
            
        ans=0
        for i in range(1,maxValue+1):
            num=1
            for k in prime(i):
                num=(num*comb(n+k-1,k))%MOD
            ans=(ans+num)%MOD
            
        return ans
```
