---
layout      : single
title       : LeetCode 3324. Find the Sequence of Strings Appeared on the Screen
tags        : LeetCode Medium Simulation
---
weekly contest 420。  
現在似乎 easy 已經不配當 Q1 了。  

## 題目

輸入字串 target。  

Alice 使用只有**兩個按鍵**的特殊鍵盤來打出 target。  

- 按鍵 1 會在現有字串追加 'a'。  
- 按鍵 2 會將**最後一個**字元改成字母表中的**下一個**字元。例如 'c' 變成 'd'，'z' 變成 'a'。

注意：最初只有空字串 ""，**只能**用按鍵 1。  

求以按鍵次數**最少**的情況下，依序回傳字串的變化過程。  

## 解法

只能末尾**追加**字元，也只能修改最後一個字元，因此必須從左到右調整出 target 的每個字元。  
模擬調整過程即可。  

每次構造當前字串需要 O(N)，在全部都是 'z' 的情況下至多構造 26N 次。  

時間複雜度 O(26 \* N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        N = len(target)
        ans = []
        a = [""] * N
        for i, c in enumerate(target):
            while a[i] != c:
                if a[i] == "":
                    a[i] = "a"
                else:
                    a[i] = chr(ord(a[i]) + 1)
                ans.append("".join(a))

        return ans
```
