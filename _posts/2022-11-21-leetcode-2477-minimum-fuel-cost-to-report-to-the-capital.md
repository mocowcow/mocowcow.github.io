--- 
layout      : single
title       : LeetCode 2477. Minimum Fuel Cost to Report to the Capital
tags        : LeetCode Medium Array Graph Tree DFS Greedy HashTable
---
周賽320。最近出現很多次這種無向無環樹，把不需要visited紀錄的寫法學起來真是太好了。  

# 題目
輸入一棵N個節點的樹(無向、無環、連通)，每個節點代表一個城市，編號分別為0\~N-1，且正好有N-1條邊。  
節點0是首都。輸入二維整數陣列roads，其中roads[i] = [a<sub>i</sub>, b<sub>i</sub>]，表示城市a<sub>i</sub>和b<sub>i</sub>之間有一條雙向的道路。  

每座城市都有一個代表要前往首都開會，且每座城市都有一台車。輸入整數seats，代表每台車最多承載seats人。  

每個代表都可以選擇要自駕或是搭便車，車輛每移動一個城市需要消耗一單位汽油。  

求每個代表抵達首**都最少需要多少汽油**。  

# 解法
以現實角度來思考，如果要省油錢，當然是等到所有人集結到某地再決定要開幾台車。  
定義dfs(i,fa)為城市i所集結的人數，fa代表要前往的下一個城市(也就是父節點)。算出城市的總人數之後，除以車子乘客數向上取整，就可以算出需要幾台車，每台車耗油1單位，加入答案之中。  

注意，城市0是首都，所以計算車輛耗油的時候不需要計入。  

dfs遍歷一次樹，計算各城市耗油的時後也遍歷一次，時空間複雜度O(N)。  

```python
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        N=len(roads)+1
        ans=0
        ppl=[0]*N
        g=defaultdict(list)
        for a,b in roads:
            g[a].append(b)
            g[b].append(a)
            
        def dfs(i,fa):
            cnt=1
            for j in g[i]:
                if j!=fa:cnt+=dfs(j,i)
            ppl[i]=cnt
            return cnt
        
        dfs(0,-1)
        
        ans=0
        for i in range(1,N):
            car=(ppl[i]+seats-1)//seats
            ans+=car
        
        return ans
```
