--- 
layout      : single
title       : LeetCode 2380. Time Needed to Rearrange a Binary String
tags        : LeetCode Medium String Simulation
---
雙周賽85。剛做完Q1感覺這次有難度，Q2果然也有點意思。

# 題目
輸入二進位字串s。在一秒鐘內，可以把字串中所有的"01"同時替換為"10"。重複此動作，直到不存在"01"為止。  
求總共需要多少秒才能達成要求。  

# 解法
當我們把01換成10時，若左邊還有0的話，下一秒勢必要繼續替換。最差的狀況如00001，那麼我們必須替換4次才能把1趕到最左方。  
字串長度最多1000，使用暴力法模擬上述過程的話複雜度是O(N^2)，還算可以接受。  

因為字串不好修改，所以先換成整數陣列。設立變數ok表示是否需要繼續替換，每次檢查兩個索引，若剛好形成01的話則替換成10。

```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        N=len(s)
        s=[int(c) for c in s]
        ans=0
        
        while True:
            ok=True
            i=0
            while i+1<N:
                if s[i]==0 and s[i+1]==1:
                    s[i]=1
                    s[i+1]=0
                    ok=False
                    i+=2
                else:
                    i+=1
            if ok:break
            ans+=1

        return ans
```
