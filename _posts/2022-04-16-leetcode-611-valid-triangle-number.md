---
layout      : single
title       : LeetCode 611. Valid Triangle Number
tags 		: LeetCode Medium Array TwoPointers BinarySearch
---
二分搜學習計畫。這題就比較適合一些了。

# 題目
輸入整數數列nums。任選三個數字組成三角形，求有幾種組合方式。

# 解法
三角形的組成要件是：兩短邊相加大於長邊。  
邊長不可能為0，所以先把0過濾掉之後排序。  
之後使用雙指標i, j分別代表兩短邊，長度和為two。用二分搜找第一個大於等於two的位置，再扣1就是最後一個不大於two的位置。  
最後k到j的距離就是可以和此i, j形成三角形的數量。

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums=sorted(x for x in nums if x>0)
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i+1,N):
                two=nums[i]+nums[j]
                k=bisect_left(nums,two)-1
                ans+=k-j
                
        return ans
```

改用雙指標寫法。一樣先去0排序。  
長邊k一定要有兩個更小的數，所以從索引2開始往右遍歷，i, j一樣代表兩個短邊。  
若(i,j,k)可以組成三角型，因為數列是漸增的，所以i+1, i+2 .. j-1 全都可以和j, k組成三角形，故答案增加j-i個，把用過的j往左移；若無法組成三角形，需要將短邊長度調高，但我們能改的只有i，則i向右移動。

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums=sorted(x for x in nums if x>0)
        ans=0
        for k in range(2,len(nums)):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    ans+=j-i
                    j-=1
                else:
                    i+=1
                    
        return ans
```