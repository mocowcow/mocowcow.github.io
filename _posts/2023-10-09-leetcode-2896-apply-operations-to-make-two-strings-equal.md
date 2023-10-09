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

我們只要考慮s1[i]和s2[i]不相同的索引i，原本相同的話再去翻轉也沒意義。  

選擇索引i, j，操作後的變化只有四種情形：00變11、11變00、01變10、10變01。  
字串中1的的數量一定是偶數增減，若不同的索引有奇數個，則不存在答案。  

試想以下例子：  
> s1 = 100, s2 = 001  
> 如果使用第一種操作，直接反轉s1[0]和s1[2]，成本x  
> 也可以用第二種操作，先反轉s1[0]和s1[1]，s1 = 010  
> 然後再反轉s1[1]和s1[2]，s1 = 001，成本2  

發現想要同時翻轉i, j兩個索引，可以選擇成本較低的方法，也就是min(x, j-i)。  
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
