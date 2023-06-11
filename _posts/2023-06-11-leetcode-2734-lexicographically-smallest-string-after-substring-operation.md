--- 
layout      : single
title       : LeetCode 2734. Lexicographically Smallest String After Substring Operation
tags        : LeetCode Medium Array String Greedy HashTable
---
周賽349。這題應該算是很機車的陷阱題，可能我對這種類型中計多次，已經免疫了。  

# 題目
輸入由小寫字母組成的字串s。每次操作你可以：  
 - 選擇任意一個非空的子字串s，並將子字串中每個字元換成前一個字母。例如'b'換成'a'，而'a'換成'z'  

 求**正好一次**操作後，可以得到的**最小字典順序**的結果。  

# 解法
字典序是從左往右比較，所以優先修改靠左的字元一定更好。  
a修改後會變成z，反而增大字典順序，所以只要修改最靠左一段由z以外字元組成的區間。  

但如果整個字串都是a，題目又要求**正好一次**操作，一定會使得字典序比原本更大，所以只把最後一個a變成z，盡可能降低字典序的增加量。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def smallestString(self, s: str) -> str:
        N=len(s)
        s=list(s)
        
        if len(set(s))==1 and s[0]=="a":
            s[-1]="z"
            return "".join(s)
        
        i=0
        while s[i]=="a":
            i+=1
            
        j=i
        while j+1<N and s[j+1]!="a":
            j+=1
                
        for k in range(i,j+1):
            s[k]=chr(ord(s[k])-1)

        return "".join(s)
```
