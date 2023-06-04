--- 
layout      : single
title       : LeetCode 2716. Minimize String Length
tags        : LeetCode Easy String HashTable BitManipulation Bitmask
---
周賽348。賽中是medium，賽後就改成easy。  
測資改大一點或許可以勉強放在Q2？  

# 題目
輸入字串s，你可以執行以下動作任意次：  
- 選擇一個索引i，令字元c為s[i]  
- 如果i的左方也存在字元c，則刪除**最靠近**i的一個  
- 如果i的右方也存在字元c，則刪除**最靠近**i的一個  

你的目標是將s的長度**最小化**。  

求數次動作後s的**最小**長度。  

# 解法
假設某個字元c出現了三次以上，你可以：  
- 選擇中間的作為i，並刪除兩個c  
- 選擇最前或最後的作為i，刪除一個c  

不管透過哪個方法，最後都可以刪到只剩下一個c。  
因此答案就是s中不同的字元數量。  

時間複雜度O(N)。  
s只由小寫字母組成，空間複雜度O(1)。  

```python
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
```

或是使用bitmask紀錄出現過的字母。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mask=0
        
        for c in s:
            i=ord(c)-97
            mask|=(1<<i)
            
        return mask.bit_count()
```