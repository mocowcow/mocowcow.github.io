--- 
layout      : single
title       : LeetCode 2546. Apply Bitwise Operations to Make Strings Equal
tags        : LeetCode Medium String BitManipulation
---
周賽329。早上腦子不靈光，把記錯成0^0=1，吞一次WA，可憐。  

# 題目
輸入長度為n的二進位字串s和target。你可以執行以下的動作任意次：  
- 選擇兩個不同的索引i和j，其中0 <= i, j < n  
- 同時，將s[i]替換成s[i] OR s[j]，且s[j]替換成s[i] XOR s[j]  

例如s = "0110"，你選擇i = 0, j = 2，所以s[0]會變成0|1 = 1，s[2]會變成0^1=1，最後s = "1110"  

如果s可以透過任意次數動作變成target，則回傳true，否則回傳false。  

# 解法
字串中只有0和1，總共只會有四種情況：  
- (1, 1) 變成 (1|1, 1^1) = (1, 0)  
- (1, 0) 變成 (1|0, 1^0) = (1, 1)  
- (0, 1) 變成 (0|1, 0^1) = (1, 1)  
- (0, 0) 變成 (0|0, 0^0) = (0, 0)  

可以看出，只要有1就可以把0變成1；有兩個1，可以把其中一個1變成0；如果只剩下0，則沒辦法生出其他1。  
只要其中一方全為0，另一方一定也要為0；除此之外的狀況一定可以變得相等。  

時間複雜度O(n)。空間複雜度O(1)。  

```python
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        a=s.count("1")    
        b=target.count("1")    
        
        if a==0 or b==0:
            return a==b
        
        return True
```

再看看大神的解法，能在比賽中想出這麼簡潔的判斷真的是很誇張。  

```python
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ("1" in s)==("1" in target)
        # equals to
        # ("1" not in s)==("1" not in target)
```