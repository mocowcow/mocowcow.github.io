---
layout      : single
title       : LeetCode 173. Binary Search Tree Iterator
tags 		: LeetCode Medium Design BinarySearchTree DFS Stack 
---
每日題。已經不知道是第幾天二元搜尋樹，這題和前幾天的[230. Kth Smallest Element in a BST]({% post_url 2022-04-18-leetcode-230-kth-smallest-element-in-a-bst.md %})有一點相關，這順序安排就有感受到管理團隊的用心。

# 題目
設計一個二元搜尋樹的疊代子，以中序遍歷的方式依序取得元素。

實作類別BSTIterator：  
1. 建構子，接收BST的根節點  
2. boolean hasNext()，若還有未使用的元素則回傳true，否則false  
3. int next()，回傳下一個元素  

# 解法
暴力法當然就是先遍歷整棵樹，把所有節點加入記憶體中。  
實作起來最簡單快速，取出元素時也不用什麼額外操作。

```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q=deque()
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.q.append(node.val)
            dfs(node.right)

        dfs(root)
            
    def next(self) -> int:
        return self.q.popleft()  

    def hasNext(self) -> bool:
        return self.q
```

follow up要求使用O(H)的空間，有點似曾相識，原來是前幾天用過的概念。  
我們需要一個stack來保存節點，還有一個函數goLeft(node)，從node不斷往左走，把路上所有碰到的節點加入stack。  
初使化直接將root交給goLeft處理。之後每次呼叫next時，從stack中取出頂端節點node，並將node的右子樹丟給goLeft，最後回傳node。  

```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        self.goLeft(root)
        
    def goLeft(self,node):
        while node:
            self.st.append(node)
            node=node.left

    def next(self) -> int:
        node=self.st.pop()
        self.goLeft(node.right)
        return node.val
        
    def hasNext(self) -> bool:
        return self.st
```