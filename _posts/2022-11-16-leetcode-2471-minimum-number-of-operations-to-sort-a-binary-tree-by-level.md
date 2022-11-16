--- 
layout      : single
title       : LeetCode 2471. Minimum Number of Operations to Sort a Binary Tree by Level
tags        : LeetCode Medium Array HashTable Tree BinaryTree DFS Sorting
---
周賽319。好多人都說這是經典題，但我還真沒印象之前有碰過這種類型的東西。  

# 題目
輸入二元樹根節點root，樹中每個節點的值都是**唯一的**。  

再一次操作中，你可以選擇**同一層**中任意兩個節點，將兩個節點值互換。  
求最少需要幾次操作才可以使得每一層的節點值按照遞增排序。  

# 解法
看到同一層，話不多說先將所有節點依照層數分類，之後再分層計算操作次數。  
對於每層的節點，先另外準備一份排好序的結果a，用雜湊表mp紀錄下個數值的期望索引。之後遍歷原始順序v，若當前數值v[i]不等於期望數值a[i]，則將兩者交換，操作次數+1，並更新mp指到交換後的新索引位置。  

依照二元樹的特性，一層最多節點數量應不會超過N/2，所以間複雜度瓶頸應該是排序的O(N log N)，排序以及遍歷的成本O(N)可以忽略。保存各層數節點，加上mp映射索引，空間複雜度O(N)。  

```python
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        nodes=defaultdict(list)
        
        def dfs(node,d):
            if not node:return
            nodes[d].append(node.val)
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,0)
        
        def f(v):
            cnt=0
            mp={x:i for i,x in enumerate(v)}
            a=sorted(v)
            for i,n in enumerate(a):
                if v[i]!=n:
                    cnt+=1
                    old=v[i]
                    j=mp[n]
                    v[i],v[j]=v[j],v[i]
                    mp[old]=j
            return cnt
                
        ans=0
        for v in nodes.values():
            ans+=f(v)
            
        return ans
```
