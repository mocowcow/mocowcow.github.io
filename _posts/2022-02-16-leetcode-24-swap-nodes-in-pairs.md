---
layout      : single
title       : LeetCode 24. Swap Nodes in Pairs
tags 		: LeetCode Medium LinkedList
---
每日題，可怕的linked list，最常出現runtime error的問題種類。

# 題目
輸入一個linked list的head，將每兩個相鄰節點互換之後回傳，若只有剩一個則不動。  
不可以直接修改node的值，只能修改node本身。

# 解法
linked list問題大部分都可以用遞迴解決，而且也比較不容易噴錯。  
從head開始，每兩個節點互換，考慮成以下情況：  
1. head為空，沒得換，直接回傳head
2. head.next為空，只有一個節點，直接回傳head
3. 存在兩個以上節點，第三個開始為新區段，交由遞迴處理，然後一和二互換，接上剛處理完的新區段。  

例如A->B->C：  
1. 先遞迴處理C，C沒有下一個節點，回傳C
2. 把C接到A後面
3. 把A接到B後面

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp
```

試著改成疊代版本。  
原本的head前面加一個dummy head，比較好操作，curr變數為當前節點。  
對每個curr，檢查後面是否還存在兩個節點，若有則開始替換：  
1. 將curr後的兩個節點稱為a,b
2. 把b後面的那串接到a後面
3. 再把b接到curr後面
4. 再把a接到b後面
5. curr=a (等價於curr=curr.next.next)

示意圖：  
1. curr->A->B->C
2. curr->A->C  |  B->C
3. curr->B->C  |  A->C
4. curr->B->A->C 
5. curr->C

全部處理完回傳dummy.next就是答案。

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(next=head)
        while curr.next and curr.next.next:
            a = curr.next
            b = curr.next.next
            a.next = b.next
            curr.next = b
            b.next = a
            curr = a

        return dummy.next
```