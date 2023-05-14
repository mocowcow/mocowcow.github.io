--- 
layout      : single
title       : LeetCode 2683. Neighboring Bitwise XOR
tags        : LeetCode Medium Array BitManipulation
---
周賽345。差點被這題搞死，拖到最後才解出來。  

# 題目
一個大小為n的陣列derived，這是由大小同為n的**二進位陣列**original透過XOR構造而來。  

對於derived中的每個索引i：  
- 如果i=n-1，則derived[i]=original[i] XOR oringinal[0]  
- 否則derived[i]=original[i] XOR oringinal[i+1]  

輸入陣列derived，並判斷是否存在**合法的二進位陣列**original能夠構造出derived。  
若存在則回傳true，否則回傳false。  

# 解法
以下簡稱derived為d，original為a。  
d[i]是由a[i] ^ a[(i+1)%N]所構成，要判斷d是存在對應的a。  

因為XOR相消的特性：  
- d[i] = a[i] ^ a[i+1]  
- 等於 d[i] ^ a[i+1] = a[i] ^ a[i+1] ^ a[i+1]  
- 相消得到 d[i] ^ a[i+1] = a[i]  

只要任意一個a[i]的值確定，就可以透過公式推導出a[i-1]，最後推出整個a陣列。  

研究一下，d[i]所對應的a[i]可能為何？  
若d[i] = 1，則a[i]和a[i+1]有兩種可能：  
- [1, 0]或是[0, 1]  
若d[i] = 0，則a[i]和a[i+1]有兩種可能：  
- [1, 1]或是[0, 0]  

發現不管d[i]為何，a[i]都有可能是0或是1。  

反正只有兩種可能，那麼兩種都代進去，只要其中一種合法，答案就是true。  

時間複雜度O(N)。  
空間複雜度O(N)。  


```python
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        d=derived
        N=len(d)
        
        def ok(x):
            a=[0]*N
            a[-1]=x # 假設a的最後一個元素是x
            for i in reversed(range(N-1)): # 然後把剩下的a[N-2]~a[0]都推出來
                a[i]=d[i]^a[i+1]
            return d[-1]==a[-1]^a[0] # 最後檢查d[N-1]是否合法
        
        for x in [0,1]:
            if ok(x):
                return True
            
        return False
```
