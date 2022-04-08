---
layout      : single
title       : LeetCode 703. Kth Largest Element in a Stream
tags 		: LeetCode Easy Design BinarySearch Heap
---
每日題。沒想到可以用heap。

# 題目
設計一個類別KthLargest，包含以下功能：  
- 建構子，每次要求第k大的元素，並以nums陣列初始化  
- int add(int val)，先加入val，之後回傳第k大的元素  

# 解法
一開始只想到排序nums後，每次add時先用二分搜找插入點，插入後再回傳倒數第k個元素。

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums,val)
        return self.nums[-self.k]
```

後來看到可以用heap實現，比較不好想到。  
維護min heap，如果元素超過k個就pop掉，這樣h裡面第一個元素剛好會是第k大的。  
> k = 3, nums = [4, 5, 8, 2]  
> h = [4,5,8]  
> add 3, pop 3, h = [4,5,8]  
> add 5, pop 4, h = [5,5,8]  
> add 10, pop 5, h = [5,8,10]  
> add 9, pop 5, h = [8,9,10]  
> add 4, pop 4, h = [8,9,10]

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.h=nums
        heapify(self.h)
        while len(self.h)>k:
            heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h,val)
        if len(self.h)>self.k:
            heappop(self.h)
        return self.h[0]
```