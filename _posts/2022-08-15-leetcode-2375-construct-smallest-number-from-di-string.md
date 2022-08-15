--- 
layout      : single
title       : LeetCode 2375. Construct Smallest Number From DI String
tags        : LeetCode Medium String Greedy Backtracking
---
周賽306。這題解法也很多元，比賽時沒想太多，直接選了一定可行的方法來做。事後複習才發現這麼有趣。  

# 題目
輸入長度為n的字串pattern，其中字元"I"表示遞增，"D"表示遞減。  
建立長度為n+1且符合以下規則的字串num：  
- num由數字1到9組成，每個數字最多使用一次  
- 若pattern[i] == 'I'，則 num[i] < num[i + 1]  
- 若pattern[i] == 'D'，則 num[i] > num[i + 1]  

回傳滿足條件且**字典順序最小**的字串num。   

# 解法
看到pattern長度最大8，字串長度最大為9，就知道回溯法代入O(N!)一定能行。  

維護回溯函數bt(i,curr)，其中i代表當前對應的pattern索引，而curr為所使用過的數字。  
當i等於N時，代表整個pattern都處理完畢，以當前curr的值去更新答案。  
否則依照pattern[i]為遞增或是遞減，來挑選下一個可以使用的數字。  

因為第一個數字沒辦法透過pattern來決定，所以要自己列舉所有數字作為第一個字元的情況。  

```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N=len(pattern)
        ans='99999999999999'
        used=set()
        
        def bt(i,curr):
            nonlocal ans
            if i==N:
                n=''.join(curr)
                ans=min(ans,n)
                return
            for j in '123456789':
                if pattern[i]=='D':
                    if j<curr[-1] and j not in used:
                        used.add(j)
                        curr.append(j)
                        bt(i+1,curr)
                        used.remove(j)
                        curr.pop()
                else:
                    if j>curr[-1] and j not in used:
                        used.add(j)
                        curr.append(j)
                        bt(i+1,curr)
                        used.remove(j)
                        curr.pop()
        
        for i in '123456789':
            used.add(i)
            bt(0,[i])
            used.remove(i)
        
        return ans
```

將判斷條件稍微修改，改成過濾掉不符合的分支，減少程式碼重複，效率也變快一些。  

```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N=len(pattern)
        ans='99999999999999'
        used=set()
        
        def bt(i,curr):
            nonlocal ans
            if i==N:
                n=''.join(curr)
                ans=min(ans,n)
                return
            for j in '123456789':
                if j in used:continue
                if pattern[i]=='I' and j<curr[-1]:continue
                if pattern[i]=='D' and j>curr[-1]:continue
                used.add(j)
                curr.append(j)
                bt(i+1,curr)
                used.remove(j)
                curr.pop()
                    
        
        for i in '123456789':
            used.add(i)
            bt(0,[i])
            used.remove(i)
        
        return ans
```

結果這題最佳解竟然是O(N)的貪心法，相較之下回溯真的是遜到不行，我很佩服能夠快速找到規律的大神。  

假設pattern的長度為4，那麼num的長度必定為5，而會出現的數字一定是1~5。因為把其中一個數字換成6或是更大的數字，必然會使字典順序變得更大。  
在pattern='IIII'時，答案不用改，就是12345了。那如果是'IIDD'呢？正確應該是12**543**。可以看出要把**連續遞減的部分**反轉。  

```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N=len(pattern)
        ans=[]
        
        left=0
        for i in range(N+1):
            ans.append(str(i+1))
            if i==N or pattern[i]=='I':
                ans[left:i+1]=reversed(ans[left:i+1])
                left=i+1
    
        return ''.join(ans)            
```
