--- 
layout      : single
title       : LeetCode 2522. Partition String Into Substrings With Values at Most K
tags        : LeetCode Medium Array String Greedy
---
周賽326。想太多奇怪的狀況，在這種簡單題上面浪費太多時間，看來有時候魯莽也不見得是壞事。  

# 題目
輸入一個由數字1到9所組成的字串s，和一個整數k。  

若s的一個分割滿足以下條件，則稱之為**好分割**：  
- s的每個數字都只屬於一個子字串  
- 每個子字串的值小於等於k  

求最少需要幾個子字串，才能使s符合**好分割**。如果沒有任何**好分割**的方式，則回傳-1。  

注意：字串"123"的值等於123，而字串"1"的值等於1。  

# 解法
很直覺的知道每個子字串的長度越長越好。但是我花了很多時間考慮：如果多拿一個數字，會不會使得後方的數字沒辦法小於k？答案是不會。  

最好的情況下，整個s屬於同一個子字串，初始化ans為1。  
遍歷s中所有字元c，並維護變數tt計算當前子字串的值。嘗試將c加入當前子字串中，若不會超過k則加入；否則以c另外開一個新的子字串。  
如果c本身超過了k的大小，則直接回傳-1。  

時間複雜度O(N)。空間複雜度O(1)。

```python
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans=1
        tt=0
        
        for c in s:
            n=int(c)
            if tt*10+n<=k:
                tt=tt*10+n
            else:
                if n>k:return -1
                ans+=1
                tt=n
                
        return ans
```
