--- 
layout      : single
title       : LeetCode 117. Populating Next Right Pointers in Each Node II
tags        : LeetCode Medium LinkedList BinaryTree DFS BFS
---
每日題。原來已經是第三次寫這題，沒想到解題思維完全都一樣，只是語法上變得更加簡潔。

# 題目
輸入一棵二元樹，將每個節點的next指針指向其相同高度的右方節點。若沒有右節點，則設為null。  
最初所有的next指針初始值都為null。

# 解法
建立雜湊表nodes，用節點的高度來分組。  
撰寫帶有高度的dfs方法，從root開始往下遞迴，每次高度+1，將節點加入nodes中。為確保每層的節點有序出現，往子節點遞迴時，一定要先走左子樹。  
dfs結束後，所有的節點都已經有序的排列在nodes中。遍歷nodes中的所有高度，將該層每個節點i的next指針指向第i+1個節點，最後一個節點不處理。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes=defaultdict(list)
        
        def dfs(node,lvl):
            if not node:
                return 
            nodes[lvl].append(node)
            dfs(node.left,lvl+1)
            dfs(node.right,lvl+1)
        
        dfs(root,0)
        
        for lvl in nodes:
            a=nodes[lvl]
            for i in range(len(a)-1):
                a[i].next=a[i+1]  
        
        return root
```

看了討論區才恍然大悟，原來bfs更適合這題，因為可以在遍歷節點的途中順便處理next指針，整體來說只需要遍歷節點各1次就行！  
我上面的dfs遍歷各節點2次，雖然同樣也是O(N)，沒有太大差別，可確實是沒有這種方法優秀。  
只是不知道為啥跑得比dfs方法還慢就是了，可能是賦值太多次，尷尬。  

以level order的方式對樹遍歷，當q的大小為x時，代表該層共有x個節點，需要x次處理。  
維護變數prev，代表左方的節點，遍歷該層所有節點curr，若prev不為空，則將prev的next指針指向curr。最後更新prev為curr，並將左右子節點加入佇列中。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q=deque([root])
        while q:
            prev=None
            for i in range(len(q)):
                curr=q.popleft()
                if not curr:
                    continue
                if prev:
                    prev.next=curr        
                prev=curr
                q.append(curr.left)
                q.append(curr.right)
        
        return root
```