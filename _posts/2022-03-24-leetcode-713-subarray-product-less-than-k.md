---
layout      : single
title       : LeetCode 713. Subarray Product Less Than K
tags 		: LeetCode Medium Array SlidingWindow
---
學習計畫碰到的。好像有一段時間沒有做滑動視窗。

# 題目
輸入整數陣列nums，以及整數k。求有多少連續子陣列其乘積小於k。

# 解法
乘積prod初始化為1，用deque作為視窗本體，就不用算邊界值，比較方便。  
將每個整數n加入window右方，prod乘上n，若prod超過k則從左方彈出一個數字，並將prod除以該數。  
window的大小等於連續子陣列的個數。如window=[10,5,2]時，以2結尾的子陣列共有[10,5,2],[5,2],[2]三種。故將答案加上視窗大小。

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans=0
        prod=1
        window=deque()
        
        for n in nums:
            prod*=n
            window.append(n)
            while prod>=k and window:
                prod//=window.popleft()
            ans+=len(window)
            
        return ans
```

