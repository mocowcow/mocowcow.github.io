--- 
layout      : single
title       : LeetCode 2454. Next Greater Element IV
tags        : LeetCode Hard Array BinarySearch Sorting SortedList HashTable
---
雙周賽90。眼殘到不行，明明範例一和我的答案不同，還是交了出去，好冤枉的WA。即使總共吃了4個BUG，還是拿到600名，也不算太差。  

# 題目
輸入非負整數陣列nums。對於每個nums[i]，你必須找到**第二個更大的數**。  

若找不到第二個更大的數，則設為-1。  
例如陣列[1,2,4,3]中，1的第二大數是4；2是3；3和4是-1。  

回傳整數陣列answer，其中answer[i]是nums[i]的**第二個更大的數**。  

# 解法
題目要求要找到在右方、又要比當前元素大的第二個數，非常麻煩。  
但是我們將元素由大到小依序加入sorted list，這樣就能確保list內元素一定比當前的還大，只剩下要找到哪些在右方。  
可以將元素以其索引來表示，使用二分搜就可以找到當前元素插入位置idx，再往右一格就是要找的**第二個更大的數**。  

注意：當某個元素n出現在多個索引上，一定要等到**全部處理完**才能加入list中，否則二分搜會被干擾。  

排序O(N log N)，需要二分搜+插入list共N次，也是O(N log N)。空間複雜度O(N)。  

```python
from sortedcontainers import SortedList

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[-1]*N
        
        d=defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
            
        sl=SortedList()
        for k in sorted(d.keys(),reverse=True):
            for i in d[k]:
                idx=sl.bisect_left(i)+1
                if idx<len(sl):
                    ans[i]=nums[sl[idx]]
            # add all elements
            for i in d[k]:
                sl.add(i)
        
        return ans
```

或是先將整個nums重新排序，值較大者放前面，值同等的以索引小的優先。這樣加入相同的元素保證可以先將較左的加入sorted list，不影響二分搜結果。  

```python
from sortedcontainers import SortedList

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[-1]*N
            
        sl=SortedList()
        a=[[i,n] for i,n in enumerate(nums)]
        a.sort(key=lambda x:(-x[1],x[0]))
        
        for i,_ in a:
            idx=sl.bisect_left(i)+1
            if idx<len(sl):
                ans[i]=nums[sl[idx]]
            sl.add(i)
        
        return ans
```