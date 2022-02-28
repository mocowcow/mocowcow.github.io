---
layout      : single
title       : LeetCode 1491. Average Salary Excluding the Minimum and Maximum Salary
tags 		: LeetCode Easy Array Sorting
---
Study Plan - Programming Skills Day 1 Basic Data Type。  
這系列大概是想考一些直覺使用的小技巧吧。

# 題目
輸入整數陣列salary，計算扣除最高和最低薪兩人後的平均薪資為多少。  
salary中的整數皆不重複，且3<=salary長度<=10^6。

# 解法
既然都說了不重複，長度又至少3，出題者大概想要排序後去頭去尾後算平均吧。

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        sa = sorted(salary)[1:-1]
        return sum(sa)/len(sa)
```

其實O(N)的解法更好，加總salary時順便找最大最小，最後扣除再平均。只不過python內建函數太強了，上面程式碼反而比較快。

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        mn = math.inf
        mx = -math.inf
        s = 0
        for n in salary:
            s += n
            mn = min(mn, n)
            mx = max(mx, n)

        return (s-mn-mx)/(len(salary)-2)

```
