--- 
layout      : single
title       : LeetCode 2487. Remove Nodes From Linked List
tags        : LeetCode Medium LinkedList Stack MonotonicStack
---
周賽321。還真是我用單調堆疊最順手的一次。  

# 題目
輸入一個linked list的首節點head。  

若某節點的右方存在**嚴格較大**的節點，則將其刪除。  

回傳修改後的首節點。  

# 解法
直接修改節點值似乎有點算是偷吃步，但題目也沒說不行，那就當他是可行的。  

每個節點的右方若有更大節點，則會被刪除；換句話說就是使得list成為**遞減**。  
維護一個單調遞減堆疊，依序遍歷所有節點，只要出現較大的節點，則把先前較小的所有節點都彈出。最後將處裡完的節點串接起來回傳。  

遍歷list最多兩次，時間O(N)。最差情況下不會刪除任何節點，全部放入堆疊中，空間O(N)。  

```python
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=[]
        curr=head
        while curr:
            while st and curr.val>st[-1].val:
                st.pop()
            st.append(curr)
            curr=curr.next
            
        for a,b in pairwise(st):
            a.next=b
        
        return st[0]
```

最合適的解法應該是透過遞迴，找到每個節點右方的最大值，依此判斷要不要刪除當前節點。  

如果右方沒節點了，直接回傳；如果右方首節點t大於當前節點node，直接回傳t；否則將t串到node後面，回傳node。  

時空間一樣都是O(N)。  

```python
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def f(node):
            if not node:return
            t=f(node.next)
            if not t:return node
            if t.val>node.val:return t
            node.next=t
            return node
        
        return f(head)
```