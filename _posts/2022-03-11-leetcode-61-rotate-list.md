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

參考[別人解法](https://leetcode.com/problems/rotate-list/discuss/22715/Share-my-java-solution-with-explanation)，加上一個dummy head會更好處理。  
拿dummy接上head，所有遍歷都從dummy開始。  
一樣先計算長度，只是判斷條件改為後方還有節點時才前進，這樣可以停在最後一點，而不是null上。  
size模k跟之前一樣。  
再來就是其中精髓：數完長度馬上把串列頭尾接上，之後就不必再跑一次了！  
最後是找切斷點mid，從dummy開始數，多一個點，所以size-k就可以，剛好抵銷-1。最後保存newHead，切斷連結回傳即可。

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        dummy = ListNode(next=head)
        size = 0
        tail = dummy
        while tail.next:
            size += 1
            tail = tail.next

        k %= size
        if k == 0:
            return head

        tail.next = head
        mid = dummy
        for _ in range(size-k):
            mid = mid.next

        newHead = mid.next
        mid.next = None

        return newHead


```