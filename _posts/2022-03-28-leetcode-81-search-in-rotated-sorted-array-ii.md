---
layout      : single
title       : LeetCode 81. Search in Rotated Sorted Array II
tags 		: LeetCode Medium BinarySearch Array
---
每日題。比較特殊的二分搜應用。

# 題目
輸入一個旋轉過的有序陣列nums，找target是否存在於裡面。

# 解法
旋轉指的是陣列元素向右搬移，而尾端元素移到左方。如[1,2,3]變成[3,1,2]。  
下界0，上界N-1，每次一樣取中點mid，如果剛好是target就回傳true，不是的話就比較麻煩。  
假設mid大於right，可以得知旋轉過後的起點介於mid和right之間，而0~mid-1的部分可以保證是有序的；若mid小於right，則保證右半邊是有序的；若mid等於right，兩邊都有可能是target正確位置，反正right一定不是target，就把right往左移一步。  
延續剛才判斷出哪邊有序，若左邊有序，且target又在左區間，則往左邊找，否則找右邊；反之，右邊有序且target於右區間，找右邊，否則找左邊。    

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid]>nums[right]: #left side sorted
                if nums[left]<=target<nums[mid]: #target in left side
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[right]: #right side sorted
                if nums[mid]<target<=nums[right]: #target in right side
                    left=mid+1
                else:
                    right=mid-1
            else:
                right-=1
            
        return False
        
```

