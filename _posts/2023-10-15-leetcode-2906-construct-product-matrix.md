---
layout      : single
title       : LeetCode 2906. Construct Product Matrix
tags        : LeetCode Medium Array Matrix PrefixSum Math
---
周賽367。這題可有趣了，根據不同方法，實作的難度和程式碼量有著天大的差異。  
這種沒有hard的手速場還是穩穩地寫，沒出BUG才不會排名炸裂。  

## 題目

輸入二維整數矩陣grid，其大小為m\*n，構造一個同為m\*n的矩陣p作為grid的乘積矩陣，滿足：  

- 對於每個元素p[i][j]，等同於grid中除了grid[i][j]以外所有元素的乘積。這個乘積必須對12345取模  

回傳grid的乘積矩陣。  

## 解法

看完題我馬上想到**乘法逆元**，行雲流水打一坨，結果發現base和mod必須互質，否則找不到逆元。  
~~好險範例有幫我擋下來~~。  

但是取過模的乘積沒辦法再用除法還原，這樣沒辦法把所有乘積先預處理出來。  
最後只好先算出每一列的乘積rprod，然後前後綴分解，算出除了第r列以外其他列的乘積rp。  

至於第r列本身，再前後綴分解一次，找出前後綴乘積pref和suff，乘上rp後再對12345取模。  

計算各列的乘積需要遍歷整個矩陣，時間O(MN)。對列乘積前後綴分解需要O(M)。  
對M個列前後綴分解需要各O(N)，共O(MN)。  

時間複雜度O(MN)。  
空間複雜度O(M+N)，輸出空間不計入。  

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        M,N=len(grid),len(grid[0])
        ans=[[0]*N for _ in range(M)]
        
        rprod=[0]*M
        for r in range(M):
            prod=1
            for x in grid[r]:
                prod*=x
                prod%=MOD
            rprod[r]=prod
            
        rpref=[1]*M
        rpref[0]=rprod[0]%MOD
        for r in range(1,M):
            rpref[r]=rpref[r-1]*rprod[r]
            rpref[r]%=MOD
            
        rsuff=[1]*M
        rsuff[-1]=rprod[-1]%MOD
        for r in reversed(range(M-1)):
            rsuff[r]=rsuff[r+1]*rprod[r]
            rsuff[r]%=MOD
            
        for r in range(M):
            # prod of rows except grid[r]
            rp=1
            if r>0:
                rp*=rpref[r-1]
            if r+1<M:
                rp*=rsuff[r+1]
            rp%=MOD

            # col suff
            suff=[1]*(N+1)
            for c in reversed(range(N)):
                suff[c]=suff[c+1]*grid[r][c]
                suff[c]%=MOD
                
            # col pref and total prod
            pref=1
            for c in range(N):
                ans[r][c]=rp*suff[c+1]*pref
                ans[r][c]%=MOD
                pref*=grid[r][c]
            
        return ans
```

如果把矩陣攤平成大小MN的一維陣列a來看，若ans[r][c]對應到a[i]，那麼其乘積正是a[0, i-1]乘上a[i+1, MN-1]。  
一次前後綴分解就完成。  

時間複雜度O(MN)。  
空間複雜度O(MN)。  

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        M,N=len(grid),len(grid[0])
        MN=M*N
        ans=[[0]*N for _ in range(M)]
        
        suff=[1]*(MN+1)
        for i in reversed(range(MN)):
            suff[i]=suff[i+1]*grid[i//N][i%N]%MOD
            
        pref=1
        for i in range(MN):
            r,c=i//N,i%N
            ans[r][c]=suff[i+1]*pref
            ans[r][c]%=MOD
            pref*=grid[r][c]
            pref%=MOD
        
        return ans
```

其實還是可以用乘法逆元來做，只是有點麻煩。  

剛才提過，求逆元時，base和質數p必須互質。  
而12345質因數分解後得到[3, 5, 823]三個數，只要我們確保三者不為base的質因數，那麼base和12345必定互質。  
  
先遍歷一次grid，把所有元素中的3, 5, 823分別拆出來記做cnt，其他因數可以直接乘在一起，記做prod。  
第二次遍歷grid，同樣拆出3, 5, 823，剩下的部分求逆元後乘上prod，在把剩餘的3, 5, 823乘上去即可。  

時間複雜度O(MN log MX)，其中MX為max(grid[i][j])。  
空間複雜度O(1)，輸出空間不計入。  

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        M,N=len(grid),len(grid[0])
        ans=[[0]*N for _ in range(M)]
        
        cnt3=cnt5=cnt823=0
        prod=1
        for r in range(M):
            for c in range(N):
                x=grid[r][c]
                while x%3==0:
                    x//=3
                    cnt3+=1
                while x%5==0:
                    x//=5
                    cnt5+=1
                while x%823==0:
                    x//=823
                    cnt823+=1
                prod*=x
                prod%=MOD
                
        for r in range(M):
            for c in range(N):
                curr3,curr5,curr823=cnt3,cnt5,cnt823
                x=grid[r][c]
                while x%3==0:
                    x//=3
                    curr3-=1
                while x%5==0:
                    x//=5
                    curr5-=1
                while x%823==0:
                    x//=823
                    curr823-=1
                x=prod*pow(x,-1,MOD) 
                x*=pow(3,curr3,MOD)
                x*=pow(5,curr5,MOD)
                x*=pow(823,curr823,MOD)
                ans[r][c]=x%MOD
                
        return ans
```
