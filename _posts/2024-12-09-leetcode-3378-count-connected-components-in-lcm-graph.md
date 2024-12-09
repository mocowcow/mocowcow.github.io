---
layout      : single
title       : LeetCode 3378. Count Connected Components in LCM Graph
tags        : LeetCode Hard Math Graph UnionFind
---
biweekly contest 145。

## 題目

輸入長度 n 的整數陣列 nums，還有正整數 threshold。  

有個 n 節點的圖，第 i 個節點的值為 nums[i]。  
若兩個節點對應的值滿足 lcm(nums[i], nums[j]) <= threshold，則兩節點之間存在一條邊。  

求此圖中有多少個**連通塊**。  

**連通塊**指的是圖中的一個子圖，子圖中任意兩節點都存在路徑相連，且子圖中的節點不與外部任何節點有連邊。  

## 解法

題目都說連通塊了，十有八九就是**併查集**。  

最原始作法是枚舉兩個點 x, y，檢查 lcm 後連邊。  
但是 N 高達 10^5，光是枚舉就需要 10^10，肯定超時。  

---

很多大神都說，這種關於 gcd (或 lcm) 的題，很多都可以透過枚舉 gcd (或 lcm) 來解決。  

設 t = lcm(x, y) = x \* y / gcd(x, y)。  

lcm 全名**最小公倍數**，顧名思義，t 肯定是 x 和 y 的倍數。  
如果把 x 和 y 都和 t 連接，可以保證 x, y, t 三個節點都屬相同連通塊。  
根據以上規則，可以枚舉所有可能的 lcm = t，然後再枚舉 t 的所有因數 x，將 x, t 連邊。  

例如：  
> nums = [2,3], threshold = 10  
> t = 1..
> t = 6 對應因數 x = 2,3 各自連邊  
> 2 和 3 會透過 6 連通  
> 共一個連通塊  

但是 t 高達 threshold = 10^5，其因子至多 sqrq(10^5)，似乎還是有點多。  

---

改成枚舉 nums 中的元素 x 作為因子，然後再枚舉 x 的倍數 t，將 x, t 連邊，可以達到同樣效果。  

例如：  
> nums = [2,3], threshold = 10  
> x = 2 對應倍數 t = 4,6,8,10 各自連邊  
> x = 3 對應倍數 t = 6,9 各自連邊  
> 2 和 3 會透過 6 連通  
> 共一個連通塊  

---

枚舉完倍數連邊後，再次統計 nums 中節點所屬的連通塊，並以集合**去重**。  
若超過 x 超過 threshold，則肯定是獨立的，不處理。  

題目保證 nums 不重複，所以最差情況下 nums = [1..T]。  
枚舉 t 倍數部分的時間複雜度是調和級數 O(T log T)。  

時間複雜度 O(N + T log T)，其中 T = threshold。  
空間複雜度 O(N + T)。  

```python
class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        uf = UnionFind(threshold+5)
        ans = set()

        for x in nums: # enumerate multiple of x
            for t in range(x+x, threshold+1, x): # t = 2x, 3x, 4x..
                uf.union(x, t)

        for x in nums:
            if x <= threshold:
                ans.add(uf.find(x))
            else:
                ans.add(x)

        return len(ans)


class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
