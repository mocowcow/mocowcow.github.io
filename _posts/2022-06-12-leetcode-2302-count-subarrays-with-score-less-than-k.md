--- 
layout      : single
title       : LeetCode 2302. Count Subarrays With Score Less Than K
tags        : LeetCode Hard Array SlidingWindow
---
雙周賽80。老實說這題感覺比Q3簡單，也可能是剛好這幾天sliding window做的多，手感比較順暢。

# 題目
陣列的**分數**定義為其總和與長度的乘積。  
例如[1, 2, 3, 4, 5]的分數為(1 + 2 + 3 + 4 + 5) * 5 = 75。  

輸入正整數陣列nums和整數k，回傳分數嚴格小於k的nums的非空子陣列的數量。  

# 解法
求子陣列數量的問題，通常可以將每個索引位置i作為結尾，計算以i結尾的子陣列數量。  

先拿例題一來分析看看：  
> nums = [2,1,4,3,5], k = 10  
> i=0 結尾的合法子陣列有[2]  
> i=1 結尾的合法子陣列有[1], [2,1]  
> i=2 結尾的合法子陣列有[4], [1,4]  
> i=3 結尾的合法子陣列有[3]  
> i=4 結尾的合法子陣列有[5]  

仔細想想，同一個結尾位置的子陣列，長度越長，乘積一定越大。那麼我們只需要找到最大長度那個子陣列，就可以知道這個位置的合法數量有幾個。  

維護變數r作為子陣列的起點，sm為子陣列總和。  
列舉nums中的每個索引位置r，找到以r為結尾的最長合法子陣列。  
若當前數字n已經大於等於k，那不可能有以r為結尾的子陣列，將sm清空，子陣列起點收縮到r的下一個位置。  
子陣列長度為r-l+1，若長度與總和的乘積達到k，則刪除左方的元素，直到小於k為止。這時候得到以r結尾的子陣列共r-l+1個，將其加入答案中。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        sm = 0

        for r, n in enumerate(nums):
            if n >= k:
                sm = 0
                l = r+1
                continue
            sm += n
            while sm*(r-l+1) >= k:
                sm -= nums[l]
                l += 1
            ans += r-l+1

        return ans
```
