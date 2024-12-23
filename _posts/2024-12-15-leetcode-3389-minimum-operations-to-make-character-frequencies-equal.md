---
layout      : single
title       : LeetCode 3389. Minimum Operations to Make Character Frequencies Equal
tags        : LeetCode Hard DP
---
weekly contest 428。  
補題發現其實沒很難，主要是前面 Q3 讓人整個心態崩潰，根本沒時間看 Q4。  

## 題目

輸入字串 s。  

若一個字串中的字元出現頻率都相等，則稱作**好的**。  

你可以執行以下操作任意次：  

- 從 s 刪除一個字母。  
- 對 s 插入一個字母。  
- 對 s 的一個字母變成字母表中下一個字母。  

注意：'z' **無法**變成 'a'。  

求使得 s 變成**好的**字串所需的**最小**操作次數。  

## 解法

字串中至多 26 個字母。先統計各字母的頻率，可對應數字 [0,25]，各頻率記做 cnt[i]。  
問題轉換成：  

> 把 cnt[0,25] 的頻率透過操作都變成目標值 t。  

若選定目標值 t，則所有 cnt 都要變成 t **或是 0**。  

---

對於某頻率 x，可以用前兩種操作變成 t 或 0：  

- x 變成 0，成本 x 次  
- x 變成 t，成本 abs(t-x) 次  

即 min(x, abs(t-x))。  

---

x 的下一個頻率記做 y。  

第三種操作會減少 x、增加 y。  
只有在 **y 小於 t** 時才有意義，否則多加的還是要扣掉，多此一舉。  

那如果三個以上連續頻率 x,y,z，使用操作三是否可行？  
> x,y,z = [3,2,1], t = 2  
> 對 x 使用操作三，變成 [2,3,1]  
> 對 y 使用操作三，變成 [2,2,2]  

實際上變化量只有 2，不如乾脆用操作一二就好。  
如果超過連續三個，用操作三根本是虧錢。  
操作三**只適兩個連續的字母**。  

---

在 y < t 的前題下，討論 x 的情況：  

- x 大於 t，變成 t 最好，成本 x-t  
- x 小於 t，變成 0 最好，成本 x  

根據 x,y,t 的值不同，有時操作完 x 還沒變成 t 或 0，需要補幾次操作二；或是 y 還沒變 t，需要補操作一。  
所以要求兩者對目標值的距離，也就是：  

- x 改 t，成本 max(t-y, x-t)  
- x 改 0，成本 max(t-y, x)  

---

對 x 做操作三會影響到下一個頻率 y，因此考慮從 0 開始考慮操作種類。  
因為找不到明顯的規律，只好往**暴力枚舉**去猜想，嘗試枚舉操作一加二，或是使用三加二的情況。  

原本問題是：  
> cnt[0,25] 變成 t 的最小操作次數。  

只用操作一或二，會變成：  
> 對 0 的操作次數 + cnt[1,25] 變成 t 的最小操作次數。  

用操作三加二，會變成：  
> 對 0, 1 的操作次數 + cnt[2,25] 變成 t 的最小操作次數。  

不同的選法會產生**重疊的子問題**，考慮 dp。  

定義 dp(i, t)：把 [0, 25] 頻率都變成 t 的最小操作次數。  
轉移：dp(i, t) = min(x 成本 + dp(i+1, t), xy 成本 + dp(i+2, t))。  
base：當 i = 26 時，修改完成，答案 0。  

---

已經知道改成 t 的最小成本，但是不知道 t 是多少。  
同樣，沒有明顯的規律，只好**暴力枚舉** t。  

各頻率最小值是 0，所以 t 下限為 0。  
而改成超過現有頻率也沒意義，所以 t 上限為 max(cnt)，最大為 N。  
其實上限直接放 N 也行，只是 py 會爆記憶體。  

dp 時間複雜度 O(N)。  
至多算 t = O(N) 次。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
"""
分類討論 目標值 t 或是 0
cnt[i] = x
cnt[i+1] = y

- 直接把 x 改成 t 或是 0
    成本 min(x, abs(t-x))
- 如果 y<t，可以用操作三，把 y 改成 t。成本至少 t-y
    操作三結束，可能 x,y 其中一個還不夠，需要補操作
    - x 改 t，成本 max(t-y, x-t)
    - x 改 0，成本 max(t-y, x)
"""
class Solution:
    def makeStringGood(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        @cache
        def dp(i, t):
            if i == 26:
                return 0

            x = cnt[i]
            # only use op1 or op2
            res = min(x, abs(t-x)) + dp(i+1, t)

            # use op3 for y
            # then use op2 for extra x
            if i < 25 and cnt[i+1] < t:
                y = cnt[i+1]
                if x > t:
                    cost = max(t-y, x-t)
                else:
                    cost = max(t-y, x)
                res = min(res, cost + dp(i+2, t))
            return res

        ans = inf
        for target in range(0, max(cnt) + 1):
            ans = min(ans, dp(0, target))

        return ans
```
