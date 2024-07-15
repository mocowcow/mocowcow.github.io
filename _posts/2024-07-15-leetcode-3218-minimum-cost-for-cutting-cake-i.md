---
layout      : single
title       : LeetCode 3218. Minimum Cost for Cutting Cake I
tags        : LeetCode Medium Array DP Greedy Sorting
---
周賽 406。

## 題目

有個 m x n 的蛋糕需要切成數塊 1 x 1 的小塊。  

輸入整數 m, n，還有兩個陣列：  

- 大小為 m - 1 的 horizontalCut，其中 horizontalCut[i] 代表在第 i 條水平線分割的成本  
- 大小為 n - 1 的 verticalCut，其中 verticalCut[j] 代表在第 j 條垂直線分割的成本  

每次操作，你可以任選一塊不為 1 x 1 大小的蛋糕，並且：  

- 在第 i 條水平線分割，成本為 horizontalCut[i]  
- 在第 j 條垂直線分割，成本為 verticalCut[j]  

每次分割操作後，蛋糕都會變成兩塊獨立的小蛋糕，且分割成本不會改變。  

求把所有蛋糕切成 1 x 1 的**最低成本**。  

## 解法

每次分割後都會變成兩塊**更小且獨立**的蛋糕，具有重疊的子問題，因此考慮 dp。  
為了知道分割成本，我們需要知道當前的小蛋糕屬於原本的哪塊位置。  

定義 dp(r1, r2, c1, c2)：當前蛋糕屬於原本的第 r1\~r2 列，以及第 c1\~c2 行。  
轉移：所有水平 / 垂直分割方式中的最小值。  

- 水平分割：  
    枚舉 [r1, r2 - 1] 之間的所有分割線 r，分成上下兩塊。  
- 垂直分割：  
    枚舉 [c1, c2 - 1] 之間的所有分割線 c，分成左右兩塊。  

base：當前 r1 = r2 且 c1 = c2 時，大小為 1 x 1。不需分割，回傳 0。  

時間複雜度 O(n^2 \* m^2 \* max(n, m))。  
空間複雜度 O(n^2 \* m^2)。  

```python
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        @cache
        def dp(r1, r2, c1, c2):
            if r1 == r2 and c1 == c2:
                return 0
            res = inf
            for r in range(r1, r2):
                res = min(res, dp(r1, r, c1, c2) + dp(r + 1, r2, c1, c2) + horizontalCut[r])
            for c in range(c1, c2):
                res = min(res, dp(r1, r2, c1, c) + dp(r1, r2, c + 1, c2) + verticalCut[c])
            return res
        
        return dp(0, m - 1, 0, n - 1)
```

然而 Q4 要求更大的測資，m, n 高達 10^5，肯定得找更好的辦法。  

找個極端情況看看：  
> m = 1, n = 100  
> 不管怎樣切，都要切 99 次  

再來看看範例：  
> m = 2, n = 2  
> 若先切直的，原本只要 1 橫刀的地方變成要 2 次了  
> 若先切橫的，原本只要 1 直刀的地方變成要 2 次了  

同樣再舉更大的例子，會發現每切一刀，會影響之後不同方向的切割點所需次數：  
> m = 3, n = 3  
> 有 h0, h1, 兩個水平切割點，還有 v0, v1 兩個垂直切割點  
>
> - 若第一刀切 h0，會使得 v0, v1 所需的切割次數從 1 變成 2  
>   若第二刀切 h1，會使得 v0, v1 所需的切割次數從 2 變成 3  
> - 若第一刀切 v0，會使得 h0, h1 所需的切割次數從 1 變成 2  
>   若第二刀切 h0 (需要兩次)，會使得 v1 所需切割次數從 1 變成 2 (不影響切過的 v0)  

發現不管怎樣切，總刀數都是 m \* n - 1。  
而且**越晚切**的切割點 vi 來說，如果先前切過的**不同方向**的刀數 hi 越多，則 vi 的所需次數會變得更多。  

---

根據**越晚切越貴**這點，先從成本最貴的切割點開始切就對了。  
將所有切割點依照成本遞減排序，並維護兩方向的所需次數 cnt，每次切割後就給不同方向的次數加 1。  

時間複雜度 O(m log m + n log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        a = []
        for x in horizontalCut:
            a.append([x, 0])
        for x in verticalCut:
            a.append([x, 1])
        a.sort(key=itemgetter(0), reverse=True)

        cnt = [1, 1]
        ans = 0
        for cost, dir in a:
            ans += cost * cnt[dir]
            cnt[dir ^ 1] += 1

        return ans
```
