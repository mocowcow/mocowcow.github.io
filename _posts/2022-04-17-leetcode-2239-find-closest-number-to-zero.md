---
layout      : single
title       : LeetCode 2239. Find Closest Number to Zero
tags 		: LeetCode Easy Array Sorting Greedy
---
雙周賽76。剛好超適合python的題，其他語言可能要寫比較多行。

# 題目
輸入整數數列nums，回傳其中最靠近0的數字。如果有多個答案，則選擇較大者。

# 解法
靠近0的距離就是絕對值。  
直接排序，絕對值越小的優先，但是像1和-1絕對值相同，題目要求選擇較大的數，也就是正數，所以排序的第二個key是數字本身的正負。

```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:(abs(x),-x))
        return nums[0]
```

不排序的話應該是使用O(N)解法，在abs(n)更小的情況，或abs相同但n更大時更新答案。  

```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans=math.inf
        for n in nums:
            if abs(n)<abs(ans) or (abs(n)==abs(ans) and n>ans):
                ans=n
                
        return ans
```
