---
layout      : single
title       : LeetCode 1675. Minimize Deviation in Array
tags 		: LeetCode Hard Heap Greedy
---
每日題，很少看到題號這麼後面的被選中。

# 題目
輸入整數陣列nums，可以對任意元素進行無限次操作：  
- 若數字是偶數，則除2
- 若數字是奇數，則乘2

定義偏差值為nums中最大元素-最小元素，試將偏差值最小化。  

# 解法
提示1說：先把所有數字變成最大可能值，指的是什麼意思？  
偶數的數字只能做除法運算，不可能比當前更大。所以把所有奇數乘2，就能達到最大可能值。  
要讓偏差值最小化，需要將最小元素盡可能大，而最大元素盡可能小。  
在數字都是偶數的狀態下，所有數字都只能做除法運算了，已經可以確定**最小元素最大化**了。意味著我們只要嘗試最大值縮小即可。  
最小元素已固定為mn，維護一個max heap，每次取出最大元素t，以(t-mn)更新答案，並檢查此t是否能為偶數，若是則將其減半後重新押入heap，否則跳出迴圈。

例：nums = [4,1,5,20,3]  
> 乘開後 = [4,2,10,20,6]  
> 放入max heap = [20,10,6,4,2] 且最小元素確定為2，開始將最大值最小化  
> 取出20減半塞回 = [10,10,6,4,2]  
> 取出10減半塞回(重複兩次) = [6,5,5,4,2]  
> 取出6減半塞回  = [5,5,4,3,2]  
> 最大元素5不可能在減半，答案為 5-2 = 3  

```python
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        for n in nums:
            if n & 1:
                heappush(h, -2*n)
            else:
                heappush(h, -n)

        mn = -max(h)
        dev = math.inf
        while True:
            t = -heappop(h)
            dev = min(dev, t-mn)
            if t & 1:
                break
            t //= 2
            mn = min(mn, t)
            heappush(h, -t)

        return dev
```
