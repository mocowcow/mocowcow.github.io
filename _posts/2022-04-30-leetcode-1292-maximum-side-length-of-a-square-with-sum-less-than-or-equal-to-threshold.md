--- 
layout      : single
title       : LeetCode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
tags        : LeetCode Medium Array Matrix BinarySearch PrefixSum
---
二分搜學習計畫。雖然不是比賽時碰到這題，但還是很欣慰我有先做好2D前綴和的模板，這種東西我可不想手動再刻一次。

# 題目
輸入一個M*N的矩陣mat，以及整數threshold。  
試著在mat中找邊長為k且元素總和不超過threshold的正方形，求k最大為多少。若不存在，則回傳0。

# 解法
好像也只能試著找不同邊長的正方形中有沒有符合的，邊長是有序成長，所以使用二分搜簡化搜尋次數。  
邊長最大不能超過M和N的最小值，所以上界取min(N,M)。最差狀況是找不到，下界設0。  
開始二分搜，如果能成功找到mid邊長正方形，則更新下界為mid；找不到則更新上界為mid-1。  
我試想lo=0, hi=1的情形：若mid取左中位數=0，會無法執行找邊長的函數，所以果斷改取右中位數=1。

在找邊長k正方形的的函數canDo(k)中，列舉每個可能的左上方座標，並加上(k-1)得到右下角座標，以2D前綴和O(1)時間得到總和，若小於threshold直接回傳true。列舉完所有左上角都沒符合的，才回傳false。

```python
class PrefixSum2D:
    def __init__(self, matrix):
        M, N = len(matrix), len(matrix[0])
        self.psum = [[0]*(N+1) for _ in range(M+1)]
        for r in range(M):
            for c in range(N):
                self.psum[r+1][c+1] = self.psum[r][c+1] + \
                    self.psum[r+1][c]-self.psum[r][c]+matrix[r][c]

    def rangeSum(self, r1, c1, r2, c2):
        return self.psum[r2+1][c2+1]-self.psum[r2+1][c1]-self.psum[r1][c2+1]+self.psum[r1][c1]
    
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M,N=len(mat),len(mat[0])
        ps=PrefixSum2D(mat)
        
        def canDo(k): # try to find any k*k <= threshold
            k-=1
            for r in range(M-k):
                for c in range(N-k):
                    if ps.rangeSum(r,c,r+k,c+k)<=threshold:
                        return True
            return False
        
        lo=0
        hi=min(M,N)
        while lo<hi:
            mid=(lo+hi+1)//2
            if not canDo(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
            
        
```
