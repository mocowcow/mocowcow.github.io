--- 
layout      : single
title       : LeetCode 88. Merge Sorted Array
tags        : LeetCode Easy Array TwoPointers Sorting
---
每日題。非常棒的雙指針題，腦子愣了下，差點寫不出來。  

# 題目
輸入兩個已經遞增排序好的整數陣列nums1和nums2，以及兩個整數m和n，分別表示nums1和nums2中的元素個數。  
將nums1和nums2合併成一個遞增陣列。  

你必須直接修改nums1，而不是回傳新的陣列。因此nums1的長度為m+n，其中只有m個非0元素，後方的0應該被忽略。  

# 解法
最簡單的方法是開一個m+n的陣列，普通的合併之後再寫回去nums1。  
時間空間都是O(m+n)。  

第一個迴圈判斷nums1和nums2，選擇較小的元素先放到新陣列a。  
第二個迴圈填充nums1沒使用完的元素，第三個迴圈填充nums2沒使用完的元素。  
最後一個迴圈再把a寫回至nums1。

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=[0]*(m+n)
        i=j=k=0

        while i<m and j<n:
            if nums1[i]<nums2[j]:
                a[k]=nums1[i]
                i+=1
            else:
                a[k]=nums2[j]
                j+=1
            k+=1

        while i<m:
            a[k]=nums1[i]
            i+=1
            k+=1
            
        while j<n:
            a[k]=nums2[j]
            j+=1
            k+=1
            
        for i in range(m+n):
            nums1[i]=a[i]
```

follow up要求時間O(m+n)的演算法，其實上面那種方法應該符合要求，但是空間的部分確實還能繼續優化。  
nums1的元素都集中在前方，後面有n個空位，若把合併順序修改成**從後方往前寫入較大的元素**，就可以省下額外的記憶體空間，直接在nums1裡面排序，空間複雜度降到O(1)。  

稍微不同的是，我們只需特別處理nums2沒處理完的情況：假設nums1的所有元素都大於nums1，那麼nums1的元素會先全部被塞到後方，而nums2的指針都沒有動過，這時依然要將nums2剩餘元素塞滿剩下的空間；但若nums2所有元素都大於nums1，寫入完nums2後，nums1直接就是正確的順序，所以不需要再做處理。  

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        write=m+n-1
        
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[write]=nums1[i]
                i-=1
            else:
                nums1[write]=nums2[j]
                j-=1
            write-=1
        
        while j>=0:
            nums1[write]=nums2[j]
            j-=1
            write-=1
```
