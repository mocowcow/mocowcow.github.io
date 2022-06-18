--- 
layout      : single
title       : LeetCode 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
tags        : LeetCode Hard Array Matrix Heap
---
隨便抽的題，一開始看到矩陣裡面每列都有序，就想到二分搜。但想不出怎麼搜，看了提示竟然要我用heap。

# 題目
輸入一個m*n的矩陣mat，還有一個整數k。  
mat的每一列都是**有序遞增**的。  

你可以從每一列中選擇一個數字來組成陣列，求所有可能陣列中第k小的陣列總和。  

# 解法
看一下測資，m和n最大40，要暴力列舉所有組合的話會是40^40，就這樣塞進heap肯定不對。  

試著用下例來思考：  
> mat = [[1,3,11],[2,4,6]], k = 2  

因為每一列都必須選擇一個數字，但我們只需要所有組合中最小的2個，至少能確定第一列不會使用到11。接下來再以[1,3]和[2,4,6]求所有相加組合，得到[3,5,7,5,7,9]，一樣只取最多最多2個，剩下[3,5]，那第二小的答案就是5了。 

若有多個列，照著此方式遍歷每列，最多只保留k個候選元素，這樣可以減少非常多的無用計算。這似乎也算是一種剪枝？

```python
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        a=[0]
        for row in mat:
            prod=[x+y for x in a for y in row]
            a=nsmallest(k,prod)

        return a[-1]
```

使用list排序後，彈出超過k的候選元素。

```python
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        a=[0]
        for row in mat:
            prod=[x+y for x in a for y in row]
            prod.sort()
            while len(prod)>k:
                prod.pop()
            a=prod
    
        return a[-1]
```
                
