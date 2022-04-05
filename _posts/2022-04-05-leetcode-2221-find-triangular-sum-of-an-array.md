---
layout      : single
title       : LeetCode 2221. Find Triangular Sum of an Array
tags 		: LeetCode Medium Array
---
雙周賽75。大概是近期最佛心的第二題了，都不用思考。  
這題其實有點像巴斯卡三角形。

# 題目
輸入數列nums，裡面只會出現數字0~9。  
重複以下步驟直到nums剩下一個元素：  
1. nums長度為N，建立一個新陣列newNums，長度為N-1  
2. 對0<=i\<N-1的每個i，把(nums[i]+nums[i+1])%10放到newNums[i]裡面  
3. 以newNums取代nums  

# 解法
python list太好用了，連開陣列都不用，直接兩個相加取餘數後加到新陣列去就好。  

```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            t=[]
            for i in range(len(a)-1):
                x=(nums[i]+nums[i+1])%10
                t.append(x)
            nums=t

        return nums[0]
```

改成比較pythonic的解法。  

```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums)-1):
            nums=[(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]

        return nums[0]
```