---
layout      : single
title       : LeetCode 1721. Swapping Nodes in a Linked List
tags 		: LeetCode Medium LinkedList TwoPointers
---
每日題。滿單純的題目，但是可以透過位移的觀念將邏輯簡化，滿好玩的。

# 題目
輸入一個linked list，以及整數k，將從左數來第k個節點和從右數來第k個節點互換，並回傳互換完的結果。

# 解法
暴力法，先遍歷一次算大小size，從右數來第k個等價於從左數來第size-(k-1)個。分別走到定點後交換即可。

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        size=0
        curr=head
        while curr:
            size+=1
            curr=curr.next
        
        back=size-(k-1)
        a=b=dummy
        for _ in range(k):
            a=a.next
        for _ in range(back):
            b=b.next
        if a.val!=b.val:
            a.val,b.val=b.val,a.val
            
        return dummy.next
```

先找到左數第k個點left之後，把tail設為left，把right設為head，一直把tail和right同時往右邊移動，直到最後一點，right就剛好停在右數第k點上了。

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left=head
        for _ in range(k-1):
            left=left.next
        
        right=head
        tail=left
        while tail.next:
            tail=tail.next
            right=right.next
            
        left.val,right.val=right.val,left.val
        
        return head
```