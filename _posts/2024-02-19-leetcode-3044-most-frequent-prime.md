---
layout      : single
title       : LeetCode 3044. Most Frequent Prime
tags        : LeetCode Medium Array Matrix HashTable
---
周賽385。

## 題目

輸入 m\*n 的二維矩陣 mat。  
對於每個格子，你可以按照以下方式生成數字：  

- 總共有八種移動方向  
- 選擇一種方向作為路徑，並在移動的過程中把遇到的數字加到當前數字的最後方  
- 每一步都會生成數字。例如路徑是 [1, 9, 1]，則會生成 [1, 19, 191] 三個數字  

求生成的數字中，大於10、且為**質數**，並出現**最多次**的數字為何。  
若不存在滿足的答案，則回傳 -1。若有多個答案出現次數相同，則回傳最大者。  

注意：移動過程中不可改變方向。  

## 解法

沒什麼特別的技巧，就是囉嗦的模擬題。  
因為套了好幾層迴圈，注意排版還有變數命名，不同的邏輯區塊可以用空行或是註解分隔，比較不容易爆炸。  

生成數字時不可改變方向，數字的位數受限於**長度**和**寬度**的最小值，記做 k = min(m, n)，最多為 6 位數。  
數字範圍 10^mn 在 10^6 以內，也不算太大，預處理篩出質數或是單個判斷都沒有問題。  

有 mn 個格子作為出發點，最多移動 k 次，共生成 mnk 個數。  
本題採用個別判斷，每次判斷的複雜度 O(sqrt(10^mn))，平方根相當於指數減半，減化成 O(10^(1/2))。  

時間複雜度 O(mnk \* 10^(1/2) )。  
空間複雜度 O(mnk)。  

```python
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        d = Counter()
        
        for r in range(M):
            for c in range(N):
                # 8 dir
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        # build num
                        rr, cc = r, c
                        val = 0
                        while 0 <= rr < M and 0 <= cc < N:
                            val = val*10 + mat[rr][cc]
                            # check num > 10 and prime
                            if val > 10 and is_prime(val):
                                d[val] += 1
                            # move
                            rr, cc = rr + dx, cc + dy
                            
        # find ans
        ans = -1
        cnt = 0
        for k, v in d.items():
            if v > cnt or (v == cnt and k > ans):
                cnt = v
                ans = k
                
        return ans
        
        
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```
