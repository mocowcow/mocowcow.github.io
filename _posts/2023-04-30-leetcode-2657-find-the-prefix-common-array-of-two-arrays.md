--- 
layout      : single
title       : LeetCode 2657. Find the Prefix Common Array of Two Arrays
tags        : LeetCode Medium Array Counting HashTable BitManipulation Bitmask
---
雙周賽103。

# 題目
輸入兩個整數陣列A和B，兩者都是1\~n的排列。  

陣列C是A和B的**前綴共通陣列**，其中C[i]代表A和B到索引i為止有多少個共通的元素。  

求A和B的**前綴共通陣列**。  

# 解法
n最大才50，暴力檢查也沒問題。  

直接紀錄A和B分別有哪些元素出現過，遍歷1\~n中的所有數字i，先將第i位的元素加入計數，然後查看1\~n有多少個同時出現在A和B的元素即可。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnta=[0]*51
        cntb=[0]*51
        ans=[]
        
        for a,b in zip(A,B):
            cnta[a]+=1
            cntb[b]+=1
            common=0
            for i in range(1,51):
                if cnta[i]==cntb[i]==1:
                    common+=1
            ans.append(common)
            
        return ans
```

如果N很大的話就要靠雜湊表來記錄出現次數。一樣依序將A[i]和B[i]加入雜湊表中，但只有在同一個元素被**加入第二次**的時候才代表是A和B所共通，共通數common增加1。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen=set()
        ans=[]
        common=0
        for a,b in zip(A,B):
            if a in seen:
                common+=1
            seen.add(a)
            if b in seen:
                common+=1
            seen.add(b)
            ans.append(common)
            
        return ans
```

也可以用兩個bit mask表示各元素的出現狀態，兩者做AND運算就是共通的結果，其中1位元的個數就是共通數量。  
其他語言要注意型別，可能需要用long。  

內建bit_count函數可視為常數時間，時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n1=n2=0
        ans=[]
        
        for a,b in zip(A,B):
            n1|=(1<<a)
            n2|=(1<<b)
            ans.append((n1&n2).bit_count())
            
        return ans
```