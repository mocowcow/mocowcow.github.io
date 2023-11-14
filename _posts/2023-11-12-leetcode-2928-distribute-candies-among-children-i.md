---
layout      : single
title       : LeetCode 2928. Distribute Candies Among Children I
tags        : LeetCode Easy Simulation Math DP PrefixSum
---
雙周賽117。最近周賽真的是越來越扯，前兩題分別是分糖果1和2。但是在開賽的前幾日，分糖果3竟然以**付費題**的形式出現。  
而且內容完全一樣，只是測資範圍變大，直接向下兼容本次兩題。真的是pay to win。  

## 題目

輸入兩個正整數n和limit。  

把n個糖果分給3個小孩，且每個小孩最多拿limit個糖果。求有多少分法。  

## 解法

首先是暴力法，枚舉三個小孩的糖果數，剛好對上總數n就合法。  

時間複雜度O(min(n,limit)^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=0
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if i+j+k==n:
                        ans+=1
                        
        return ans
```

如果只枚舉第一個小孩i，剩下j+k兩個小孩的糖果數會是n-i=jk。  
分類討論三種情況：  

1. jk不超過limit。則j小孩可以隨便拿，然後k撿剩的  
2. jk超過limit，不超過兩倍limit，當j在某個區間時，正好可以分完  
3. jk超過兩倍limit。兩人無法分完  

情況1，j可以隨便拿[0, jk]個，剩下給k一定合法。  
情況3不處理。  
至於情況2，我們要找出j在哪個區間才會合法。  

j最多肯定可以拿到limit個，故上界是limit。  
如果j拿越少，則k拿的會越多。當j少到一個臨界值min(j)，會使得k超過limit。  
必須滿足jk-j <= limit。  

> 以min(j)帶入j  
> jk-min(j) <= limit  
> 移項  
> jk-limit <= min(j)  

得到min(j) = jk-limit，這就是下界。  
所以j的範圍是[min(j), limit]。  

時間複雜度O(min(n,limit))。  
空間複雜度O(1)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        limit=min(limit,n)
        ans=0
        for i in range(limit+1):
            jk=n-i
            if jk<=limit:
                ans+=jk+1
            elif jk<=limit*2:
                hi=limit
                lo=jk-limit
                ans+=hi-lo+1
                
        return ans
```

其實也可以用dp來解，但不是最好的辦法。  
有點類似於上面的方法，就是枚舉第一人拿多少，剩下的再給第二人拿多少，最後全部留給第三人。  

定義dp(ppl,candy)：將candy分給ppl個人，且每個人最多只能拿limit時，共有幾種分法。  
轉移方程式：dp(ppl,candy) = sum(dp(ppl-1, candy-take)) FOR ALL 0<=take<=min(candy,limit)  
base case：當ppl=0且candy=0，代表剛好分完，回傳1；沒分完就不合法，回傳0。  

時間複雜度O(n\*min(n,limit))。  
空間複雜度O(n)。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        @cache
        def dp(ppl,candy):
            if ppl==0:
                return int(candy==0)
            res=0
            for take in range(min(limit,candy)+1):
                res+=dp(ppl-1,candy-take)
            return res
        
        return dp(3,n)
```

但這種樸素的dp時間複雜度大約是O(n^2)，沒有辦法通過10^6的測資。  
看看有沒有可以優化的地方。先改成遞推。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        dp=[[0]*(n+1) for _ in range(4)]
        dp[0][0]=1
        for ppl in range(1,4):
            for candy in range(n+1):
                res=0
                for take in range(min(limit,candy)+1):
                    res+=dp[ppl-1][candy-take]
                dp[ppl][candy]=res
            
        return dp[3][n]
```

可以發現，對於dp[ppl][candy]和dp[ppl][candy-1]來說，他們的選擇幾乎是相同的。  
例如：  
> dp[i][0] = dp[i-1][0]  
> dp[i][1] = dp[i-1][0] + dp[i-1][1]  
> dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]  

研究後看出dp[ppl][candy]會比dp[ppl][candy-1]多出一個dp[ppl-1][candy]，也就是**完全不拿**的選法。  
這部分可以用前綴和來維護。  

但是candy超過limit時，就不能全拿了，會少掉一些選法：  
> limit = 2  
> dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]  
> dp[i][3] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]  

candy=3時，比起前一個式子，依然多出一個**完全不拿**的選法，就是dp[i-1][3]。  
但是最多只能拿2個，所以要把拿三個的選法排除掉，也就是少了dp[i-1][0]。  
當candy超過limit時，每一次增長，都會多dp[ppl-1][cadny]，少一個dp[ppl-1][candy-(limit+1)]。  

轉移方程式：  

- 當candy <= limit，則dp[ppl][candy] = ps+dp[ppl-1][candy]  
- 當candy > limit，則dp[ppl][candy] = ps+dp[ppl-1][candy]-dp[ppl-1][candy-(limit+1)]  

時間複雜度O(n)。  
空間複雜度O(n)。  

```python
        dp=[[0]*(n+1) for _ in range(4)]
        dp[0][0]=1
        for ppl in range(1,4):
            ps=0
            for candy in range(n+1):
                ps+=dp[ppl-1][candy]
                if candy>limit:
                    ps-=dp[ppl-1][candy-(limit+1)]
                dp[ppl][candy]=ps

        return dp[3][n]
```

dp[ppl]只會參考到dp[ppl-1]的狀態，可以用滾動陣列優化，只需要一維陣列。  
雖然空間複雜度一樣不變就是，但至少快了一些。  

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for ppl in range(1,4):
            dp2=[0]*(n+1)
            ps=0
            for candy in range(n+1):
                ps+=dp[candy]
                if candy>limit:
                    ps-=dp[candy-(limit+1)]
                dp2[candy]=ps
            dp=dp2

        return dp[n]
```
