--- 
layout      : single
title       : LeetCode 149. Max Points on a Line
tags        : LeetCode Hard HashTable Math Geometry
---
和上次周賽[2280. minimum lines to represent a line chart]({% post_url 2022-05-22-leetcode-2280-minimum-lines-to-represent-a-line-chart %})有點像，真想知道我以前怎麼知道要用斜率。

# 題目
輸入points陣列，其中points[i] = [xi, yi]，代表X-Y平面上的一個點，回傳同一條直線上最多有幾個點。

# 解法
列舉點i和所有和點j形成的直線，並以分數記錄其斜率，約分後加入雜湊表計數。遍歷所有不同斜率的線，線的數量+1就是線上的點。  

需要注意的是，內建的gcd函數只會回傳正整數，若碰到分數(-5/10)和(5/-10)做約分時，會變成(-1/2)和(1/-2)，被當作不同的斜率，所以要先將points排序，確保點i和點j的相對位置。

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def fraction(a,b):
            _gcd=gcd(a,b)
            return (a//_gcd,b//_gcd)
        
        N=len(points)
        points.sort()
        ans=1
        for i in range(N-1):
            d=defaultdict(int)
            for j in range(i+1,N):
                dx=points[j][0]-points[i][0]
                dy=points[j][1]-points[i][1]
                d[fraction(dy,dx)]+=1
            ans=max(ans,max(d.values())+1)
                
        return ans
```

如果不想排序，也可以自己寫個會出現負數的gcd。  
> 分數(-5/10)約分，gcd(-5,10)=-5，約分完變成(1/-2)  
> 分數(5/-10)約分，gcd(5,-10)=5，約分完變成(1/-2)  

這樣約分結果就相同了。

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def fraction(a,b):
            _gcd=mygcd(a,b)
            return (a//_gcd,b//_gcd)

        def mygcd(a, b):
            if b == 0:
                return a
            return mygcd(b, a % b)
        
        N=len(points)
        ans=1
        for i in range(N-1):
            d=defaultdict(int)
            for j in range(i+1,N):
                dx=points[j][0]-points[i][0]
                dy=points[j][1]-points[i][1]
                d[fraction(dy,dx)]+=1
            ans=max(ans,max(d.values())+1)
                
        return ans
```