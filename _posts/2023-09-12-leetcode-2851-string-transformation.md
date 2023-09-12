---
layout      : single
title       : LeetCode 2851. String Transformation
tags        : LeetCode Hard Array String Matrix Math DP
---
周賽362。最近真的很喜歡出競賽的東西，面試中考這種就是不錄取的意思吧。  

## 題目

輸入兩個長度皆為n的字串s和t。你可以對s執行以下操作：  

- 從s中移除長度為l的**後綴**，並將其移到s的左方。其中l滿足0 < l < n  
- 例如s = 'abcd'，可以移除後綴'cd'然後加到前方，操作完成後s =  'cdab'  

另外還輸入整數k。求**正好**執行k次操作後，有多少種方式能夠使s等於t。  

答案很大，先模10^9+7後回傳。  

## 解法

題目規定後綴不可以為空，也不可以是整個s，這兩種選擇都會使s保持不變。  
將後綴搬到前方，其實可以把s看做一個頭尾相連的循環字串，只是改變字串的起點索引而已。例如：  
> s = 'abcd'移除後綴'cd'  
> 等價於s = s[2:] + s[:2]  

為了方便處理循環字串，且避免s被匹配到兩次，可以將s重複兩次，並去除最後一個字元，變成ss = s+s[:-1]。  
這下我們只要在ss中，找到能夠所有作為字串t的起點索引，將這些索引稱為**好索引**。  
只要停在任意好索引i上，則可以保證s[i:]+s[:i]，也就是ss[i:i+N]等於t。  
但是s有夠長，只能選O(N)的字串匹配演算法，像是KMP或Rabin-Karp都行。這裡選擇前者。  

在s中共有n個索引可以作為開頭，其中有good個**好索引**；反之，剩餘 n - good = bad個都是**壞索引**。  
定義dp[i][0]為：第i次操作後，停在**好索引**上的方法數；而dp[i][1]為停在**壞索引**上的方法數。  

如果操作後想停在好索引上，只能從**自己以外的好索引**或是**壞索引出發**；想停在壞索引上，只能從**好索引**或是**自己以外的壞索引**出發。  
得到轉移方程式：  

- dp[i][0] = dp[i-1][0] \* (good-1) + dp[i-1][1] \* (good)  
- dp[i][1] = dp[i-1][0] \* (bad) + dp[i-1][1] \* (bad-1)  

base cases取決於s和t是否相等，因為dp[0]代表操作0次，也就是初始值。  
若s=t，則只能停在好索引上；否則只能停在壞索引上。  

又但是k高達10^15，普通的dp是O(N)，還是不夠快。這時必須將轉移方程式變成**矩陣乘法**，然後套用**矩陣快速冪**。  
等我哪天搞懂再來補詳解。  

時間複雜度O(n + log k)。  
空間複雜度O(n)。  

```python
MOD=10**9+7

def nextTable(p):
    N = len(p)
    table = [0]*(N+1)
    table[0] = -1
    i, j = 1, 0
    while i < N:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            table[i] = j
        else:
            j = table[j]
    return table

def KMP(s, p):  # search p in s
    cnt=0
    M, N = len(s), len(p)
    i = j = 0
    table = nextTable(p)
    while i < M :
        if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
        else:
            j = table[j]
        if j==N:
            cnt+=1
            j=table[j]
    return cnt

def countGood(s,t):
    ss=s+s[:-1]
    return KMP(ss,t)

def matrixPower(base,p):
    res=[[1,0],[0,1]]
    while p>0:
        if p&1:
            res=matrixMultiply(res,base)
        p//=2
        base=matrixMultiply(base,base)
    return res

def matrixMultiply(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            c[i][j]=a[i][0]*b[0][j] + a[i][1]*b[1][j]
            c[i][j]%=MOD
    return c

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        N=len(s)
        good=countGood(s,t)
        bad=N-good
        
        # dp[i][0] = dp[i-1][0]*(good-1) + dp[i-1][1]*(good)
        # dp[i][1] = dp[i-1][0]*(bad) + dp[i-1][1]*(bad-1)
        
        mat=[
            [good-1,good],
            [bad,bad-1]
        ]
        
        mat=matrixPower(mat,k)
        
        if s!=t:
            return mat[0][1]
        else:
            return mat[0][0]
```
