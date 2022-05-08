--- 
layout      : single
title       : LeetCode 2266. Count Number of Texts
tags        : LeetCode Medium String DP
---
周賽292。我最愛的DP，打數字[7,9]的時候手滑變成[4,9]，吃了一個WA。

# 題目
![圖例](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png){:height="200" width="200px"}  
如圖，字母a需要按2號鍵1次，字母b需要按2號鍵2次，以此類推。  

Alice傳訊息給Bob，由於傳輸錯誤，所有的字母都變成了數字。  
- Alice原本傳送'bob'，但Bob只收到數字字串'2266622'  

輸入字串pressedKeys，代表Bob收到的字串，求此字串總共有幾種解碼的可能性。答案很大，模10^9+7後回傳。

# 解法
求解碼方式幾種，一看就是dp，而且只有在數字連續出現時才會有不同的解碼方式。  

先看看每個數字對應到多少字母：  
- 7, 9對應4種字母  
- 其餘都對應3種字母  

代表7和9最多可以連續出現4次，其他的最多連續出現3次。所以每個數字可以往前追溯2個位置，若是7或9，可以再往前一個位置。  
原本想用bottom up，但是處理base case超級麻煩，姑且改成top down，晚點找時間再補。  

定義dp(i)：到pressedKeys[i]為止的解碼方式有幾種。  
轉移方程式：dp(i)=dp(i-1)，若key[i-1]==key[i]則加上dp(i-2)，又若key[i-2]==key[i]則再加dp(i-3)，又又又key[i]是[7,9]且key[i-3]還是相同，最後在加dp(i-4)  

base cases：i=0時只有一個數字，只有一種解碼方式；i<0時沒有數字，也只有空字串一種解碼方式。  

```python
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        N = len(pressedKeys)
        MOD = 10**9+7

        @lru_cache(None)
        def dp(i):
            if i <= 0:
                return 1
            ans = dp(i-1)
            if i > 0 and pressedKeys[i] == pressedKeys[i-1]:
                ans += dp(i-2) # 2個連續數解碼成1個字母
                if i > 1 and pressedKeys[i] == pressedKeys[i-2]:
                    ans += dp(i-3) # 3個連續數解碼成1個字母
                    if i > 2 and pressedKeys[i] in '79' and pressedKeys[i] == pressedKeys[i-3]:
                        ans += dp(i-4) # 4個連續數解碼成1個字母
            return ans % MOD

        return dp(N-1)
```
