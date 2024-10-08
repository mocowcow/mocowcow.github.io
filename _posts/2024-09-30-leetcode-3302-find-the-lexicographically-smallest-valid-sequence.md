---
layout      : single
title       : LeetCode 3302. Find the Lexicographically Smallest Valid Sequence
tags        : LeetCode Medium String Greedy PrefixSum
---
biweekly contest 140。  

## 題目

輸入兩個字串 word1 和 word2  

若一個字串 x 在修改**至多一個**字元後等同於字串 y，則稱 x 和 y **幾乎相等**。  

若一個索引序列 seq 滿足以下條件，則稱為**合法**：  

- 索引是遞增排序。  
- 將 word1 中這些索引對應的字元**依序**串接起來，可得到一個與 word2 **幾乎相等**的字串。  

回傳長度為 word2.length 的陣列，代表一個**字典序最小**的**合法**索引序列。若不存在則回傳空陣列。  

注意：答案是回傳索引序列，而不是其對應的字串。  

## 解法

若不能修改字元，就是經典的雙指針。  
相似題 [392. is subsequence]({% post_url 2022-03-02-leetcode-392-is-subsequence %})。  

---

在修改 word1[i] 為 c 後若**合法**，則有 pre + c + suf =  word2。  
其中 pre 是 word1[..i-1] 的子序列，且 suf 是 word1[i+1..] 的子序列。  

我們可以分別從兩個方向匹配 word2，並以 pre[i] 代表 word1[..i] 匹配到的前綴長度、suf[i] 代表 word1[i..] 匹配到的後綴長度。  
最後枚舉分割點 i，只要 pre[i] + suf[i+1] 至少有 N-1，便可以透過一次修改滿足合法序列。  

---

難點在於題目要求的是**最小索引序列**，而不只是問答案是否存在。  

為了使字典序盡可能小，應當從左向右匹配，且字元相同則應當立即選用該索引。  
那如果不同呢？有兩種選擇：**不選**或是**修改**。  

有可能修改了當前字元，而使得後續真正需要修改的字元無法修改而失敗。例如：  
> word1 = "aabd", word2 = "abc"  
> 已匹配 "a"，但 word1[1] != word2[1]，而把 word1[1] 改成 "b"  
> 結果最長只匹配到 "ab"  
> 正確方式應該是把 word1[3] 改成 "c"  
> 合法序列 [0,1,3]  

也可能原本不需要修改就有合法序列，但修改後能夠得到更小的字典序。例如：  
> word1 = "abbd", word2 = "abd"  
> 原有合法序列 [0,1,3]  
> 若把 word1[2] 改成 d，使 word1 = "abdd"  
> 得到更小的合法序列 [0,1,2]  

---

講這麼多，到底什麼時候要改？  

若有多個索引在修改後都合法，那麼應該貪心地選擇最小的索引，因為會使得字典序更小。  
因此只要 word1[i] 修改後，後方剩於的字串還能夠匹配整個 word2，那就必須改。  

回想剛才提過的 suf[i]，他表示 word1[i..] 匹配的後綴長度。  
在 word1[i] != word2[j] 時，已經成功匹配的前綴長度為 j，而剩餘的部分 word1[i+1..] 則是 suf[i+1]。  
我們可以修改 word1[i] = word2[j]，修改後的總長度為 pre[i] suf[i+1] + 1，只要滿足 N 則代表合法。  

匹配過程，只要湊滿 N 個索引立即回傳答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        M, N = len(word1), len(word2)

        suf = [0] * (M + 1)
        j = N-1
        for i in reversed(range(M)):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = N-1-j

        ans = []
        j = 0
        changed = False
        for i in range(M):
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and j + suf[i+1] + 1 >= N:
                changed = True
                ans.append(i)
                j += 1

            if j == N:
                return ans

        return ""
```
