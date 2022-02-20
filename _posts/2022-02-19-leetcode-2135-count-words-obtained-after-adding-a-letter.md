---
layout      : single
title       : LeetCode 2135. Count Words Obtained After Adding a Letter
tags 		: LeetCode Medium String HashTable BitManipulation Sorting
---
模擬周賽275。bit mask爸爸又來了。

# 題目
輸入兩個字串陣列startWords及targetWords，求共有多少targetWord有多少可以從startWords中轉換而來。  
轉換包含以下兩種步驟：  
1. 對字串加入本身未出現過的字元到尾端，例如abc可以在最後方加入d,e或y，但不可加入a或b。  
2. 把上一步得到的新字串以任意順序重新排列，也可以不排列。  

# 解法
題目只有說轉換不可能加入重複的字元，但沒說startWords中本身會不會有aab這種字串，只好直接自訂測資試試看。試完才看到最下方的Constraints最後一行寫：  
> No letter occurs more than once in any string of startWords or targetWords.  

好吧真的做白工了，細節藏在魔鬼裡，學習到寶貴的一課。既然每個字元只會出現一次，那麼我們可以使用bit mask表示各字元。  
1<<0表示a，1<<1表示b，以此類推。  
定義一個toBit函數，把字串轉換成整數表示的bit mask。  
把所有targetWords轉換成整數後裝入雜湊表，然後遍歷startWords，對每個字串試著加入所有未出現過的字元，若新字串在雜湊表中則ans加1。  
結果吃了個WA。因為targetWords中會出現重複的字串。  
例：  
> startWords = ["act"], targetWords = ["acti","acti"]  
> 答案應為2  

只好改變方向，把startWords裝入set變數sw中，遍歷targetWords，試著刪除每個已出現個字元，若新字串在sw中則ans+1。

```python
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        def toBit(s):
            n = 0
            for c in s:
                n |= 1 << (ord(c)-97)
            return n

        # build startWords
        sw = set()
        for s in startWords:
            sw.add(toBit(s))

        ans = 0
        # iter targetWords
        for s in targetWords:
            n = toBit(s)
            for i in range(26):
                if n & (1 << i):
                    conversion = n-(1 << i)
                    if conversion in sw:
                        ans += 1
                        break

        return ans

```

後來發現官方標籤有個sorting，原來也可以透過這方法解，而且還容易閱讀，執行又更有效率。  
維護一個set變數sw，把所有startWords排序後放入。然後遍歷targetWords，排序後，試刪除其中一個字元，看是否在sw中，若是則ans+1。

```python
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sw = set([''.join(sorted(x)) for x in startWords])
        ans = 0
        for w in targetWords:
            w = ''.join(sorted(w))
            for i in range(len(w)):
                if w[:i]+w[i+1:] in sw:
                    ans += 1
                    break

        return ans

```