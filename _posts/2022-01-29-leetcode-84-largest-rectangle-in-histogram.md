---
layout      : single
title       : LeetCode 84. Largest Rectangle in Histogram
tags 		: LeetCode Hard Stack MonotonicStack
---
當初就是在這題認識到stack的強大，歷久不衰的經典。

# 題目
輸入一個整數陣列heights，代表1*heights[i]的長方形，求出最大的矩形面積。

# 解法
忘記以前用什麼方法解，結果被超大寬度低高度的測資卡死。  
這題使用特殊資料結構Monotonic Increasing Stack，堆疊的值必須遞增，否則pop出處理。  
基於上述特性，我們先在heights陣列末端加入一個[0]，確保所有輸入都會被計算。  
簡單來說，當前的值若比堆疊頂端還大，代表能夠延續底部的矩形面積，可以先放著不管；反之，假設i=3高度5，堆疊頂端=2高度7，那高度為7的矩形右邊界只能到2為止。
每次計算矩形面積時，pop一個值設為高度h，再pop一個值當作左邊界(空stack則左邊界為0)，面積為(i-left-1)*h，並更新答案。

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        heights.append(0)
        area = 0
        for i in range(len(heights)):
            while st and heights[i] <= heights[st[-1]]:
                h = heights[st.pop()]
                w = i if not st else i-st[-1]-1
                area = max(area, h*w)
            st.append(i)

        return area

```
