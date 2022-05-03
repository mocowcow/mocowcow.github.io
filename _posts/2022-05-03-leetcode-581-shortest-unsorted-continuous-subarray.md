--- 
layout      : single
title       : LeetCode 581. Shortest Unsorted Continuous Subarray
tags        : LeetCode Medium Array TwoPointers Greedy Sorting
---
每日題。題號這麼前面，我竟然沒有做過，這題其實也挺好玩的。

# 題目
輸入陣列nums，你需要找到一個**連續的子陣列**，將之重新排序，可以使得整個nums為有序。  
求該子陣列的最短長度。

# 解法
題目說要重新排序的子陣列**正好一個**，表示我們可以將整個nums分成三等份：[左半邊不變]+[重排序]+[右半邊不變]。  
先將nums複製一份並排序好，分別從左往右找到左半邊的最後位i、從右往左找右半邊的最後位j。  
若nums原本就有序，則i>j，直接回傳0；否則回傳j-i-1，代表需要重新排序的子陣列長度。

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a=sorted(nums)
        N=len(nums)
        i=0
        j=N-1
        while i<N and nums[i]==a[i]:
            i+=1
        while j>=0 and nums[j]==a[j]:
            j-=1
            
        if i<j:
            return j-i+1
        
        return 0
```

follow up問有沒有O(N)的解法？上面方法使用排序就不符合了，要另外想想不用排序的方式。  
當某個數nums[i]值小於左方的任何數，會使得陣列亂序。我們從左往右掃，並維護左方見過的最大值，若碰到亂序的位置則將其記錄為r。  
同理，nums[j]值若大於右方的任何數，也會變得無序。從右往左掃，維護右方的見過的最小值，碰到亂序的位置則紀錄為l。  
最後l,r便是亂序子陣列的開頭和結尾，r-l+1得到子陣列的長度。

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        r=0
        l=N-1
        mx=-math.inf
        mn=math.inf
        for i in range(N):
            if nums[i]<mx:
                r=i
            mx=max(mx,nums[i])
        for i in range(N-1,-1,-1):
            if nums[i]>mn:
                l=i
            mn=min(mn,nums[i])
    
        if l<r:
            return r-l+1
        
        return 0
```
