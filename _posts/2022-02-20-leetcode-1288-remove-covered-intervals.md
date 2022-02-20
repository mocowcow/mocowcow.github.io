---
layout      : single
title       : LeetCode 1288. Remove Covered Intervals
tags 		: LeetCode Medium Sorting
---
每日題。比較不那麼難處理的區間問題。

# 題目
輸入陣列intervals，裡面包含多個區間[l,r]，若某區間被其他區間覆蓋則將之刪除，求最後剩下幾個區間。  
定義(a,b)被(c,d)覆蓋若且唯若c<=a且b<=d。如[3,6]被[2,8]覆蓋。

# 解法
將intervals先以左邊界遞增排序，再以右邊界遞減排序，可以保證每一個區間左邊界都小於先前出現過的區間，且右邊界都小於**左邊界相同但尚未出現的區間**。  
題目要求的是沒被去除的區間數，也就是沒被覆蓋的區間。維護一個right變數代表碰過最遠的右邊界，開始遍歷排序過的區間。若某右邊界超過right，代表他沒被覆蓋，ans+1，並更新right值。  

![示意圖](/assets/img/2022-02-20-leetcode-1288-remove-covered-intervals-1.jpg)  
圖中只有綠色、藍色兩區間未被其他覆蓋，答案為2。

```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = right = 0
        print(intervals)
        for _, r in intervals:
            if r > right:
                ans += 1
                right = r

        return ans

```
