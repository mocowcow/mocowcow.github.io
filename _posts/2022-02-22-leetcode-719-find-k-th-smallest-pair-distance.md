---
layout      : single
title       : LeetCode 719. Find K-th Smallest Pair Distance
tags 		: LeetCode Hard BinarySearch Sorting TwoPointers SlidingWindow
---
放在待辦清單好久了，今天總共挖出來做。

# 題目
輸入整數陣列nums及整數k，求第k小的**數對距離**。 
數對距離指的是ABS(nums[j]-nums[i])且滿足i<j。

# 解法
如同前幾篇提過的，測資超級大的話八成都可以用二分搜，這題剛好也是。  
先將nums排序，寫一個函數numOfPairsMost(int:x)，用來找距離不超過x的數對有多少。  
lower bound為最小的數對距離，也就是(第二個數-第一個數)，upper bound為最大的數對距離，也就是(最後一個數-第一個數)。開始二分搜，如果mid的數對量不足k，則更新low為mid+1；否則更新high為mid。最後mid就是答案。  

重點是numOfPairsMost函數做了什麼：使用left right指標模擬出一個滑動視窗。  
nums排序後，我們可以確定右方的元素一定不會小於左方元素。
而(left,right)代表由left和[left+1 .. right]產生(right-left)個數對，如[1,2,3]產生[1,2],[1,3]。  
既然如此，我們只需要對每個left找到最後一個不超過nums[right]-nums[left]的右邊界right，就可以確定i能和右方多少元素產生合法數對。值得注意的是，right變數可以延續使用之前的值，因為nums[left]的值只會增加，不可能減少，相對來講nums[right]的需求值也不可能減少，只會增加，所以right不可能出現往左跑的情況。

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def numOfPairsMost(x):
            left = cnt = 0
            right = 1
            while left < N:
                while right < N and (nums[right]-nums[left] <= x):
                    right += 1
                cnt += right-left-1
                left += 1
            return cnt

        N = len(nums)
        nums.sort()
        low = nums[1]-nums[0]
        high = nums[-1]-nums[0]
        while low < high:
            mid = (low+high)//2
            if numOfPairsMost(mid) < k:
                low = mid+1
            else:
                high = mid

        return low

```
