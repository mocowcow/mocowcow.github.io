---
layout      : single
title       : LeetCode 23. Merge k Sorted Lists
tags 		: LeetCode Hard Heap DevideAndConquer
---
好像是我最早解過的困難題之一，當初還開心一段時間。  

# 題目
輸入一個長度k的陣列，每一格都存著有序遞增的linked list，將所有linked list合併排序後回傳。

# 解法
剛開始我選擇逐一比較各list的元素。  
設立一個變數dummy作為新的head，另一個變數curr作為最後節點，之後遍歷所有lists，找出最小值m，再將所有值為m的node連接到curr後面，重複至lists全部為null為止。

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return
        N = len(lists)
        dummyHead = ListNode()
        curr = dummyHead
        while any(lists):
            m = min([n.val for n in lists if n])
            for i in range(N):
                while lists[i] and lists[i].val == m:
                    curr.next = ListNode(m)
                    curr = curr.next
                    lists[i] = lists[i].next

        return dummyHead.next
```

後來我認識新的資料結構heap，赫然發現正適合此題。  
heap是一種priority queue的實作，可以插入元素至合適的位置，保持有序。  
直接把所有node塞入heap中，再把node全部pop出並連接，就是一個有序的linked list。

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            while l:
                heappush(h, l.val)
                l = l.next

        curr = dummy = ListNode()
        while h:
            curr.next = ListNode(heappop(h))
            curr = curr.next

        return dummy.next
```

當然暴力法也是可以解決這題，全部node塞進陣列後排序再連接，程式碼就不付上了。