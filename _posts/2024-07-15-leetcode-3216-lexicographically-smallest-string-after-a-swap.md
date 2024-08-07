---
layout      : single
title       : LeetCode 3216. Lexicographically Smallest String After a Swap
tags        : LeetCode Easy Array String Simulation Greedy
---
周賽 406。

## 題目

輸入數字字串 s。你可以交換其中兩個**相鄰**且**奇偶性相同的**字元，**最多一次**。  
求可得到字典序最小的字串。  

## 解法

最暴力的做法，枚舉所有相鄰的數對，若奇偶性相同則生成交換後的字串 t，並與答案取最小值。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        N = len(s)
        a = list(s)
        ans = s
        for i in range(N - 1):
            if ord(a[i]) % 2 == ord(a[i + 1]) % 2:
                a[i], a[i + 1] = a[i + 1], a[i]
                # new string
                t = "".join(a)
                ans = min(ans, t)
                a[i], a[i + 1] = a[i + 1], a[i]

        return ans
```

仔細想想，字串比對是由左至右，就算多個相鄰數對奇偶性相同，第一個能使得字典序變小的肯定是最佳答案。  

舉個簡單例子：  
> s = "531"  
> 交換 "53"，得到 "351"  
> 交換 "31"，得到 "513"  

很明顯交換 "53" 更好。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        N = len(s)
        a = list(s)
        for i in range(N - 1):
            if ord(a[i]) % 2 == ord(a[i + 1]) % 2 and a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                return "".join(a)

        return s
```
