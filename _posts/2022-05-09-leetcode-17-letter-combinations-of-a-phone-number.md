--- 
layout      : single
title       : LeetCode 17. Letter Combinations of a Phone Number
tags        : LeetCode Medium HashTable String Backtracking DP
---
每日題。我就覺得昨天周賽的電話圖片很眼熟，結果今天每日題就出現，這選題者一定是故意的。

# 題目
輸入一個只包含數字2~9的字串digits，回傳有所有可能的字母組合，以任何順序都可以。  
下圖給出了數字所對應的字母：  
![圖例](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png){:height="200" width="200px"}  

# 解法
先建立雜湊表，紀錄每個數字有可能對應到的字母。  
使用回溯法，暴力搜索出每種可能性，加到答案裡面。

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        N=len(digits)
        d = {'2': 'abc',
             '3': 'def',
             '4': 'ghi', 
             '5': 'jkl', 
             '6': 'mno',
             '7': 'pqrs', 
             '8': 'tuv', 
             '9': 'wxyz'
             }
        
        def bt(i,curr):
            if i==N:
                if curr:
                    ans.append(''.join(curr))
            else:
                for c in d[digits[i]]:
                    curr.append(c)
                    bt(i+1,curr)
                    curr.pop()

        bt(0,[])
        
        return ans
```

另外一種寫法，從空字串開始，遍歷所有digits並生成新的字串。  
雖然是重複利用到上次運算的結果，但又感覺不太算是DP；如果裝在佇列裡面似乎又可以看成是BFS？糾結名詞真麻煩。

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dp=['']
        d = {'2': 'abc',
             '3': 'def',
             '4': 'ghi', 
             '5': 'jkl', 
             '6': 'mno',
             '7': 'pqrs', 
             '8': 'tuv', 
             '9': 'wxyz'
             }
        
        for n in digits:
            dp=[x+c for c in d[n] for x in dp]
            
        return dp
```