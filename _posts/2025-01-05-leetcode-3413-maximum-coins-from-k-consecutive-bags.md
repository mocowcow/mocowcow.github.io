---
layout      : single
title       : LeetCode 3413. Maximum Coins From K Consecutive Bags
tags        : LeetCode Medium Sorting Greedy SlidingWindow
---
weekly contest 431。  
雖然我馬上想到原題，也想到正解，但是手賤想試試看動態開點線段樹，結果 TLE。  
還以為是 python 被卡，換 go 再交一次還是 TLE。  

## 題目

在數線上有無限多個袋子，每個座標對應一個袋子。其中某些袋子裡有硬幣。  

輸入二維整數陣列 coins，其中 coins[i] = [l <sub>i</sub>, r <sub>i</sub>, c <sub>i</sub>] 代表從 l <sub>i</sub> 到 r <sub>i</sub> 的每個袋子都有 c <sub>i</sub> 個硬幣。  

coins 中的區間保證**不重疊**。  

另外輸入整數 k。  
求連續 k 個袋子可得到的**最多**硬幣數量。  

## 解法

相似題 [2271. maximum white tiles covered by a carpet]({% post_url 2022-05-15-leetcode-2271-maximum-white-tiles-covered-by-a-carpet %})。  

當初花了不少時間理解，這題一次就過，回本了。  

---

對於原題來說，選擇的範圍左端點對齊連續袋子的左端點總是最優的。  

假設有兩個袋子區間：  
> coins = [[1,3,1], [5,5,1]], k = 4  
> 向第一個區間對齊左端點，能拿 [1,4] 的所有袋子，共 1+1+1 個硬幣。  

若將選擇的範圍右移一格，變成 [1,4]，少拿了袋子 0 的 1 個硬幣，多拿了袋子 4 的 1 個硬幣，正好不變。  
最好的情況下硬幣數只維持不變，差一點就少拿，不對齊根本沒好處。  

故**貪心**地對選擇範圍**對齊區間左端點**。  

---

但是袋子裡裝的硬幣**權重不同**。  
換個例子：  
> coins = [[1,2,1], [3,3,100]], k = 2  
> 選擇 [1,2] 只拿 1+1 個硬幣。  
> 選擇 [3,4] 只拿 100 個硬幣。  

正確答案是選 [2,3] 拿 1+100 個硬幣。  
在這種情況下，**對齊區間右端點**才是正解。  

分別處理對齊左右端點的情況，做滑動窗口即可。  

時間複雜度 O(N log N)，瓶頸在排序。  
空間複雜度 O(1)。  

```python
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        N = len(coins)
        coins.sort()

        ans = 0
        # 枚舉區間 [l, r]
        # 對齊右端點，拿 [r-k+1, r] 的袋子
        sm = 0
        j = 0
        for i, (l, r, c) in enumerate(coins):
            ll = r-k+1
            sm += (r-l+1)*c
            while j <= i and coins[j][0] < ll:  # 刪掉不完全包含的區間
                sm -= (coins[j][1]-coins[j][0]+1) * coins[j][2]
                j += 1

            extra = 0  # 部分包含的區間
            if j > 0:
                extra = max(0, (coins[j-1][1]-ll+1) * coins[j-1][2])

            ans = max(ans, sm+extra)

        # 對稱
        # 枚舉區間 [l, r]
        # 對齊左端點，拿 [l, l+k-1] 的袋子
        sm = 0
        j = N-1
        for i in reversed(range(N)):
            l, r, c = coins[i]
            rr = l+k-1
            sm += (r-l+1)*c
            while j >= i and coins[j][1] > rr:  # 刪掉不完全包含的區間
                sm -= (coins[j][1]-coins[j][0]+1)*coins[j][2]
                j -= 1

            extra = 0  # 部分包含的區間
            if j < N-1:
                extra = max(0, (rr-coins[j+1][0]+1) * coins[j+1][2])

            ans = max(ans, sm+extra)

        return ans
```

看了不少大神的寫法，共通點都是**基於對稱性**的**函數複用**。  
只需要寫對齊一邊的邏輯，封裝起來，把 coins 區間翻轉後重新跑一次就行。  

```python
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        ans = f(coins, k)
        # 對稱性
        for x in coins:
            x[0], x[1] = -x[1], -x[0]

        return max(ans, f(coins, k))


def f(coins, k):
    N = len(coins)
    coins.sort()
    ans = 0
    # 枚舉區間 [l, r]
    # 對齊右端點，拿 [r-k+1, r] 的袋子
    sm = 0
    j = 0
    for i, (l, r, c) in enumerate(coins):
        ll = r-k+1
        sm += (r-l+1)*c
        while j <= i and coins[j][0] < ll:  # 刪掉不完全包含的區間
            sm -= (coins[j][1]-coins[j][0]+1) * coins[j][2]
            j += 1

        extra = 0  # 部分包含的區間
        if j > 0:
            extra = max(0, (coins[j-1][1]-ll+1) * coins[j-1][2])

        ans = max(ans, sm+extra)

    return ans
```
