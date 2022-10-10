--- 
layout      : single
title       : LeetCode 2434. Using a Robot to Print the Lexicographically Smallest String
tags        : LeetCode Medium String Greedy Simulation Stack
---
周賽314。這題Q3算挺難的，做完了Q4才回來補交，兩題應該換個位置。  

# 題目
輸入字串s和一個擁有空字串t的機器人。選擇以下操作之一，直到s和t都為空為止：  
- 刪除字串s的**第一個**字元並將其丟給機器人。機器人會將此字元加到字t的末端  
- 刪除字串t的**最後一個**字元並將其丟給機器人。機器人會將此字元寫到紙上  

求可以寫到紙上的**最小字典順序**字串。  

# 解法
既然要求最小字典順序，那我們應該優先將字典順序最小的字母放到前面，再來處理次小的字母，以此類推。  
例如s="abadf"，從最小的'a'開始，要先把所有'a'都寫出來，之後再去考慮'b'、'c'等。  

可以先使用雜湊表d統計各字母的出現次數，方便追蹤s內各字母還剩下幾個。變數target代表當前要挑出來的字母，若d[target]為0時，切換到下一個字母。   
但有時候t裡面的字母會小於target，這時候要馬上將該字母加入答案中，才能保證答案字串較小。  

時空間複雜度都是O(N)。  

```python
class Solution:
    def robotWithString(self, s: str) -> str:
        d=Counter(s)
        s=deque(s)
        t=deque()
        ans=[]
        target='a'
        
        while s:
            if t and t[-1]<=target:
                ans.append(t.pop())
                continue
                
            if d[target]==0:
                target=chr(ord(target)+1)
                continue
                
            d[s[0]]-=1
            t.append(s.popleft())
        
        # remain
        while t:
            ans.append(t.pop())
        
        return ''.join(ans)
```

t只會將新字母加入頂端，並從頂端彈出，其實用stack就可以。而s只會從左向右依序彈出字母，也可以簡化成一個迴圈遍歷。  
反正不管如何，一定會先將遍歷到的字元c加到t頂端。之後根據剩餘次數來更新target，再將t中小於等於target的部分彈出，加到答案中。  

```python
class Solution:
    def robotWithString(self, s: str) -> str:
        t=[]
        ans=[]
        target='a'
        d=Counter(s)
        
        for c in s:
            d[c]-=1
            t.append(c)
            
            while d[target]==0 and target<'z':
                target=chr(ord(target)+1)
                
            while t and t[-1]<=target:
                ans.append(t.pop())
            
        return ''.join(ans)
```