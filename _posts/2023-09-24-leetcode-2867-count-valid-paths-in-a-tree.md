---
layout      : single
title       : LeetCode 2867. Count Valid Paths in a Tree
tags        : LeetCode Hard Array Tree Graph UnionFind HashTable Math
---
周賽364。思維比較不明顯，想通就很好做。  

## 題目

有個n節點的無向樹，編號由1到n。  
輸入整數n和長度為n-1的二維整數陣列edges，其中edges[i] = [u<sub>i</sub>, v<sub>i</sub>]，代表u<sub>i</sub>和v<sub>i</sub>之間存在一條邊。  

求有多少**有效的**路徑。  

如果一個路徑(a, b)之中只出現**正好一個**質數節點，則稱為**有效的**。  

## 解法

話不多說，先預處理，篩出所有質數。  

一條路徑中正好一個質數點，只有兩種情況：  

1. 質數在路徑起/終點上 [p...]  
2. 質數在路徑中間 [..p..]  

我們只要枚舉所有質數p，從p開始向外擴散出去，能找到的非質數點都可以和p組成路徑。  
如果p的鄰接點j可以生成cnt個非質數節點的子樹，則p可以作為**路徑起點**，組成cnt條**情況一**的路徑。  
然後，p還可以再以這cnt個節點，搭配先前出現過的ps個節點，組成**情況二**的路徑。根據乘法原理，共有cnt+ps條。  
算完j對p的路徑組合之後，記得把cnt加入ps中。  

那麼要怎樣找p有多少相鄰的非質數節點？又是好朋友**並查集**。  
把相鄰的非質數節點連接成一塊，統計一下該連通塊有多少節點即可。  

預處理質數時間為O(MX log log MX)，其中MX為10^5。  
預處理不計算，時間複雜度剩下並查集的O(n log n)。  
空間複雜度O(n)。  

```python
MX=10**5
def get_prime(n):
    sieve = [True]*(n+1)
    prime = []
    for i in range(2, n+1):
        if sieve[i]:
            prime.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return set(prime)

prime=get_prime(MX)

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        fa=list(range(n+1))
        
        def find(x):
            if fa[x]!=x:
                fa[x]=find(fa[x])
            return fa[x]
        def union(a,b):
            f1=find(a)
            f2=find(b)
            if f1!=f2:
                fa[f1]=f2
                
        g=[[] for _ in range(n+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            if a not in prime and b not in prime:
                union(a,b)
                
        d=Counter()
        for i in range(1,n+1):
            d[find(i)]+=1
            
        ans=0
        for i in range(1,n+1):
            if i not in prime:
                continue
            ps=0
            for j in g[i]:
                if j in prime:
                    continue
                cnt=d[find(j)]
                ans+=cnt
                ans+=ps*cnt
                ps+=cnt
                
        return ans
```
