---
layout      : single
title       : LeetCode 3217. Delete Nodes From Linked List Present in Array
tags        : LeetCode Medium Array LinkedList Simulation HashTable
---
周賽 406。完全可以感受到出題人想打混摸魚的心情。  

## 題目

輸入整數陣列 nums，還有一個 linked list 的首節點 head。  
刪除所有存在於 nums 中的節點，並回傳修改後的首節點。  

## 解法

nums 值很多，先裝進雜湊表供快速查找。  
遍歷一次 linked list，把**不刪除**的節點留下來，重新連接後回傳即可。  

題目有保證至少會有一個節點不被刪除，因此不需考慮空 list 的情況。  

時間複雜度 O(N + M)，其中 M 為 list 長度。  
空間複雜度 O(N + M)。  

```python
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        a = []
        curr = head
        while curr:
            if curr.val not in s:
                a.append(curr)
            curr = curr.next

        for prev, next in pairwise(a):
            prev.next = next
        a[-1].next = None

        return a[0]
```

也可以原地刪除，不使用額外空間。  
為應對刪除首節點的情形，需要加上哨兵節點。  

時間複雜度 O(N + M)。  
空間複雜度 O(N)。  

```python
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        prev = dummy = ListNode(next=head)
        curr = head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
```
