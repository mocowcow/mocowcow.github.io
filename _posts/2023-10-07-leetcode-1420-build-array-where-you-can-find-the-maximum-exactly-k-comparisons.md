---
layout      : single
title       : LeetCode 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
tags        : LeetCode Hard Array DP PrefixSum
---
每日題。可以優化超級多次dp練習題。單純通過不難，難的是找出最佳解。  

## 題目

輸入三個整數n, m和k。  
下列演算法用來來找出正整數陣列的最大元素：  

![img](https://assets.leetcode.com/uploads/2020/04/02/e.png)  

你必須構造出滿足以下條件的出陣列arr：  

- arr擁有n個整數  
- 1 <= arr[i] <= m 其中 (0 <= i < n)  
- 使用上述的演算法後，search_cost會等於k  

求有多少種構造出arr的方案。答案很大，先模10^9+7後回傳。  

## 解法

search_cost以下簡稱**成本**。  
題目給定的演算法，就是遍歷陣列找到最大值。最大值初始為-1，成本就是最大值更新的次數。  

構造出長度為n的陣列，只能由1\~m的元素組成，而成本必須是k。  
先前最大值會影響成本的變化。  
目前知道有三個變數：陣列長度、先前最大值、成本。  

定義dp(i,j,k)：長度為i的陣列，先前最大值為j，且成本為k的陣列的**構造方案數**。  

我們可以任選1\~m的任意元素，則會縮減問題的規模，形成較小的子問題dp(i-1,j',k')。  
而新的最大值j'取max(j,x)。所有小於等於j的元素x都不會使成本增加，因此子問題為dp(i-1,j,k)；  
大於j的元素x則會改變最大值，且成本增加1，因此子問題為dp(i-1,x,k-1)。  
對於dp(i,j,k)來說，共有1\~j共j個元素小於等於j，其他都大於j。  
轉移方程式：dp(i,j,k) = dp(i-1,j,k)\*j + sum( dp(i-1,x,k-1) FOR ALL j<x<=m )  
base cases：剩餘長度i=0，且需求成本k=0時，順利達成要求，答案為1；若長度或成本不足0，代表不合法的狀態，答案為0。  

狀態有三個參數，共有nmk種狀態。每個狀態轉移需要O(m)時間。  

時間複雜度O(n \* m^2 \* k)。  
空間複雜度O(n \* m \* k)。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(i,j,k):
            if i==0 and k==0:
                return 1
            if i<0 or k<0:
                return 0
            res=dp(i-1,j,k)*j
            for x in range(j+1,m+1):
                res+=dp(i-1,x,k-1)
            return res%MOD
    
        return dp(n,0,k)
```

我們發現i和k這兩個變數會出現負數，為了方便改寫成遞推版本，將狀態上的i和k都增加位移量1，使所有狀態都不為負。  
當然，入口函數也要一起增加。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(i,j,k):
            if i==1 and k==1:
                return 1
            if i<1 or k<1:
                return 0
            res=dp(i-1,j,k)*j
            for x in range(j+1,m+1):
                res+=dp(i-1,x,k-1)
            return res%MOD
    
        return dp(n+1,0,k+1)
```

迴圈使用到的k會和輸入的k相同，原本的k記作k0，避免數值被汙染。  

初始化狀態將三個狀態參數轉換成迴圈、然後return改成continue，剩餘照搬就可以。  
dp(i,j,k)是從dp(i-1,j',k')轉移過來，因此只需要確保i是最外層迴圈，從小到大枚舉，剩餘兩者隨意。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        k0=k
        dp=[[[0]*(k+2) for _ in range(m+1)] for _ in range(n+2)]
        
        for i in range(n+2):
            for j in range(m+1):
                for k in range(k0+2):
                    if i==1 and k==1:
                        dp[i][j][k]=1
                        continue
                    if i<1 or k<1:
                        continue
                    res=dp[i-1][j][k]*j
                    for x in range(j+1,m+1):
                        res+=dp[i-1][x][k-1]
                    dp[i][j][k]=res%MOD
                    
        return dp[n+1][0][k0+1]
```

又發現當i或j等於0時，方案數一定是0，根本不用處理。  
因此i和j可從1開始枚舉。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        k0=k
        dp=[[[0]*(k+2) for _ in range(m+1)] for _ in range(n+2)]
        
        for i in range(1,n+2):
            for j in range(m+1):
                for k in range(1,k0+2):
                    if i==1 and k==1:
                        dp[i][j][k]=1
                        continue
                    res=dp[i-1][j][k]*j
                    for x in range(j+1,m+1):
                        res+=dp[i-1][x][k-1]
                    dp[i][j][k]=res%MOD
                    
        return dp[n+1][0][k0+1]
```

仔細觀察，又又發現當i和k不變的情況下，只要j越大，轉移的次數會越小。  
對dp(i,j,k)來說，x轉移的範圍是j<x<=m；  
對dp(i,j-1,k)來說，x轉移的範圍是j-1<x<=m，比起上者，只多出一個來源dp(i-1,j,k)。  
也就是說這部分有非常多的重複計算。  

這些重複計算怎麼處理？  
如同先讓你找1\~1的總和，再找1\~2的總和，再找1\~3的總和同理，重複利用先前的值：正是**前綴和**。  
維護一個變數ps，作為先前x來源的前綴和，直接加入ps就可以，不需要枚舉所有m個元素。  
計算完dp(i,j,k)後，記得dp(i-1,j,k-1)加入前綴和中，為之後的j作貢獻。  

注意：因為上述更動，dp(i,j-1,k)依賴於dp(i,j,k)的轉移前綴和，因此j必須**從大到小**枚舉。  
並且k都是維持同樣的值，所以必須把k的迴圈搬到j的外層。  

時間複雜度O(n \* m \* k)。  
空間複雜度O(n \* m \* k)。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        k0=k
        dp=[[[0]*(k+2) for _ in range(m+1)] for _ in range(n+2)]
        
        for i in range(1,n+2):
            for k in range(1,k0+2):
                ps=0
                for j in reversed(range(m+1)):
                    if i==1 and k==1:
                        dp[i][j][k]=1
                        continue
                    res=dp[i-1][j][k]*j+ps
                    dp[i][j][k]=res%MOD
                    ps+=dp[i-1][j][k-1]
                    
        return dp[n+1][0][k0+1]
```

這樣就結束了嗎？並沒有。  

dp(i,j,k)只依賴於i-1的結果，別忘了遞推空間優化的老朋友：**滾動陣列**。  
計算長度為i的方案時，只需要保留前一次i-1的結果，壓縮掉n這個維度的空間。  

時間複雜度O(n \* m \* k)。  
空間複雜度O(m \* k)。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        k0=k
        dp=[[0]*(k+2) for _ in range(m+1)]
        
        for i in range(1,n+2):
            dp2=[[0]*(k+2) for _ in range(m+1)]
            for k in range(1,k0+2):
                ps=0
                for j in reversed(range(m+1)):
                    if i==1 and k==1:
                        dp2[j][k]=1
                        continue
                    res=dp[j][k]*j+ps
                    dp2[j][k]=res%MOD
                    ps+=dp[j][k-1]
            dp=dp2
                    
        return dp[0][k0+1]
```

最後再看看k的變化，對於dp(i,j,k)只會依賴於dp(i-1,j,k)和dp(i-1,j,k-1)。  
其實連滾動的dp2陣列都不需要，只要把k逆向枚舉，就不會覆蓋到需要的值。  

```python
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7
        k0=k
        dp=[[0]*(k+2) for _ in range(m+1)]
        
        for i in range(1,n+2):
            for k in reversed(range(1,k0+2)):
                ps=0
                for j in reversed(range(m+1)):
                    if i==1 and k==1:
                        dp[j][k]=1
                        continue
                    res=dp[j][k]*j+ps
                    dp[j][k]=res%MOD
                    ps+=dp[j][k-1]
                    
        return dp[0][k0+1]
```

搞這麼多次，總算大功告成。  
