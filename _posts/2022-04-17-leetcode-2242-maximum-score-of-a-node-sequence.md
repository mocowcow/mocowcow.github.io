---
layout      : single
title       : LeetCode 2242. Maximum Score of a Node Sequence
tags 		: LeetCode Hard Graph Sorting
---
雙周賽76。還以為是併查集，搞了半天TLE，比賽結束才知原來是腦筋急轉彎。

# 題目
輸入一個無向圖，共有n個節點，編號從0~n-1。  
陣列scores代表各節點的分數。二維陣列edges代表[a,b]兩節點間的連線。  

一個有效的**節點序列**須符合：  
- 序列中相鄰的節點必須要有邊存在  
- 沒有重複出現的節點  

序列的分數總合為序列中所有節點的分數加總。求有效且長度為4的節點序列中最大分數總合為多少。

> scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]  
> [0,1,2,3], [3,1,2,0], [1,0,2,3]皆有效  
> [0,3,2,4]無效，因為0和3之間沒有邊存在
> 答案為[0,1,2,3]的分數總合5+2+9+8=24

# 解法
這個合法節點序列講這麼複雜，簡單講就是可以連成一條直線的四個節點。  

根據[大神的開導](https://leetcode.com/problems/maximum-score-of-a-node-sequence/discuss/1953669/Python3-Explanation-with-pictures-top-3-neighbors./1353347)，看到測資N<10^5就知道普通DFS不可能通過，必須要靠想像力(創意?)來分析問題核心。  
為什麼特別要求**長度4的序列**，其中隱藏的提示是什麼？每個edge兩邊各加上一個節點，剛好可以串成4個！  

既然題目要求分數最大化，那麼每個邊[a,b]要加上盡可能大的節點c,d，才能符合需求。我們可以試著只保劉每個點的2個最大的相鄰節點，簡化枚舉的次數。  
但是碰到這種情況會出錯：  
> a的最大鄰居[b,x1] b的最大鄰居[a,x1]  
> a,b互為最大 所以湊不出第四個點  

需要改成保留3個最大相鄰節點才能正確計算：  
> a的最大鄰居[b,x1,x2] b的最大鄰居[a,x1,x3]  
> [a,b]+a的鄰居[x1]+b的鄰居[x1] 節點重複無效  
> [a,b]+a的鄰居[x1]+b的鄰居[x3] 得到[a,b,x1,x3] 更新最大值
> [a,b]+a的鄰居[x2]+b的鄰居[x1] 得到[a,b,x2,x1] 更新最大值
> [a,b]+a的鄰居[x2]+b的鄰居[x3] 得到[a,b,x2,x3] 更新最大值

遍歷所有邊a,b，枚舉a和b的所有鄰居c,d，就可以得到所有可能的長度4節點序列。  
把a,b,c,d塞入set去重複就可以輕鬆檢查是否合法，若合法則以四個點的分數加總更新答案。  

節點長度為N，邊數量為E，時間複雜度應該是：  
遍歷所有eddes及兩方最多各3個鄰居=O(E\*3\*3)=O(E)

```python
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for a,b in edges:
            g[a].append((scores[b],b))
            g[b].append((scores[a],a))
            
        # just keep 3 largest neighbors
        for k in g.keys():
            g[k].sort(key=lambda x:-x[0])
            while len(g[k])>3:
                g[k].pop()
                
        # enumerate all 4 nodes sequence
        ans=-1
        for a,b in edges:
            for c_score,c in g[a]:
                for d_score,d in g[b]:
                    if len(set([a,b,c,d]))==4:# no duplicated 
                        ans=max(ans,scores[a]+scores[b]+c_score+d_score)
                        
        return ans
```

