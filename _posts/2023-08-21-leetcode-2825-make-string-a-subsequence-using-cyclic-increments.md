---
layout      : single
title       : LeetCode 2825. Make String a Subsequence Using Cyclic Increments
tags        : LeetCode Medium Array String Greedy TwoPointers DFS
---
雙周賽111。這題還挺有意思的，想了快半小時才明白。  

## 題目

輸入字串str1和str2。  

每次操作，你可以選擇一個str1的索引**集合**，對於集合中的所有索引i，會使str1[i]**循環**遞增。  
也就是說，'a'會變成'b'，而'z'會變成'a'。  

若能在**最多操作一次**的情況下使得str2成為str1的子序列，則回傳true，否則回傳false。  

## 解法

選擇一個集合的意思是：某些str[i]會被遞增一次，也就是決定每個str[i]遞增或不遞增。  

若str2要成為str1的子序列，則必須在遍歷str2的過程中，保證每個字元都依序在str1中出現。  

例如：  
> str1="ab", str2="b"  
> str1[0]="a", str2[0]="b"  
> 可以選擇讓str1[0]遞增變成"b"  
> 也可以不遞增，讓str1[1]的"b"去配對  

雖然在這個例子中，str1[0]選擇遞增或否都不影響答案。但若不選，有可能會使得某些配對失敗，例如：  
> str1="ab", str2="bb"  
> 選str1[0]遞增，變成"ba"  
> 若str1[0]不選，雖然str1[1]依然可以滿足str2[0]，但str2[1]卻無法滿足  

同理，如果str1[i]=str2[j]也一定要選。因此得到貪心的結論：能配對成功就一定要選。  

時間複雜度O(M+N)。  
空間複雜度O(M+N)。  

```python
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        M,N=len(str1),len(str2)
        
        s1=[ord(c)-97 for c in str1]
        s2=[ord(c)-97 for c in str2]
        
        def dfs(i,j):
            if j==N:
                return True
            if i==M:
                return False
            if s1[i]==s2[j]:
                return dfs(i+1,j+1)
            if (s1[i]+1)%26==s2[j]: # inc str1[i]
                return dfs(i+1,j+1)
            return dfs(i+1,j)
            
        return dfs(0,0)
```

也可以改成雙指針的形式。  

時間複雜度O(M+N)。  
空間複雜度O(1)。  

```python
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        M,N=len(str1),len(str2)
        j=0
        for i,c in enumerate(str1):
            inc=ord(c)-97+1
            inc=chr(inc%26+97)
            if j<N and (c==str2[j] or inc==str2[j]):
                j+=1
                
        return j==N
```
