--- 
layout      : single
title       : LeetCode 399. Evaluate Division
tags        : LeetCode Medium Array Graph
---
每日題。果然還是不太適合併查集的併查集系列題，這次主角是floyd warshall。

# 題目
輸入長度為N的陣列equations和values，equations[i]由兩個代數組成[A,B]，代表A除B=values[i]。  
queries[i]也是由[C,D]代表要查詢C除D的值，若無法計算則回傳-1。  
查詢保證都是合法的，不會出現分母為0的情況。

# 解法
以前練習併查集的時候碰過這題，想半天沒半點頭緒，看了[大神解法](https://leetcode.com/problems/evaluate-division/discuss/88175/9-lines-%22Floydu2013Warshall%22-in-Python)，驚為天人，到現在還記得。  

把等式看作是有像圖的邊，如例題的A\*B=2，B\*C=3，可以當作A到C的路徑，也就是2\*3=6。  
例題還好心的告訴我們B\*A=0.5，是要提醒我們(A\*B)除(B\*)A永遠是1；而某個數除以自己也永遠是1。  

透過以上三點，可以把每個a\*b=v拆成三個部分來初始化graph：  
- a到a恆為1  
- a到b為v  
- b到a為1/v  

之後使用floyd warshall，遍歷每個代數k，以k為中間點，試著將所有能和k連通的代數連通。  
最後再遍歷一次equations，在graph裡找路徑(a,b)的值，若路經不存在則代表無法計算，回傳-1。  

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(dict)
        for (a,b),v in zip(equations,values):
            g[a][a]=1
            g[a][b]=v
            g[b][a]=1/v

        for k in g:
            for a in g[k]:
                for b in g[k]:
                    g[a][b]=g[a][k]*g[k][b]
                    
        ans=[]
        for a,b in queries:
            if a in g and b in g[a]:
                ans.append(g[a][b])
            else:
                ans.append(-1)
                
        return ans
```
