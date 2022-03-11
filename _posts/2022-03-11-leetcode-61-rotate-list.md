---
layout      : single
title       : LeetCode 61. Rotate List
tags 		: LeetCode Medium LinkedList TwoPointers
---
每日題。其實我不確定這算不算雙指標，應該勉強算吧。

# 題目
輸入一linked list的head，將其向右旋轉k次。  
> head = [1,2,3,4,5], k = 2  
> rotated = [4,5,1,2,3]

# 解法
首先過濾幾種不用更動的狀況：空串列、長度一串列或是k=0，直接回傳head。  
再來計算整個串列長度size，方便之後旋轉。再拿k模size檢查一次看是否餘0，若是則可直接回傳。  
把原串列分為前後兩部分，前面長度為size-k，後面長度為k。所以從head開始向後前進size-k-1次可以抵達newHead，保存位置並切斷連結。  
最後再從newHead走到尾端，接上原本的head就成功旋轉了。

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        k %= size
        if k == 0:
            return head

        move = size-k
        curr = head
        for _ in range(move-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None

        curr = newHead
        while curr.next:
            curr = curr.next
        curr.next = head

        return newHead

```
