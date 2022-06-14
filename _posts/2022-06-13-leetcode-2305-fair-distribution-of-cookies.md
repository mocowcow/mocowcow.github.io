--- 
layout      : single
title       : LeetCode 2305. Fair Distribution of Cookies
tags        : LeetCode Medium Array Backtracking
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
                if cookies[i]+child[j]<=ans: # pruning
                    child[j]+=cookies[i]
                    bt(i+1)
                    child[j]-=cookies[i] 
        
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