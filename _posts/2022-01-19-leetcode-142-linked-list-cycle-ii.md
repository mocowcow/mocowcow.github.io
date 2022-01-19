---
layout      : single
title       : LeetCode 142. Linked List Cycle II
tags 		: LeetCode Medium TwoPointers
---
以前碰到的時候沒有仔細看，用了set硬解，這題真正想考的應該是快慢指標。

# 題目
輸入一個單向linked list，找出環的入口，若無則回傳null。

# 解法
使用快慢指標，先判斷有無環。  
若有環，環入口為E，相遇點為M。  
因fast是兩倍速，且又比slow多走一圈，head到E+E到M=環長度，  
也就是head到E=M再次回到E，所以從再從head和M同時往前，
最終會在E點相遇。

[這篇文](https://www.cnblogs.com/hiddenfox/p/3408931.html)有很清楚的解釋，十分感謝！

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
```
