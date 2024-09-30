---
layout      : single
title       : LeetCode 3305. Count of Substrings Containing Every Vowel and K Consonants I
tags        : LeetCode Medium SlidingWindow TwoPointers HashTable Math
---
weekly contest 417。  

## 題目

輸入字串 word 和非負整數 k。  

求有多少**子字串**滿足每個母音出現**至少**一次，且有**正好** k 個子音。  

## 解法

看到**子字串**就會想到**滑動窗口**。  

上週的滑窗問題 [3297. count substrings that can be rearranged to contain a string i]({% post_url 2024-09-22-leetcode-3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i %})。  
該題是求**至少**滿足某些條件。枚舉右端點 right，並在條件滿足時收縮左端點 left。  
因為只有在**滿足時才收縮 left**，因此 left-1 肯定是合法的。故 [0, left-1] 都是合法的左端點。  

但本題還有**正好** k 個子音的限制，雖然能確定 left-1 合法，但卻不知道 left-2 是母音還是子音，不適用此方法。  

---

在 Q2 時至多 k = 250，稍微暴力點的方法還是可行的。  
先枚舉可能的子字串長度，再透過滑窗檢查子字串是否合法。  

時間複雜度 O(N^2)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        vowel = set("aeiou")
        ans = 0
        # enumerate possible size
        for sz in range(5, N+1):
            d = Counter("aeiou")
            v_need = 5
            c_need = k
            left = 0
            for right, c in enumerate(word):
                # expand right
                if c in vowel:
                    if d[c] == 1:
                        v_need -=1
                    d[c] -= 1
                else:
                    c_need -= 1

                if right - left + 1 == sz:
                    # valid substring
                    if v_need == 0 and c_need == 0:
                        ans += 1
                    # shrink left
                    t = word[left]
                    if t in vowel:
                        if d[t] == 0:
                            v_need += 1
                        d[t] += 1
                    else:
                        c_need += 1
                    left += 1

        return ans
```

對於 Q4 的 k = 2e5 就得想想其他優化方法。  

相似題 [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)。  

雖然沒辦法輕鬆找到**正好 k 個**，但是找**至少 k 個**卻很簡單。  
若找至少 k 個，同時會包含 k+1, k+2,.. 的答案。  
根據排容原理，**至少 k 個**扣掉**至少 k+1 個**，等於**正好 k 個**。  

設 f(k) 為至少 k 個子音的合法子陣列個數。  
只需要兩次滑動窗口，分別求 f(k) 和 f(k+1) 即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return f(word, k) - f(word, k+1)

# at least k consonants
vowel = set("aeiou")
def f(word, k) -> int:
    N = len(word)
    res = 0
    d = Counter("aeiou")
    v_need = 5
    c_need = k
    left = 0
    for right, c in enumerate(word):
        # expand right
        if c in vowel:
            if d[c] == 1:
                v_need -=1
            d[c] -= 1
        else:
            c_need -= 1

        while v_need == 0 and c_need <= 0:
            t = word[left]
            if t in vowel:
                if d[t] == 0:
                    v_need += 1
                d[t] += 1
            else:
                c_need += 1
            left += 1
        res += left
    return res
```
