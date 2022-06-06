--- 
layout      : single
title       : LeetCode 160. Intersection of Two Linked Lists
tags        : LeetCode Easy LinkedList TwoPointers
---
每日題。

# 題目
輸入兩個單向linked list的首節點headA和headB，回傳相交的節點。若無交集則回傳null。  

# 解法
最簡單的方法是把A的所有節點裝進set中，再去遍歷B，如果途中發現set中有重複的點，就代表是交集。  
假設A的長度是M，而B的長度是N，時間複雜度為O(N+M)，空間O(M)。  

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen=set()
        a=headA
        b=headB
        while a:
            seen.add(a)
            a=a.next
            
        while b:
            if b in seen:
                return b
            b=b.next
            
        return None
```

follow up要求時間複雜度O(N+M)，空間O(1)，那麼就不能用set了。  
依照描述，兩個list交集之後就只會剩下一條路線，不會再分岔，那麼可以知道交點開始之後的長度都相同。  

首先各遍歷一次A和B，分別計算出長度的差diff，哪方較長則先行移動diff步。  
之後兩者同時往後走，若a和b為相同的節點，則代表是交集。  

```python   
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        aSize=0
        bSize=0
        
        while a:
            aSize+=1
            a=a.next
            
        while b:
            bSize+=1
            b=b.next
            
        a=headA
        b=headB
        
        if aSize>bSize:
            for _ in range(aSize-bSize):
                a=a.next
        else:
            for _ in range(bSize-aSize):
                b=b.next
                
        while a:
            if a==b:
                return a
            a=a.next
            b=b.next
        
        return None
```
