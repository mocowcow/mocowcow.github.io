---
layout      : single
title       : LeetCode 138. Copy List with Random Pointer
tags 		: LeetCode Medium LinkedList HashTable
---
每日題。  
還滿有趣的題目，大部分人都是使用O(N) space-time解法，沒想到竟然會出現O(1) space[解法](https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43497/2-clean-C%2B%2B-algorithms-without-using-extra-arrayhash-table.-Algorithms-are-explained-step-by-step.)，敬佩不已。晚點深入研究。

# 題目
輸入一個linked list，比一般的節點多出一個random參照，指向此list中的隨機位置。把list深度複製一份後回傳。

# 解法
雖然以前做過，這次重逢還是被題目的"random"嚇一跳，想說是什麼鬼東西，其實就當作是兩個出口就好。  
把複製拆解成兩個大動作：  
1. 先複製線性出現的節點，同時以舊節點為key，存到nodes建立與新節點的映射，舊random參照暫存在新節點上  
2. 再遍歷一次新串列，把原本暫存的random參照到nodes裡更新為真正對應的節點

此方法簡單暴力，速度勝過了97.3%的解答。

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        nHead = Node(head.val, random=head.random)
        nodes = {head: nHead}
        curr1 = head
        curr2 = nHead
        # copy new list and mapping
        while curr1.next:
            curr1 = curr1.next
            curr2.next = Node(curr1.val, random=curr1.random)
            curr2 = curr2.next
            nodes[curr1] = curr2

        # relink random
        curr2 = nHead
        while curr2:
            if curr2.random:
                curr2.random = nodes[curr2.random]
            curr2 = curr2.next

        return nHead

```
