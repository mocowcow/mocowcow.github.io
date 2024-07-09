---
layout      : single
title       : LeetCode 3208. Alternating Groups II
tags        : LeetCode Medium Array DP
---
雙周賽 134。

## 題目

有個由紅藍瓷磚組成的圓環。  
輸入整數陣列 colors，還有整數 k。其中 colors[i] 代表第 i 個磁磚的顏色：  

- colors[i] == 0 代表磁磚 i 是紅色  
- colors[i] == 1 代表磁磚 i 是藍色  

每 k 個連續且**顏色交替**的磁磚稱作**交替組**。  

求有多少個**交替組**。  

注意：由於是環狀，最後一個磁磚和第一個磁磚被視為相鄰的。  

## 解法

**交替組**從 3 次交替變成 k 次，暴力作法肯定不行。  

注意到交替是連續的，且依賴於前一個位置的交替次數。  
以 i 結尾時，往左數交替了 x 次，則以 i - 1 為右邊界肯定交替了 x - 1 次。  
存在規模更小的子問題，因此考慮 dp。  

定義 dp(i)：以 i 結尾時的最大連續交替次數。  
轉移：  

- 若 colors[i] != colors[i - 1]：  
    dp[i] = dp[i - 1] + 2
- 若 colors[i] == colors[i - 1]：  
    dp[i] = 1  

---

colors 是環形結構、首尾相連。  
這樣算的話，小於 k - 1 轉移來源處於尚未計算的狀態，前半段會是錯的。  
因此需要重新再算一次，方可得到正確結果。  

最後統計有幾個 dp(i) 的值大於等於 k 即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

---

在首尾連接處呈現交替時，前 k 個 dp(i) 的值可能會比預期的大，例如：  
> colors = [0,1,0,1]  
> 第一次計算後 dp = [1,2,3,4]  
> 第二次計算後 dp = [5,6,7,8]  

根據題意，k 至多和 N 相等，因此只會有 k = 4 的交替組，dp 結果明顯不太對。  
但不影響本題作答，我們只需確保至少交替 k 次即可。  

```python
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        dp = [0] * N
        for _ in range(2):
            for i in range(N):
                if colors[i] != colors[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = 1

        return sum(x >= k for x in dp)
```

發現 dp(i) 只會參考到 dp(i - 1)，因此可以空間優化，但必須改在轉移的過程中統計答案。  
為確保得到的 dp 值正確、且**不重複計入答案**，因此只有在第二次循環的時候統計答案。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        ans = 0
        cnt = 0
        for rep in range(2):
            for i in range(N):
                if colors[i] != colors[i - 1]:
                    cnt += 1
                else:
                    cnt = 1

                if rep == 1 and cnt >= k:
                    ans += 1

        return ans
```
