---
layout      : single
title       : LeetCode 3453. Separate Squares I
tags        : LeetCode Medium Math BinarySearch PrefixSum
---
biweekly contest 150。  
以前沒仔細研究浮點數二分，這次吃了大虧，差點沒寫出來。  

## 題目

<https://leetcode.com/problems/separate-squares-i/description/>

## 解法

所有矩形的面積和為 tot。  
分割線位於 lim，位於 lim 以下的面積為 cnt。  
需要滿足 cnt == tot - cnt。  

---

試想 lim 從 0 開始逐漸變大過程中，對 cnt 產生的影響：lim 變大，cnt 也只增不減。  
lim 越大，越能夠滿足條件。答案具有**單調性**，考慮**二分答案**。  

維護函數 ok(lim)，代表分割線 lim 是否滿足 cnt >= tot - cnt。  
下界為 y 軸最小值 0；上界為 y 軸最大值，再加上矩形邊長，為 2e9。  
找到第一個滿足的 lim 就是答案。  

---

最後是**浮點數二分**的實現細節。  

以往再找**第一個大於等於**的答案時，因為整數除法會使得中位數向下取整。  
在上下界很接近時可能會造成會造成死循環，所以更新下界需要多加 1。  

```python
while lo < hi:
    mid = (lo + hi) // 2
    if not ok(mid):
        lo = mid + 1
    else:
        hi = mid
```

但是浮點數沒有取整問題，不需要加 1。  
取而代之的給定與答案的**近似值**，在此誤差內都算正確。  

```python
eps = 1e-5
while lo + eps < hi:
    mid = (lo + hi) / 2
    if not ok(mid):
        lo = mid
    else:
        hi = mid
```

時間複雜度 O(N log (MX / eps))，其中 MX = 2e9，誤差 eps = 1e-5。  
空間複雜度 O(1)。  

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot = sum(l*l for _, _, l in squares)

        def ok(lim):
            cnt = 0
            for _, y, l in squares:
                if lim > y:
                    cnt += (min(y+l, lim) - y) * l
            return cnt >= tot - cnt

        eps = 1e-5
        lo = 0
        hi = 2e9
        while lo + eps < hi:
            mid = (lo + hi) / 2
            if not ok(mid):
                lo = mid
            else:
                hi = mid

        return lo
```

每次二分，使答案的可能區間 L = (hi - lo) 減半。需滿足：  
> L / 2^k <= 1e-5
> 移項得  
> k > log(2, L \* 1e5)  

代入本題區間 L = 2e9：  
> k > log(2, 1e15)  
> k = 48  

至多只需二分 48 次。  
以後乾脆直接 100 次算了，肯定夠。  

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot = sum(l*l for _, _, l in squares)

        def ok(lim):
            cnt = 0
            for _, y, l in squares:
                if lim > y:
                    cnt += (min(y+l, lim) - y) * l
            return cnt >= tot - cnt

        lo = 0
        hi = 2e9
        for _ in range(48):
            mid = (lo + hi) / 2
            if not ok(mid):
                lo = mid
            else:
                hi = mid

        return lo
```

想像這條分割線從下往上，面積 cnt 逐漸增加，這就是**掃描線**。  
對於矩形左下角 (x, y) 來說，當掃描線移動到 y 時，x 的和增加 l；移動到 x+l 時，x 的和減少 l。  
先把矩形轉換成**差分**，並在移動時以**前綴和**維護 x 的和，記做 x_ps。  

每次移動到高度 y，與前一個高度差為 h = y - pre_y，本次移動所新增的面積為：  
> h \* x_ps  

---

在某個高度 y，滿足 cnt 超過總面積 tot 一半時，答案高度肯定不超過 y。  
超出一半面積的部分為：  
> extra = cnt - half

以知當前 x 的和為 x_ps。  
若要減少 extra 面積，則需使高度下降 (extra / x_ps)。  
答案即 y - (extra / x_ps)。  

時間複雜度 O(N log N)，瓶頸為排序。  
空間複雜度 O(N)。  

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot = sum(l * l for _, _, l in squares)
        half = tot / 2

        # turn squares into difference array
        diff = Counter()
        for _, y, l in squares:
            diff[y] += l
            diff[y + l] -= l

        # sweep y-axis from low to high
        # and maintain prefix sum of x
        ys = sorted(diff)
        cnt = 0
        x_ps = 0
        for i, y in enumerate(ys):  
            if i > 0:  
                h = y - ys[i - 1] # height between current and previous y
                cnt += h * x_ps
                if cnt >= half: 
                    extra = cnt - half
                    return y - (extra / x_ps)

            x_ps += diff[y]

        return -1
```
