--- 
layout      : single
title       : LeetCode 1574. Shortest Subarray to be Removed to Make Array Sorted
tags        : LeetCode Medium Array TwoPointers SlidingWindow
---
二分搜學習計畫。最佳解當然不是二分搜。

# 題目
輸入陣列arr，你可以刪除一個arr的子陣列，使得arr成為嚴格遞增。  
子陣列可以為空，求最小的子陣列長度。

# 解法
這題是真難，本想說函數二分搜找適合的刪除長度，但是沒辦法確認要從哪裡開始刪，後來去參考其他人題解。  

題目要求只能刪除一個子陣列，而且要盡可能的小。  
先找出arr左右兩邊的有序子陣列，使0\~L和R\~N-1都是有序，而L\~R中間就是無序的子陣列，是一定要刪除的部分。  
最差的情況有兩種：  
1. 將左方和中間全部刪除，使右方有序  
2. 將中間和右方全部刪除，使左方有序  

以此兩個最差情況為ans的初始值，開始以索引i,j做滑動窗口，i初始為0，j初始為R。  
若arr[j]<arr[i]，代表無法使arr有序，必須多刪除幾個，故將j向右移。  
j移動停止後，以j-i-1求得刪除子陣列長度，更新答案。

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:       
        N=len(arr)
        L=0
        while L<N-1 and arr[L]<=arr[L+1]:
            L+=1
            
        if L==N-1: # sorted
            return 0
        
        R=N-1
        while R>0 and arr[R-1]<=arr[R]:
            R-=1
        
        ans=min(R, N-L-1) # delete left or right part
        j=R
        for i in range(L+1):
            while j<N and arr[j]<arr[i]:
                j+=1
            ans=min(ans,j-i-1)
    
        return ans
```
