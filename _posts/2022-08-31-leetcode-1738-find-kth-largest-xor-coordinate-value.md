--- 
layout      : single
title       : LeetCode 1738. Find Kth Largest XOR Coordinate Value
tags        : LeetCode Medium Array Matrix BitManipulation PrefixSum Heap
---
隨便抽到的題。算是2D前綴和的變種題，但是有一些可以優化的小地方。  

# 題目
輸入m\*n的矩陣，由非負整數組成，還有一個整數k。  
產生另一個矩陣，其座標(a,b)的值為所有matrix[i][j]的XOR結果，其中0<=i<=a<m且0<=j<=b<n。  

找到矩陣中第k大的值。  

# 解法
中心思想和[304. range sum query 2d   immutable]({% post_url 2022-03-25-leetcode-304-range-sum-query-2d---immutable %})一樣，由四個區域來計算出當前的總和。  
差別在於XOR的特性，相同的數字會相消，所以四個區塊互相做XOR就好。  
計算出每個位置的XOR總和之後，排序並回傳第k大的值。  

記算XOR總和矩陣的複雜度為O(M\*N)，共有MN個元素。排序複雜度為O(MN log MN)，整體複雜度為O(MN log MN)。  

```python
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M,N=len(matrix),len(matrix[0])
        dp=[[0]*N for _ in range(M)]
             
        for r in range(M):
            for c in range(N):
                up=0 if r==0 else dp[r-1][c]
                left=0 if c==0 else dp[r][c-1]
                upleft=0 if (c==0 or r==0) else dp[r-1][c-1]
                dp[r][c]=up^left^upleft^matrix[r][c]
                        
        return sorted(dp[r][c] for r in range(M) for c in range(N))[-k]
```

可以使用min heap代替排序，只維護k個最大的元素，將複雜度將低到O(M\*N log k)。  
在產生XOR總和的過程中只保留大的k個元素，如果新加入的值後超過k個，則彈出最小的。如此一來heap頂端將會是第k大的總和，因為M\*N個更小的元素已經被刪掉了。  

```python
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M,N=len(matrix),len(matrix[0])
        dp=[[0]*N for _ in range(M)]
        h=[]
             
        for r in range(M):
            for c in range(N):
                up=0 if r==0 else dp[r-1][c]
                left=0 if c==0 else dp[r][c-1]
                upleft=0 if (c==0 or r==0) else dp[r-1][c-1]
                dp[r][c]=up^left^upleft^matrix[r][c]
                if len(h)==k:
                    heappushpop(h,dp[r][c])
                else:
                    heappush(h,dp[r][c])
                        
        return h[0]
```