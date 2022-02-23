---
layout      : single
title       : LeetCode 133. Clone Graph
tags 		: LeetCode Medium HashTable Graph DFS BFS
---
每日題。很久以前做過，但今天才發現討論版有人吵說題目描述很爛，看來是以前的測資爛得糟糕，但現在版本沒有問題。  

# 題目
輸入一個無向圖的其中一個節點，將其deep copy一份後回傳。

# 解法
測資包含空節點，首先過濾這個情況。  
採用DFS複製圖。雜湊表nodes用以存所有新建立的節點，撰寫一個dfs(node)函數，node表示要被拷貝的舊節點。建立一個與node相同的複製品，並加入nodes中，並對node檢查所有鄰接節點adj，若adj無法在nodes中取得映射，代表該點尚未完成複製，先對adj執行複製。  
題目有提到所有節點皆從1開始命名，最後只要回傳1號新節點即可。

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodes = {}

        def dfs(node):
            nodes[node.val] = newNode = Node(node.val)
            for adj in node.neighbors:
                if adj.val not in nodes:
                    dfs(adj)
                newNode.neighbors.append(nodes[adj.val])

        dfs(node)

        return nodes[1]

```

看看以前寫的版本，或許這也是一種DFS吧。  

```python
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        head = node
        stack = [head]
        nodes = {1: Node(val=1)}

        while stack:
            node = stack.pop()
            newNode = nodes[node.val]
            for nbr in node.neighbors:
                if nbr.val not in nodes:
                    t = Node(nbr.val)
                    nodes[nbr.val] = t
                    stack.append(nbr)
                newNode.neighbors.append(nodes[nbr.val])

        return nodes[head.val]

```