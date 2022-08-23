--- 
layout      : single
title       : LeetCode 2381. Shifting Letters II
tags        : LeetCode Medium Array String PrefixSum
---
雙周賽85。第一眼覺得是線段樹，冷靜想想線段樹不應該出現在Q3才對。  
~~其實是因為我沒有存範圍修改的線段樹模板~~。


# 題目
輸入由小寫字母組成的字串s和一個2D整數陣列shifts。其中shifts[i] = [starti, endi, directioni]，代表將starti到endi範圍內的所有字母進行修改。若directioni為1，則將字母向前移動一位；若為0，則向後移一位。

向前移指的是"a"變成"b"，而"z"變回"a"。反之，後移指的是"b"變成"a"，而"a"變回"z"。
求套用完整個shifts之後的字串。  

# 解法
有個很關鍵的點在於：題目只有求**最終結果**。意味著我們可以先算每個位置的最終移動方向，而不必逐一套用。  

這時可以使用**差分陣列**來計算區間的變化量。假設我們一開始有空的差分陣列D[0,0,0,0]，要使得閉區間[1,2]增加1，可以先使D[1]+1，而d[2+1]-1，得到D=[0,1,0,-1]。在拿來做前綴和，變成[0,1,1,0]，正好是所求的原陣列。  

照這個思路做，遍歷所有shift，若要使字母向前移，則將區間[a,b]加1；否則-1。遍歷完成後做前綴和，得到原本的變化量。  
最後遍歷字串s中的所有字元c，移動對應的步數後模26，將值調整於0\~25之間，轉回字元並加入答案中。  

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N=len(s)
        diff=[0]*(N+5)
        
        for a,b,dir in shifts:
            x=1 if dir==1 else -1
            diff[a]+=x
            diff[b+1]-=x
            
        for i in range(1,N):
            diff[i]+=diff[i-1]
            
        ans=[]
        for i,c in enumerate(s):
            x=ord(c)-97+diff[i]
            x%=26
            ans.append(chr(x+97))
        
        return ''.join(ans)
```
