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

後來才想通其實用樹狀陣列也可以做這題，而且就算要在任意次修改間查詢某索引的字元也沒問題。  
樹狀陣列的query查的就是前i項元素的前綴和，所以在進行區間修改時，一樣也是做差分的修改。  
再次強調：差分的前綴和=原陣列。  

總共需要N次區間修改，每次複雜度O(log N)，之後的N次區間查詢也是O(log N)，整體複雜度O(N log N)。

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.bit = [0]*(n+1)
        self.N = len(self.bit)

    def update(self, index, val):
        index += 1
        while index < self.N:
            self.bit[index] += val
            index = index + (index & -index)

    def prefixSum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index = index - (index & -index)
        return res

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N=len(s)
        BIT=BinaryIndexedTree(N+5)
        ans=[0]*N
        
        for a,b,dir in shifts:
            x=1 if dir==1 else -1
            BIT.update(a,x)
            BIT.update(b+1,-x)
            
        for i,c in enumerate(s):
            offset=BIT.prefixSum(i)
            x=ord(c)-97+offset
            x%=26
            ans[i]=chr(x+97)
            
        return ''.join(ans)
```