---
layout      : single
title       : LeetCode 10037. Maximum Size of a Set After Removals
tags        : LeetCode Medium Array Math HashTable
---
周賽379。想了二十分鐘，想到個很神奇的解，送出去還真對了。  

## 題目

輸入兩個長度n的整數陣列nums1和nums2。  

你必須分別從nums1和nums2之中移除 n/2 個元素。  
然後將留下來的元素全都加入集合s中。  

求s的**最大**大小。  

## 解法

最理想的狀況下，當然是nums1, nums2各擁有至少n/2個不同的元素。例如：  
> nums1 = [1,2], nums2 = [1,2], s = [1,2]  
或是：  
> nums1 = [1,2], nums2 = [3,4], s = [1,3]..  

先看前者，每個陣列都有n個不同的元素，而且兩陣列之間**有交集**。兩陣列提供的元素可能會**重複**。  
但我不在乎怎樣選才不重複，只想知道這兩陣列的聯集總共有多少不同元素。  
就像範例1：  
> nums1 = [1,2,1,2], nums2 = [1,1,1,1]  
nums1可以提供[1,2]，但nums2只能提供[1]。兩者聯集是[1,2]，就算不限貢獻個數的情況下，也只能湊出[1,2]兩個。  

再看看後者的情況是，每個陣列都有n個不同的元素，而且兩陣列之間**沒有交集**。但是只能選擇其中n/2個。  
但有時候陣列中的不同元素根本不足n/2個，所以nums1能提供的不同元素最多是min(len(set(nums1)), n/2)個；nums2同理。  
就算兩者聯集是[1,2,3,4]超過n=2個元素，也會受到每個陣列只提供n/2限制，最多只能從裡面挑出2個元素。  

答案就是這兩個情形取最小值。  

時間複雜度O(m+n)。  
空間複雜度O(m+n)。  

```python
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        s1=set(nums1)
        s2=set(nums2)
        s=s1 | s2
        
        return min(
            len(s),
            min(len(s1),N//2) + min(len(s2),N//2)
        )
```
