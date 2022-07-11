--- 
layout      : single
title       : LeetCode 2334. Subarray With Elements Greater Than Varying Threshold
tags        : LeetCode Hard Array UnionFind Stack MonotonicStack
---
雙周賽82。自己完全想不出頭緒，看了提示發現有兩種方法，實作起來都不會太困難。  

# 題目
輸入整數陣列nums和整數threshold。  
找到任何長度k的nums子陣列，且子陣列中的每個元素都大於threshold / k。  

回傳任一合法的子陣列大小。若不存在則回傳-1。  

# 解法
提示說了可以列舉每個元素作為子陣列中的最小值，以此找到左右邊界，有點像是[2281. sum of total strength of wizards]({% post_url 2022-05-22-leetcode-2281-sum-of-total-strength-of-wizards %})。  

使用單調遞增堆疊，分別以正反兩次找到每個子陣列的左右邊界。最後列舉子陣列邊界，得到子陣列大小size，若合法則回傳其大小。  
總共需要三次遍歷，複雜度為O(N)。  

```python
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        N=len(nums)
        lb=[0]*N
        rb=[N-1]*N
        st=[]
        for i,n in enumerate(nums):
            while st and n<nums[st[-1]]:
                t=st.pop()
                rb[t]=i-1
            st.append(i)
            
        st=[]
        for i in range(N-1,-1,-1):
            n=nums[i]
            while st and n<nums[st[-1]]:
                t=st.pop()
                lb[t]=i+1
            st.append(i)
            
        for i,n in enumerate(nums):
            size=rb[i]-lb[i]+1
            if n>threshold//size:
                return size
            
        return -1
```

還有一種比較奇特的併查集解法，比較難想到，也比較難實現。  
nums[i]的值越大，則越有可能符合threshold/k的限制，因此依照元素大小遞減排序，試著依序加入每個索引位置。  

遍歷排序後的索引i，將i加入併查集中，並試著對相鄰的左右索引合併。計算以和i連通的索引共有多少個，即為當前子陣列大小。因為我們是以遞減順序加入索引，所以可以保證當前陣列的最小值一定是nums[i]，以nums[i]/size檢查子陣列是否合法。 

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}


    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[px]=py
        self.size[py]+=self.size[px]


    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        ns=sorted(enumerate(nums),key=itemgetter(1),reverse=True)
        uf=UnionFind()
        
        for i,num in ns:
            uf.parent[i]=i
            uf.size[i]=1
            if i-1 in uf.parent:
                uf.union(i,i-1)
            if i+1 in uf.parent:
                uf.union(i,i+1)
            root=uf.find(i)
            if num>threshold//uf.size[root]:
                return uf.size[root]
            
        return -1
```