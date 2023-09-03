---
layout      : single
title       : LeetCode 2839. Check if Strings Can be Made Equal With Operations I
tags        : LeetCode Easy String HashTable Sorting
---
雙周賽112。

## 題目

輸入字串s1和s2，兩者長度都是4，只由小寫英文字母組成。  

你可以對兩者執行以下操作任意次  

- 選擇兩個索引i和j，滿足 j - i = 2。然後將索引上的字元交換  

若可以使得s1和s2相等，則回傳true，否則回傳false。  

## 解法

兩個索引差為2，就是以奇偶數分組的意思。  
至於改s1或改s2都可以，只要能讓兩者相等就好。  

可以操作任意次，代表只要兩字串中的兩個組的字元次數相等，就一定可以排成相同順序。  

奇偶數分兩次處理，把s1中的字元計數+1，s2的字元計數-1，若出現次數相同，則所有計數都會是0；不為0則回傳false。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        for i in range(2): # odd/even
            d=Counter()
            for j in range(i,4,2):
                d[s1[j]]+=1
                d[s2[j]]-=1
            for v in d.values():
                if v!=0:
                    return False
                
        return True
```

後來看到前幾名的py神寫法，驚覺我根本不會py。  

不去管出現次數，直接奇偶分類排序判斷是否相等。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2])==sorted(s2[::2]) and sorted(s1[1::2])==sorted(s2[1::2])
```
