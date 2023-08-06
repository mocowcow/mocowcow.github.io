---
layout      : single
title       : LeetCode 2807. Insert Greatest Common Divisors in Linked List
tags        : LeetCode Medium Array LinkedList
---
雙周賽110。沒什麼陷阱的單純題目，可能是最近幾次最良心的Q2。  

## 題目

輸入一個linked list的首節點，每個節點都有一個整數值。  

在每兩個節點中插入一個新節點，其值為兩者的gcd。  

回傳插入新節點後的linked list。  

## 解法

按照題意模擬。  

比賽時求穩，把所有節點拿出來後才逐一插入新節點。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
            
        if len(nodes)==1:
            return head
        
        for a,b in pairwise(nodes):
            g=gcd(a.val,b.val)
            o=ListNode(g)
            a.next=o
            o.next=b
            
        return head
```

其實不需要額外空間，只要檢查後方是否還有節點即可。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr.next:
            nxt=curr.next
            val=gcd(curr.val,nxt.val)
            o=ListNode(val,nxt)
            curr.next=o
            curr=nxt
            
        return head
```
