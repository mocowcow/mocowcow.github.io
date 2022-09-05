--- 
layout      : single
title       : LeetCode 2396. Strictly Palindromic Number
tags        : LeetCode Medium Array String
---
雙周賽86。很奇怪的一題，雖然隱約感覺到怪異之處，但沒辦法馬上證明，只好用暴力法來做。  

# 題目
**嚴格回文**指的是：將某個數字n，分別轉成b進制字串後，每個字串都是回文的。限制2<=b<=n-2。  
輸入整數n，判斷是不是**嚴格回文**。  

n的範圍為4\~100000。  

# 解法
本來想說n越大，回文的機率越低，應該是從某個閾值開始就不可能是嚴格回文，暴力法複雜度會趨近於O(1)才對。  
我記得java就有轉進制的內建函數，我們尊貴的python竟然沒有，只好自己手刻。  

若要轉成b進制，則不斷對其取餘數，將餘數加到字串上，直到變成0為止。  
檢查回文就使用最簡單的方式：反轉字串，檢查是否相等。  

```python
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base(b):
            x=n
            nums=[]
            while x:
                r=x%b
                nums.append(str(r))
                x//=b
            return ''.join(reversed(nums))
        
        def isPalindrome(s):
            return s==s[::-1]
        
        for i in range(2,n-1):
            s=base(i)
            if not isPalindrome(s):return False
            
        return True
```

比賽解完四題還有時間，就回來想想：  
> n = 4  
> 4的2進制是100  
> n = 5  
> 5的3進制是12  
> n = 6  
> 6的4進制是12  
> n = 7  
> 7的5進制是12  
> ...

不管是多少，轉換成最後一個進制一定會失敗，所以答案在簡單不過了。  

```python
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
```




