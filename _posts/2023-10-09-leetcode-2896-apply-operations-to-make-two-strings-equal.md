---
layout      : single
title       : LeetCode 2896. Apply Operations to Make Two Strings Equal
tags        : LeetCode Medium Array DP
---
周賽366。完全沒想到是dp，而且竟然有三種dp作法，真的是好題。  

## 題目

輸入兩個二進位字串s1和s2，長度都是n，還有一個正整數x。  

你可以對s1執行以下操作**任意**次：  

- 選擇兩個索引i和j，並反轉s1[i]和s1[j]。操作成本為x  
- 選擇小於n-1的索引i，並反轉s1[i]和s1[i+1]。操作成本為1  

求使得s1和s2相等的**最小成本**，若不可能相等則回傳-1。  

注意：反轉指的是將0變成1，或是1變成0。  

## 解法

我們只要考慮s1[i]和s2[i]不相同的索引i，原本相同的話再去反轉也沒意義。  

選擇索引i, j，操作後的變化只有四種情形：00變11、11變00、01變10、10變01。  
字串中1的的數量一定是偶數增減，若不同的索引有奇數個，則不存在答案。  

試想以下例子：  
> s1 = 100, s2 = 001  
> 如果使用第一種操作，直接反轉s1[0]和s1[2]，成本x  
> 也可以用第二種操作，先反轉s1[0]和s1[1]，s1 = 010  
> 然後再反轉s1[1]和s1[2]，s1 = 001，成本2  

發現想要同時反轉i, j兩個索引，可以選擇成本較低的方法，也就是min(x, j-i)。  
那要怎樣配對才能保證成本最小？  

如果循序倆倆配對，那麼碰到s1 = 10011001, s2 = 00000000 這種情形就會算錯。  
試著往dp去考慮。  

定義dp(l,r)：需要反轉的索引陣列idx中，反轉子陣列idx[l, r]的最小成本。  
枚舉與idx[l]配對的索引idx[i]，並計算反轉idx[l+r, l]和idx[l+1, r]兩個子字串。  
轉移方程式：dp(l,r) = min( cost(idx[l],idx[i]) + dp(l+1, i-1) + dp(i+1, r) ) FOR ALL l<i<r  
base cases：若l>r代表反轉結束，回傳0；若r-i+1為奇數，則不可能有答案，回傳inf。  

狀態共有N^2個，每個狀態需要轉移N次。  
時間複雜度O(N^3)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[]
        for i,c in enumerate(s1):
            if c!=s2[i]:
                idx.append(i)
        
        @cache
        def dp(l,r):
            if (l-r+1)%2==1:
                return inf
            if l>r:
                return 0
            res=inf
            for i in range(l+1,r+1):
                cost=min(x,idx[i]-idx[l])
                res=min(res,cost+dp(l+1,i-1)+dp(i+1,r))
            return res
        
        ans=dp(0,len(idx)-1)
        
        if ans==inf:
            return -1
        
        return ans
```

按照最初說的，反轉的個數必須是偶數，乾脆在一開始就過濾。  
dp轉移時也只枚舉奇偶性不同的索引，省略一堆無效的計算。  

複雜度不變，但是常數小很多。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[i for i,c in enumerate(s1) if c!=s2[i]]
        
        if len(idx)%2==1:
            return -1
        
        @cache
        def dp(l,r):
            if l>r:
                return 0
            res=inf
            for i in range(l+1,r+1,2):
                cost=min(x,idx[i]-idx[l])
                res=min(res,cost+dp(l+1,i-1)+dp(i+1,r))
            return res
        
        return dp(0,len(idx)-1)
```

另種思路是把第一種操作**拆成兩半**。  

定義dp(i)：需要反轉的索引陣列idx中，反轉前i個索引的最小成本。  
可以選擇idx[i]要使用第一種操作，配對的idx[j]之後再找；或是idx[i]和idx[i-1]一起使用第二種操作。  
轉移方程式：dp(i) = min( dp(i-1) + x/2, dp(i-2) + idx[i]-idx[i-1] )  
base case：當i等於-1，代表反轉完成，回傳0。  

注意：只有在剩下至少兩個索引的時候才能使用第二種操作，而且先前也過濾掉奇數情況，保證索引一定會成對。  
然後x可能是奇數，所以dp結果必須是浮點數，最後才轉回整數。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[i for i,c in enumerate(s1) if c!=s2[i]]
        
        if len(idx)%2==1:
            return -1
        
        @cache
        def dp(i):
            if i<0:
                return 0
            res=dp(i-1)+x/2
            if i>0:
                res=min(res,dp(i-2)+idx[i]-idx[i-1])
            return res
        
        return int(dp(len(idx)-1))
```

如果怕浮點數誤差，可以把成本都先設成兩倍，最後回傳答案時一次除回來。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[i for i,c in enumerate(s1) if c!=s2[i]]
        
        if len(idx)%2==1:
            return -1
        
        @cache
        def dp(i):
            if i<0:
                return 0
            res=dp(i-1)+x
            if i>0:
                cost=idx[i]-idx[i-1]
                res=min(res,dp(i-2)+cost*2)
            return res
        
        return dp(len(idx)-1)//2
```

改寫成遞推版本。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[i for i,c in enumerate(s1) if c!=s2[i]]
        N=len(idx)
        
        if N%2==1:
            return -1

        dp=[0]*(N+1)
        for i in range(N):
            dp[i+1]=dp[i]+x
            if i>0:
                cost=idx[i]-idx[i-1]
                dp[i+1]=min(dp[i+1],dp[i-1]+cost*2)
                
        return dp[N]//2
```

dp[i]只會參考到dp[i-1]和dp[i-2]這前兩項的結果。  
可以使用滾動陣列，節省空間。  

注意：需要特判s1等於s2的情形。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        idx=[i for i,c in enumerate(s1) if c!=s2[i]]
        
        N=len(idx)
        if N%2==1:
            return -1
        
        if N==0: # s1==s2
            return 0
        
        pprev=0
        prev=x
        for i in range(1,N):
            cost=idx[i]-idx[i-1]
            t=prev
            prev=min(prev+x,pprev+cost*2)
            pprev=t
        
        return prev//2
```

其實還有一種O(N^2)的dp，但我覺得比起上面兩種更難想到。  
判定當前索引i是否被**反轉過**，更類似於dfs的暴力搜索。  

定義dp(i,free,rev)：剩下free次免費反轉機會，使前i個字元相等的最小反轉成本。rev代表s1[i]是否被反轉過。  

轉移方程式：  
如果s1[i]和s2[i]原本就相同、或經過反轉後相同，則不需多餘操作，直接考慮下一個字元  

- dp(i,free,rev) = dp(i-1,free,False)  

使用第一種操作，先計算費用，並記錄一次反轉的機會  

- dp(i,free,rev) = dp(i-1,free+1,False) + x  

如果當前有免費機會也可以使用  

- dp(i,free,rev) = dp(i-1,free-1,False) if free>0  

否則使用第二種操作，把s1[i]和s1[i-1]一起反轉  

- dp(i,free,rev) = dp(i-1,free,True) + 1  

base cases：當i小於0時，所有字元都處理完，這時free應為0、rev也為false，合法則回傳0；否則因操作1需要成對操作，剩餘奇數free代表沒有答案，非零0的偶數代表使用太多的操作次數，兩種都不會是答案，回傳inf。  

時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        N=len(s1)
        if s1.count("1")%2!=s2.count("1")%2:
            return -1
        
        @cache
        def dp(i,free,rev):
            if i<0 and free==0 and not rev:
                return 0
            if i<0:
                return inf
            if (s1[i]==s2[i]) == (not rev): # no need flip
                return dp(i-1,free,False)
            res=dp(i-1,free+1,False)+x # op1 
            res=min(res,dp(i-1,free,True)+1) # op2
            if free>0:
                res=min(res,dp(i-1,free-1,False))
            return res
        
        return dp(N-1,0,False)
```
