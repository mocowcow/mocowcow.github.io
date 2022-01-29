---
layout      : single
title       : LeetCode 42. Trapping Rain Water
tags 		: LeetCode Hard Stack MonotonicStack
---
順便把相似題也寫一寫放上來。

# 題目
輸入一個整數陣列heights，代表寬度1的海拔圖，計算出會有多少積水。

# 解法
這次使用Monotonic Decreasing Stack，堆疊的值必須遞減，否則pop出處理。  
如果當前高度小於堆疊頂端值，表示可以繼續積水；反之，以此為rightBound，計算左側積水量。  
計算積水時，先pop一次作為地板高，再取堆疊頂端做leftBound，width為rightBound-leftBound-1
，積水量為min(leftHeight,rightHeight)*width。  

舉個案例[3,2,1,2,3]，stack狀態如下：
1. [0]
2. [0, 1]
3. [0, 1, 2]
4. [0, 3] #積水(1-0)*1=1
5. [4] #積水(3-2)*3=3  
   
答案4

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        water = 0
        for i in range(len(height)):
            while st and height[i] >= height[st[-1]]:
                bottomHeight = height[st.pop()]
                if st:
                    leftHeight = height[st[-1]]
                    waterHeight = min(leftHeight, height[i])-bottomHeight
                    waterWidth = i-st[-1]-1
                    water += waterHeight*waterWidth
            st.append(i)

        return water
```
