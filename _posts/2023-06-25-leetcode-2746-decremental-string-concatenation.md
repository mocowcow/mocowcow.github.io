--- 
layout      : single
title       : LeetCode 2746. Decremental String Concatenation
tags        : LeetCode Medium Array String DP
---
雙周賽107。前三題都是字串系列，其中兩題可以dp，看來是精心設計過的。  

# 題目
輸入長度為n個字串陣列words。  

定義操作join(x,y)為：將兩個字串x和y合併成xy。但如果x的最後一個字元和y的第一個字元相同，則其中一個會被**刪除**。  
例如：join("ab", "ba") = "aba"；join("ab", "cde") = "abcde"。  

你必須執行n-1次操作，操作編號由1到n-1。  
令str<sub>0</sub>=words[0]，第i次操作中，你可以選擇其一：  
> 使str<sub>i</sub> = join(str<sub>i-1</sub>, words[i])  
> 使str<sub>i</sub> = join(words[i], str<sub>i-1</sub>)  

你的目標是使得str<sub>n-1</sub>的長度盡可能小。  

求str<sub>n-1</sub>的**最小**長度。  

# 解法
看錯題目，還以為是任意兩個合併，總共n-1次，原來是只能從左向右依序合併。  
反正就是依序遍歷words，每次決定words[i]要加在左邊或右邊。  

str中間長怎樣都無所謂，知道他的**開頭**和**結尾**字元是什麼就行。  
例如"aba"和"a"合併後得到"abaa"和"aaba"，對於後面的操作都是一樣的。  
我們只要看prev,head這個前提下，words[i]放前還是放後的結果比較短。  

定義dp(i,head,tail)：在字串str的首字元為head，尾字元為tail時，串接words[i,N-1]可以得到的最小長度。  
轉移方程式：dp(i,head,tail) = len(words[i]) + min(放左邊, 放右邊)。  
若head=words[i].tail，放左邊=dp(i+1,words[i].head,tail)-1；否則dp(i+1,words[i].head,tail)。  
若tail=words[i].head，放右邊=dp(i+1,head,words[i].tail)-1；否則dp(i+1,head,words[i].tail)。  
base case：當i=N，代表沒有字串要連接了，回傳0。  

注意，words[0]不受限制，可以直接擺上，遞迴的入口從i=1開始。  

i共有N種，head和tail各有26種字元，每狀態轉移2次。  
時間複雜度O(N\*26\*26)。  
空間複雜度O(N\*26\*26)。  

```python
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        N=len(words)
        first=words[0]
            
        @cache
        def dp(i,head,tail):
            if i==N:
                return 0
            w=words[i]
            return len(w)+min(
                dp(i+1,w[0],tail)-(w[-1]==head), # words[i] + str
                dp(i+1,head,w[-1])-(w[0]==tail) # str + words[i]
            )
        
        return len(first)+dp(1,first[0],first[-1])
```
