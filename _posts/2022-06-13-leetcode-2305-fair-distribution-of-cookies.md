--- 
layout      : single
title       : LeetCode 2305. Fair Distribution of Cookies
tags        : LeetCode Medium Array Backtracking DP BitManipulation Bitmask
---
周賽297。又是python被霸凌的一天，沒剪枝吃了一個TLE，但是c++和java沒剪枝都沒事。  

# 題目
輸入整數陣列cookies，其中cookies[i]表示第i個袋子中的餅乾數。另外還有整數k，代表k個小孩要分餅乾。  
同一袋的餅乾都必須給同一個小孩，不能分開。  

分配的**不公平性**定義為所有小孩中拿到最多的餅乾數量。  
求所有分配方式中的**最小**不公平性。  

# 解法
剛看完題目沒什麼特別的想法，再看看測資範圍，小孩k最多8個，那就很確定可以用回溯法來做。  

撰寫一個輔助函數bt(i)用來做回溯，i代表著當前要分配的餅乾袋。  
我們要分給k個小孩，所以要開長度為k的陣列child，代表每個小孩手上持有的餅乾數。  
試著把每個餅乾都分給不同的小孩，在餅乾袋全部分完之後，以當前公平性更新答案。  

注意：python由於時間限制比較嚴格，必須要多加一個判斷，若某個小孩拿到第i袋餅乾不可能使最佳答案變小，則不進行遞迴。  
2022-6-16更新：看到有人有更厲害的剪枝，在所有小孩都沒餅乾的時候，給誰都一樣，所以只給第一個。  

```python
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        N=len(cookies)
        child=[0]*k
        ans=inf
        
        def bt(i):
            nonlocal ans
            if i==N:
                ans=min(ans,max(child))
                return 
            for j in range(k):
                if cookies[i]+child[j]<=ans: # 有可能使答案更小
                    child[j]+=cookies[i]
                    bt(i+1)
                    child[j]-=cookies[i] 
                if child[j]==0: # 只給第一個
                    break
        
        bt(0)
        
        return ans
```

java版本，即使不做剪枝判斷也可以過，這就滿玄學的。

```java
class Solution {
    int ans=Integer.MAX_VALUE;
    
    public int distributeCookies(int[] cookies, int k) {
        int[] child=new int[k];
        bt(0,cookies,k,child);
        return ans;
    }
    
    void bt(int i, int[] cookies, int k, int[] child){
        if(i==cookies.length){
            int mx=0;
            for(int n:child){
                mx=Math.max(mx,n);
            }
            ans=Math.min(ans,mx);
            return;
        }
        for(int j=0;j<k;j++){
            child[j]+=cookies[i];
            bt(i+1,cookies,k,child);
            child[j]-=cookies[i];
        }
    }
}
```

2023-07-01更新：原來這題也可以狀態壓縮dp來做，但是複雜度還真不好算。  

我們可以把每個小孩都當成一個子集合，總共有k個子集，加起來要把每個餅乾正好都選一次。  
而N個餅乾共有2^N-1種非空子集，以1 bit代表餅乾可用。  

定義dp(i,mask)：分配給i個小孩，且餅乾剩餘狀態為mask時，所能得到的最小**不公平性**。  
轉移方程式：dp(i,mask) = min( max( dp(i-1,mask^submask),cost[submask] ) FOR ALL submask of mask )  
base cases：當i<0且mask=0，代表全部小孩正好分完餅乾，不需要繼續分，回傳；否則只有i<0或是mask=0時，分別代表有餅乾沒分完，或是有小孩沒拿到，為不合法狀態，回傳inf避免計算。  

有k個小孩，每個小孩可能有2^N種mask，共k \* 2^N種狀態。  
mask不知道可以轉移個submask，據說是3^N種，時間複雜度O(k \* 3^N)。  
空間複雜度O(k \* 2^N)。  

```python
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        N=len(cookies)
        start=(1<<N)-1
        cost=[0]*(1<<N)
        
        for mask in range(1,1<<N):
            for i in range(N):
                if mask&(1<<i):
                    cost[mask]+=cookies[i]
        
        @cache
        def dp(i,mask):
            if i<0 and mask==0:
                return 0
            if i<0 or mask==0:
                return inf
            ans=inf
            sub=mask
            while sub>0:
                new_mask=mask^sub
                ans=min(ans,max(cost[sub],dp(i-1,new_mask)))
                sub=(sub-1)&mask
            return ans
        
        return dp(k-1,start)
```
