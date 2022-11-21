--- 
layout      : single
title       : LeetCode 2476. Closest Nodes Queries in a Binary Search Tree
tags        : LeetCode Medium Array BinarySearchTree Tree BinarySearch Sorting
---
周賽320。這題Q2就有點過分了，同時要求對二分搜尋樹以及二分搜的理解，缺一不可。  

# 題目
輸入一棵**二分搜尋樹**的根節點root，共有n個正整數節點。  

生成一個大小為n的二維整數陣列answer，其中answer[i] = [min<sub>i</sub>, max<sub>i</sub>]：  
- min<sub>i</sub>為小於等於於queries[i]的**最大**節點值  
- max<sub>i</sub>為大於等於於queries[i]的**最小**節點值  

回傳answer陣列。  

# 解法
二分搜尋樹正如其名，就是拿來給你做二分搜的。但是題目可沒說這是平衡樹，他可能是一直線的
linked list，直接在上面找值會退化成**線性時間**，複雜度變成O(MN)，直逼10^11次運算。  

一份測資要拿來搜尋M次，不妨利用二分搜尋樹本身的特性，以中序dfs將其轉換成大小N的
有序整數陣列再進行二分搜。遍歷樹的時間為O(N)，不清楚特性的朋友也可以隨便次序取值，
最後再花一次O(N log N)排序。  

接下來要找第最後一個小於等於queries[i]的整數，以及第一個大於等於queries[i]的整數。  
先找到第一個大於等於q[i]的索引位置idx，分類討論四種結果：  
1. 所有數字都小於q[i]，所以idx等於N，將max設為-1，而min就是idx-1  
2. 正好存在等於q[i]的數，兩者都等於q[i]   
3. 因為已經過濾掉idx等於q[i]的情況，若idx的數大於q[i]，則idx-1一定小於q[i]  
4. 若idx為0，則不存在小於q[i]的數，設min為-1  

總共對大小N的陣列做M次二分搜，時間複雜度O(M log N)。忽略保存答案的O(M)，儲存所有節點空間為O(N)。
  
```python
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a=[]
        
        def dfs(o):
            if not o:return
            dfs(o.left)
            a.append(o.val)
            dfs(o.right)
        
        dfs(root)
        
        N=len(a)
        ans=[]
        for q in queries:
            idx=bisect_left(a,q)
            if idx==N:
                ans.append([a[idx-1],-1])
            elif a[idx]==q:
                ans.append([q,q])
            elif idx>0:
                ans.append([a[idx-1],a[idx]])
            else:
                ans.append([-1,a[idx]])
                
        return ans
```

如果覺得分類討論很麻煩，也可以改成兩次二分搜：
- 找**第一個**大於等於q[i]的索引 
- 找**最後一個**小於等於q[i]的索引 

只要超出陣列邊界(等於N或是小於0)則設為-1。  

```python
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a=[]
        
        def dfs(o):
            if not o:return
            dfs(o.left)
            a.append(o.val)
            dfs(o.right)
        
        dfs(root)
        
        N=len(a)
        ans=[]
        for q in queries:
            mx=mn=-1
            idx=bisect_left(a,q)
            if idx<N:
                mx=a[idx]
            idx=bisect_right(a,q)-1
            if idx>=0:
                mn=a[idx]
            ans.append([mn,mx])
                
        return ans
```