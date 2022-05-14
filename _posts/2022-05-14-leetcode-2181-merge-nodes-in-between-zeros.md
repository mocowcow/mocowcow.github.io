--- 
layout      : single
title       : LeetCode 2181. Merge Nodes in Between Zeros
tags        : LeetCode Medium LinkedList Simulation
---
模擬周賽281。又是奇怪的一題，2N的解法竟然比N還快。

# 題目
輸入一個linked list的首節點，其中包含好幾個由0分隔開的整數，且此list的頭尾節點值都是0。  
將位於兩個0之間的節點值加總，合併為一個節點。合併完的list不應該存在任何0。  
回傳合併完的list。

# 解法
題目已經講明了頭尾一定是0，且最少出現3個節點以上，而且不會有兩個0相鄰，這樣就不用處理任何例外。  
輸入的list一定長成這樣的結構：  
> 0..0..0  

我們可以忽略掉第一個0，處理的邏輯就會從**合併兩個0之間的節點**簡化成**加總節點值，碰到0後結算**。  
維護變數sm，代表連續節點的加總值，指針curr從第二個節點開始向後遍歷：當curr不為0時，加總；否則建立一個值為sm的新節點，暫存在nodes中。  
遍歷完後nodes中會有數個合併完的節點，再遍歷一次nodes將其串接後回傳即可。

```python
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        curr=head.next
        sm=0
        while curr:
            if curr.val==0:
                nodes.append(ListNode(sm))
                sm=0
            else:
                sm+=curr.val
            curr=curr.next
            
        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
            
        return nodes[0]
```

也可以在合併時直接建立新節點並串接，遍歷次數降低到1次。  
利用偽首節點dummy儲存新建的節點，加上tail變數指向新節點的最尾端，每次碰到0節點時建立一個值為sm的新節點，附加到tail後方，再將tail後移一步。  
最後dummy.next就是新list的首節點。

```python
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=tail=ListNode()
        curr=head.next
        sm=0
        
        while curr:
            if curr.val==0:
                tail.next=ListNode(sm)
                tail=tail.next
                sm=0
            else:
                sm+=curr.val
            curr=curr.next
            
        return dummy.next
```