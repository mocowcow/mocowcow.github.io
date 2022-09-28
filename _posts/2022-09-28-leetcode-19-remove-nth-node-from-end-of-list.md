--- 
layout      : single
title       : LeetCode 19. Remove Nth Node From End of List
tags        : LeetCode Medium LinkedList TwoPointers
---
每日題。滿經典的雙指針應用

# 題目
輸入linked list的首節點，刪除倒數第n個節點後回傳。  

# 解法
假設某list中總共有m個節點，倒數第n個節點，等價於第m-n+1個節點。  

最簡單的方法是遍歷一次list找到其總長度。  
但是當n=m時會出現例外，代表要刪除首節點，所以直接回傳head.next。  
否則找到第m+n+1前後兩個點連接起來，因為首節點實際上是第1個點，所以只需要往後前進m-n-1次就可以抵達第m-n個點。  

時間複雜度O(1)，空間複雜度O(1)。  

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        curr=head
        
        while curr:
            size+=1
            curr=curr.next
        
        if size==n:
            return head.next
        
        curr=head
        for _ in range(size-n-1):
            curr=curr.next
        
        curr.next=curr.next.next
        
        return head
```

運用雙指針方法可以簡化成一次遍歷。  
快慢指針fast和slow從首節點開始，先讓fast右移n次，之後兩指針同時向右移直到fast停下為止，slow正好會位於倒數第n個節點上。  

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=fast=head
        
        for _ in range(n):
            fast=fast.next
            
        if not fast:
            return head.next
            
        while fast.next:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        
        return head
```

也可以在原本的list前方加上dummy節點，這樣就不必特別處理刪除首節點的情況。  

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        slow=fast=dummy
        
        for _ in range(n):
            fast=fast.next
            
        while fast.next:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        
        return dummy.next
```
