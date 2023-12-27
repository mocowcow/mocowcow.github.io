---
layout      : single
title       : LeetCode 2977. Minimum Cost to Convert String II
tags        : LeetCode Hard Array String Graph DP HashTable
---
周賽377。應該刷新個人最佳，名次66。  
這題太多瑕疵，可能我吃過太多次同口味的屎，很快就知道要怎麼吞下肚，因禍得福吧。  
而且兩段一樣的敘述，Q3用的是letters，但Q4改用characters，乍看內容不同，結果意思完全一樣，浪費時間。  

之前碰到好幾次O(N^2)的dp竟然噴MLE，還要清掉快取才能過，莫名其妙。  
這次更離譜，我清了快取還是MLE，只好把dp裡面的轉移做剪枝才AC。  
C++好像不是噴MLE而是TLE，一樣需要對轉移剪枝才行。  

看幾個常常榜一的選手都吃了7次BUG，可見這題是真的是很有問題。  

## 題目

輸入兩個長度n，只由小寫字母組成的字串source和target。  
另外還有兩個字元陣列original, changed和整數陣列cost。其中cost[i]代表將original[i]改成changed[i]的成本。  

最初你擁有字串source。  
每次操作，如果滿足original[j]=x, changed[j]=y, cost[j]=z，你可以從字串中的**任一**個**字串**x改成y，並支付成本z。  

你可以執行**任意次**操作，但必須滿足以下兩個條件：  

- 任意兩次操作所選擇的字串source[a..b]和source[c..d]，滿足b<c或d<a  
- 任意兩次操作所選擇的字串source[a..b]和source[c..d]，滿足b==c且d==a  

求將source變成target的**最小成本**；若不可能，則回傳-1。  

注意：可能存在兩個索引i, j，其中original[j] == original[i]且changed[j] == changed[i]。也就是兩種修改方向相同，但成本不一定相同。

## 解法

和前一題不同的點在於：  

- 原本修改**字元**，現在修改**字串**  
- 選擇修改的子字串位置必須完全相同，否則不可有交集  

簡單來說，就是在source中選擇任意不重疊的區間，修改**任意次**後變成target。若原本字元就相同也可以不修改。  
例如：  
> source = "abb", target = "acc"  
> 若存在"abb"改成"acc"的路徑，可以直接修改  
> 因為兩者共通前綴a，也可以不修改  
> 縮減成更小的子問題"bb"和"cc"  

再看看cost長度上限變成100，那麼修改前/後最多會有各100種不同的字串，圖中最多200個節點、100種字串長度。  
這樣要做floyd好像也還行。  

而source長度上限變成1000，代表O(N^2)的作法應該可以接受。  
我們要決定source中的某些子字串選擇**改或不改**，因此考慮dp。  

定義f(i)：將子字串source[i, n-1]修改成target[i, n-1]的最小成本。  
轉移：f(i) = min(改, 不改)。  
source[i]等於target[i]則可以不改，直接跳到f(i+1)。  
不改 = min(cost(i,j) + f(j+1))。其中cost(i,j)維修改子字串[i,j]的最小成本。  
base case：當i等於N，子字串修改完畢，成本0。  

dp轉移過程中會需要多次使用到重覆的子字串，因此可以先預處理所有子字串(或快取)。  
最後f(0)就是答案。  

最多只會有200種不同的節點(子字串)，也就是200種不同的長度。  
floyd大約是200^3 = 8\*10^6次運算。  

dp轉移的過程中，只枚舉合法子字串的長度，這樣每個狀態最多只需要轉移M=100次，而非原本的N=1000次。
共有N個狀態，每次轉移需要構造子字串，每次O(N)，每個狀態轉移M次。
dp的部分大約是1000^2 \* 100 = 10^8次運算。  

雖然10^8看起來很慢，但可能python字串切片太快了，確實是能夠AC。  

時間複雜度O(V^3 + N^2 \* M)。其中V=len(cost)\*2，M=len(cost)。  
空間複雜度O(V^2 + N^2)。  

其實在floyd部分的耗時佔了非常大的比例，因為不同長度之間的字串不可能相互修改，造成大量無效計算。  
試想有100個字串長度都不同，那floyd跑完跟沒跑一樣。  
如果以字串長度來分組計算會更加有效率。或是在枚舉[i,k,j]路徑時，發現ik不通就直接跳過。  
原本python大概需要跑13000ms，加上這行剪枝直接加速到1000ms左右。就連golang剪枝後也可以AC。  

```python
class FloydWarshallDict:
    def __init__(self, vertexes):
        self.dp = defaultdict(lambda: defaultdict(lambda: inf))
        for v in vertexes:
            self.dp[v][v] = 0

    def add(self, a, b, c):
        if c < self.dp[a][b]:
            self.dp[a][b] = c

    def get(self, a, b):
        return self.dp[a][b]

    def build(self):
        for k in self.dp:
            for i in self.dp:
                if self.dp[i][k] == inf:  # pruning
                    continue
                for j in self.dp:
                    new_dist = self.dp[i][k]+self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N=len(source)
        ss=set(original+changed)
        sizes=sorted(set(len(x) for x in ss))
        
        # O(V^3)
        fw=FloydWarshallDict(ss)
        for a,b,c in zip(original,changed,cost):
            fw.add(a,b,c)
        fw.build()
        
        # O(N^2 * M)   
        @cache
        def f(i): # O(N)
            if i==N:
                return 0
            res=inf
            if source[i]==target[i]: 
                res=f(i+1)
            for size in sizes: # O(M)
                j=i+size
                if j>N:
                    break
                s=source[i:j] # O(N)
                t=target[i:j]
                res=min(res,fw.get(s,t)+f(j))
            return res
        
        ans=f(0)
        f.cache_clear()
        
        if ans==inf:
            return -1
        
        return ans
```

回顧一下，最多有V=200個端點，還有E=100條邊(同時也是100種字串長度)。  

floyd是找出**任意兩節點之間**的最短路相較之下，dijkstra是計算**單點到所有節點**的最短路。  
剛才用floyd的複雜度是O(V^3)，大約8\*10^6次運算。  
而dijkstra跑一次是O(E log E)，對V=200個點各跑一次，大約10^5次運算，其實比floyd還快。  

時間複雜度O(VE log E + N^2 \* M)。其中V=len(cost)\*2，M=len(cost)。  
空間複雜度O(V^2 + N^2)。  

```python
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ss=set(original+changed)
        sizes=sorted(set(len(x) for x in ss))
        g=defaultdict(list)
        for a,b,c in zip(original,changed,cost):
            g[a].append([b,c])
        
        # heap optimized dijkstra
        # O(E log E)
        @cache
        def dijkstra(src):
            dis = defaultdict(lambda: inf)
            dis[src] = 0
            heap = [(0, src)]
            while heap:
                cost, curr = heappop(heap)
                if cost > dis[curr]:
                    continue
                dis[curr] = cost
                for adj, c in g[curr]:
                    new_cost = cost+c
                    if new_cost < dis[adj]:
                        dis[adj] = new_cost  # important pruning
                        heappush(heap, (new_cost, adj))
            return dis
        
        # O(N^2 * M)   
        N=len(source)
        @cache
        def f(i): # O(N)
            if i==N:
                return 0
            res=inf
            if source[i]==target[i]: 
                res=f(i+1)
            for size in sizes: # O(M)
                j=i+size
                if j>N:
                    break
                s=source[i:j] # O(N)
                t=target[i:j]
                res=min(res,dijkstra(s)[t]+f(j))
            return res
        
        ans=f(0)
        f.cache_clear()
        
        if ans==inf:
            return -1
        
        return ans
```
