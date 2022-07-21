--- 
layout      : single
title       : LeetCode 92. Reverse Linked List II
tags        : LeetCode Medium LinkedList TwoPointers
---
每日題。本來覺得這題很麻煩，但是找到了神一般的題解，難度瞬間下降許多。

# 題目
輸入單向linked list的head和兩個整數left與right，其中left <= right。將第left到right節點的範圍反轉，並返回反轉後的list。  

# 解法
第一個想法當然還是把所有節點依序裝入陣列中，透過陣列索引來存取各節點，並使用雙指針進行換值，需要兩次遍歷。  
若不允許更改節點值，則改成將整個節點交換，需要三次遍歷。  

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes=[]
        curr=head
        
        while curr:
            nodes.append(curr)
            curr=curr.next
            
        l=left-1
        r=right-1
        while l<r:
            nodes[l].val,nodes[r].val=nodes[r].val,nodes[l].val
            l+=1
            r-=1
            
        return head
```

follow up要求只用一次遍歷就完成反轉，我一下子還真想不到。看了不少題解都沒有滿意的，直到發現[這篇](https://leetcode.cn/problems/reverse-linked-list-ii/solution/java-shuang-zhi-zhen-tou-cha-fa-by-mu-yi-cheng-zho/)，整個邏輯都鮮明起來。這方法有個很動聽的名字：**頭插法**。  

因為反轉的範圍有可能包含首節點head，所以需要使用dummy連接head，才有辦法在反轉後取到新的首節點。  
找到left的前一個節點，稱為guard，作為每次插入的位置，並將第left個節點稱為curr，開始插入。  
我們總共會進行right-left次插入。curr的下一個節點稱為temp，將curr移動至temp.next，才將temp插入至guard後方。  

自己也做一次圖解強化印象，希望能夠記住這種好方法。  
![示意圖](/assets/img/92-1.jpg)

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        
        guard=dummy
        for _ in range(left-1):
            guard=guard.next
            
        curr=guard.next
        for _ in range(right-left):
            temp=curr.next
            curr.next=t.next
            t.next=guard.next
            guard.next=temp
        
        return dummy.next
```