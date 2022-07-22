--- 
layout      : single
title       : LeetCode 86. Partition List
tags        : LeetCode Medium LinkedList TwoPointers
---
每日題。又是linked list，但沒有昨天的那麼麻煩。今天寫出來的code跟之前幾乎完全相同，差在變數名不同而已，真神奇。  

# 題目
輸入一個linked list的首節點和整數x，使得小於x的節點出現在list的前段，而大於等於x的節點出現在後段。  
分為前後兩段，每一段內的節點必須保持原來的相對順序。  

# 解法
對前後段各維護一個dummy節點，遍歷原本的list，若當前節點小於x則加入前段，否則加入後段。  
最後將前段的尾節點接上後段的首節點，再將後段的尾節點next清除即可。  

注意，若像例題1這種，若不清除末段尾節點則會造成死循環：  
> head = [1,4,3,2,5,2], x = 3  
> front = [1,2,**2**], back = [3,**5**]  
> 這時back的尾節點5，其next指向2，需手動設為null  

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        frontDummy=front=ListNode()
        backDummy=back=ListNode()
        curr=head
        
        while curr:
            if curr.val<x:
                front.next=curr
                front=front.next
            else:
                back.next=curr
                back=back.next
            curr=curr.next
            
        front.next=backDummy.next
        back.next=None
        
        return frontDummy.next
```
