--- 
layout      : single
title       : LeetCode 315. Count of Smaller Numbers After Self
tags        : LeetCode Hard Array BinarySearch SortedList BIT
---
聽說是經典題，特地來寫寫，仔細一看，這竟是我前陣子練習線段樹時有看過的題目，但那時候還真想不出怎麼做。

# 題目
輸入整數陣列nums，你必須回傳一個新的counts陣列。  
counts[i]代表著nums[i]右側較小元素的數量。

# 解法
初見時只有一個想法：O(N^2)暴力法，但是N會到10^5，是絕對不可能過的。  

想想既然要找右邊的較小元素，那應該是要從右邊往遍歷。  
對於遍歷到的數字n，需要一個資料結構將其計數+1，然後查找小於n的數字總出現次數有多少。  
再來想想看什麼資料結構可以快速查詢區間和：segment tree和binary indexed tree。  

線段樹前陣子用過不少次，這次改用樹狀陣列BIT。  
BIT是一種索引以0開始的**可變區間和查詢**資料結構，但是這題的數字範圍是[-10^4, 10^4]，所以需要額外加上10^4的位移，將範圍調整成[0, 2*10^4]。  
從右邊往左遍歷每個數字n，將其調整為n+offset，並查詢BIT中小於n+offset的數有幾個，更新至ans[i]，最後將n+offset的計數+1即可。

```python
class BinaryIndexedTree:

    def __init__(self, nums: List[int]):
        self.bit = [0]+nums  # restore range sum
        self.nums = nums  # original list
        self.N = len(self.bit)

    # add value to a certain index  
    def update(self, index: int, val: int) -> None:
        self.nums[index] += val
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    # get prefix sum from 0 to index
    def prefixSum(self, index: int) -> None:
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset=10**4
        bit=BinaryIndexedTree([0]*(offset*2+5))
        N=len(nums)
        ans=[0]*N
        for i in reversed(range(N)):
            n=offset+nums[i]
            ans[i]=bit.prefixSum(n-1)
            bit.update(n,1)

        return ans
```

偷雞解法：使用sorted list，速度竟然比BIT還快，媽呀。  
一樣從右方往左遍歷回來，對於每個數字n，在sl裡面找到最後一個小於等於n-1的索引位置idx，也就是bisect_right在-1。  
該idx再加1就是小於等於n-1的元素數量，可以把-1和+1抵銷，直接變成bisect_right(n-1)。

```python
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl=SortedList()
        N=len(nums)
        ans=[0]*N
        for i in reversed(range(N)):
            n=nums[i]
            ans[i]=sl.bisect_right(n-1)
            sl.add(n)

        return ans
```