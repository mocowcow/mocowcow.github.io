---
layout      : single
title       : LeetCode 143. Reorder List
tags 		: LeetCode Medium LinkedList TwoPointers
---
今天帶臭狗去照心臟超音波，打了利尿劑，結果把我褲子全都尿濕了。

# 題目
輸入一linked list，將其重新排序，先從前端取一個，再從尾端取一個。  
如[1,2,3,4,5,6]變成[1,6,2,5,3,4]。 

# 解法
以前把所有節點裝到陣列裡面用雙指標取出重連，雖說不是不行，但就沒有linked list的味道，今天改以節點操作為主。  
可以觀察出答案是由前半段保持原序，而後半段反轉後交織插入。主要分為三大步驟：  
1. 先用快慢指針找到中心點  
2. 將後半段反轉，並斷開連結  
3. 將兩個子串列合併  

值得一提的是合併的部分，我是先對兩子串列各用一個temp保存next，串接後才將指標移回temp上。看到有人採用l1和l2交替的方式，非常漂亮。  

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into 2 lists
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse second
        curr=slow.next
        prev=None
        slow.next=None
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        
        # merge
        l1=head
        l2=prev
        while l2:
            t1=l1.next
            t2=l2.next
            l1.next=l2
            l2.next=t1
            l1=t1
            l2=t2

        # 另一種合併法 
        # l1=head
        # l2=prev
        # while l2:
        #     t=l1.next
        #     l1.next=l2
        #     l1=l1.next
        #     l2=t
```

還有人用stack來做，雖然說和塞進陣列差不多意思，不過也是很好玩，還莫名的快。  
先把節點全部塞進stack後，計算總數，再從stack取出節點插入前方，重複size/2次。

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # into stack
        st=[]
        curr=head
        while curr:
            st.append(curr)
            curr=curr.next
        size=len(st)
        
        # insert
        curr=head
        for _ in range(size//2):
            t=curr.next
            curr.next=st.pop()
            curr=curr.next
            curr.next=t
            curr=t
            
        curr.next=None
        
        return head
```