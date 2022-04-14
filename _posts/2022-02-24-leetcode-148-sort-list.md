---
layout      : single
title       : LeetCode 148. Sort List
tags 		: LeetCode Medium LinkedList TwoPointers Sorting DevideAndConquer
---
每日題，難度上下限很大，依據作法不同要說是easy或hard都可以。

# 題目
輸入節點head，表示linked list的頭，將list遞增排序後回傳。  
follow up:使用時間O(N log N)且空間O(1)

# 解法
最簡單的方法是把所有節點搬出來，直接當成整數排序，排完再接成list。  
空間複雜度是O(N)。

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None

        return nodes[0]

```

使用top down的merge sort，持續將list對半分割，直到每個子串列都是長度1，開始倆倆合併。  
額外空間只用於儲存分割的子串列，可以將空間壓到O(log N)。

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # split into 2 lists, respectively starts from head and slow
        prev.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, list1, list2):
        dummyHead = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummyHead.next

```

但題目要求O(1)，那只能使用bottom up的merge sort。  
首先計算整個串列長度N，從子串列大小size=1開始，每次翻倍，直到size>=N停止。  
對每個size，每次抓兩個size大小的子串列合併，直到整個串列處理完。  
例如：  
> head = [-1,5,3,4,0]  
> [(-1),(5),(3),(4),(0)] size=1  
> [(-1,5),(3,4),(0)] size=2  
> [(-1,3,4,5),(0)] size=4  
> [-1,0,3,4,5] size=8 排序完成

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = prev = head

        # count list size
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        # merge two sublists until sorted
        size = 1
        while size < N:
            curr = dummy.next
            prev = dummy
            while curr:
                left = curr
                right = self.split(curr, size)
                curr = self.split(right, size)
                prev = self.merge(left, right, prev)
            size *= 2

        return dummy.next

    def split(self, node, n):
        while node and n > 1:
            node = node.next
            n -= 1

        if not node:
            return None

        t = node.next
        node.next = None

        return t

    def merge(self, a, b, prev):
        curr = prev
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next

        if a:
            curr.next = a
        else:
            curr.next = b

        while curr.next:
            curr = curr.next

        return curr

```

2022-04-14更新：  
聽說有人白板題考bubble sort排linked list，我連什麼是bubble sort都快忘記，特此複習。  
雖然O(N^2)不出意外是太慢了些，喜聞樂見TLE。  

首先遍歷一次list，找到長度N。  
之後會進行N-1次的冒泡，第i次的冒泡會需要N-i-1次比較。例：  
> i=0，需要N-0-1次的比較  
> i=1，需要N-1-1次的比較  

以此類推。若第節點值大於子節點值的話則兩者交換，冒泡完N-1次後完成排序。

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # bubble sort
        # get full size
        size=0
        curr=head
        while curr:
            size+=1
            curr=curr.next
            
        #sort
        for i in range(size):
            last=size-i-1
            curr=head
            for _ in range(last):
                if curr.val>curr.next.val:
                    #swap
                    curr.val,curr.next.val=curr.next.val,curr.val
                curr=curr.next
            
        return head
```

