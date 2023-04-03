--- 
layout      : single
title       : LeetCode 2607. Make K-Subarray Sums Equal
tags        : LeetCode Medium Array UnionFind Sorting Math
---
雙周賽101。這題挺難的，完全找不到線索。  

# 題目
輸入整數陣列arr和整數k。  
陣列arr是**循環的**，也就是說末端元素的下一個元素是頂端元素，而頂端元素的前一個元素是末端元素。  

你可以執行以下操作任意次：  
- 選取arr中的一個元素，將其增加或是減少1  

求使得所有長度為k的**子陣列總和**相等，所需的最小操作次數。  

# 解法
使每個子陣列**總和相等**，其實意味著**完全相等**。  

以例題1的為例：  
> arr = [1,4,1,3], k = 2  
> 第一個子陣列應為arr[0], arr[1]  
> 第二個子陣列應為arr[1], arr[2]  
> 兩者總和相等，故arr[0] + arr[1] = arr[1] + arr[2]  
> 移項後得到arr[0] = arr[2]  

第1個子陣列的第1個元素和第2個子陣列的第1個元素相等、而第2個子陣列的第1個元素右和第3個子陣列的第1個元素相等，以此類推。  
暗示著每個子陣列的第i個元素都是相等的。  

因為子陣列大小為k，所以i的下一個相同元素位置為i+k。  
遍歷每個索引i，透過併查集將i和i+k合併。由於是循環陣列，所以i+k要模N避免越界。  

分完組後再來考慮如何透過最少的操作次數，來使得所有元素變得相等。  
例如某一組中有[1,2,3]這些元素，選1的話操作次數為0+1+2，選2的話是1+0+1，選3的話是2+1+0，很明顯中位數是最佳選擇。  
而在偶數元素的時候，選擇左右中位數都是可以的。如[1,5,8,9]，選5的操作次數為4+0+3+4，選8的操作次數為7+3+0+1。  

所以最後只要遍歷各個組別，將元素排序後，計算所有元素與中位數median的絕對差總和，加入答案即可。  

在k=1時，所有元素集中在同一組，瓶頸為排序，時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        N=len(arr)
        fa=list(range(N))
        
        def find(i):
            if fa[i]!=i:
                fa[i]=find(fa[i])
            return fa[i]
        
        def union(a,b):
            fa[find(a)]=find(b)
            
        for i in range(N):
            union(i,(i+k)%N)
            
        d=defaultdict(list)
        ans=0 
        
        for i in range(N):
            d[find(i)].append(arr[i])
        
        for v in d.values():
            v.sort()
            median=v[len(v)//2]
            for x in v:
                ans+=abs(x-median)
            
        return ans
```
