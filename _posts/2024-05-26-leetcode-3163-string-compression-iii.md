---
layout      : single
title       : LeetCode 3163. String Compression III
tags        : LeetCode Medium Array String Simulation
---
周賽 399。

## 題目

輸入字串 word，按照以下規則將字串壓縮：  

- 最初有個空字串 comp。重複以下操作直到 word 為空：  
  - 移除 word 由相同字元 c 構成的前綴。長度上限為 9。  
  - 將前綴長度和字元 c 加到 comp。  

回傳字串 comp。  

## 解法

分組循環秒殺題。  
枚舉左端點 i，維護當前長度 cnt 並嘗試向右擴展右端點。停止擴展後將壓縮後的結果加入答案。  

時間複雜度 O(N)。  
空間複雜度 O(1)，輸出空間不計入。  

```python
class Solution:
    def compressedString(self, word: str) -> str:
        N = len(word)
        ans = []
        i = 0
        while i < N:
            c = word[i]
            cnt = 1
            j = i
            while j + 1 < N and word[j + 1] == c and cnt < 9:
                j += 1
                cnt += 1
                
            # compress
            ans.append(str(cnt) + c)
            i = j + 1
        
        return "".join(ans)
```
