---
layout      : single
title       : LeetCode 2973. Find Number of Coins to Place in Tree Nodes
tags        : LeetCode Hard Array Tree Graph DFS Greedy Sorting
---
雙周賽120。

## 題目

有棵n節點的無向樹，節點編號從0到n-1，且根節點為0。  
輸入長度n-1的二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間存在一條邊。  

另外輸入長度n的整數陣列cost，其中cost[i]是在第i個節點上放置硬幣的**成本**。  

你必須所有節點上都放置硬幣。在節點i放置的硬幣數量規則是：  

- 若節點i的子樹大小小於3，就放1個硬幣  
- 否則，在子樹中找到任意3個不同節點的**最大乘積**。放置等同數量的硬幣。若乘積是**負數**則放0個  

回傳長度為n的陣列coin，其中coin[i]代表節點i所放置的硬幣數。  

## 解法

很直覺的可以想到用dfs來做樹狀問題，由下而上，處理完所有子節點，才知道父節點子樹中的所有節點成本。  
難點在於，當樹是鍊狀的時候，節點數不斷增加，要怎麼有效率的處理節點成本？  

由於只要選擇三個成本相乘，有兩種選法能得到最大值：  

- 3正數  
- 1正數2負數  

因此我們只需要保留最大的3個數，以及最小的2個數。  
那如果成本不足5個，且無法滿足以上選法會怎樣？  

- 2正1負，乘積一定負，放0個硬幣  
- 3負，乘積一定負，放0個硬幣  

除此之外一定可以滿足其中一種選法，因此是可行的。  

保留3+2的方法也很簡單：直接排序，取前3大、後2小的元素組成長度5的陣列即可。  
在鍊狀樹的情況下，大概需要把5個成本排序N次；在樹的深度只有2的情況，會將N-1個成本排序一次。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        N=len(edges)+1
        ans=[None]*N
        g=[[] for _ in range(N)]
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        def dfs(i,fa):
            # build subtree costs
            vals=[cost[i]]
            for j in g[i]:
                if j==fa:
                    continue
                for x in dfs(j,i):
                    vals.append(x)
            
            # less than 3 
            if len(vals)<3:
                ans[i]=1
                return vals
            
            # pruning
            vals.sort(reverse=True)
            if len(vals)>5: # 3 big, 2 small
                vals=vals[:3]+vals[-2:]
            
            ans[i]=max(
                0,
                vals[0]*vals[1]*vals[2], # 3 big
                vals[0]*vals[-1]*vals[-2] # 1 big 2 small
            )
            return vals
        
        dfs(0,-1)
        
        return ans
```
