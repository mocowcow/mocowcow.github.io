--- 
layout      : single
title       : LeetCode 2484. Count Palindromic Subsequences
tags        : LeetCode Hard Array String DP
---
雙周賽92。一直想用3d dp來解，但是到比賽結束都沒辦法處理000000這個例子，思路完全錯誤。  

# 題目
輸入字串s，求s有多少個長度為5的**回文子序列**。  
答案很大，先模10^9+7後回傳。  

# 解法
看了許多人的解法，很多都是什麼4d dp，看到四維陣列我就不想動了。在排行榜上翻好久，終於找到瞬間理解的直觀做法。  

一個長度5的回文可以看作abcba的模式，對我們來說只有前兩位的ab和後兩位的ba要相同，中心其實無所謂。  
字串中只會出現數字，只需要10\*10的空間就可以窮舉前兩位的所有可能，而第4位需要等於第2位，第5位需要等於第1位。  

遍歷s中所有的字元c，將其轉成對應的數字x，從第5位往第1位建構：  
- 和所有長度為4且符合x...的子序列組成x...x的**回文子序列**  
- 和所有長度為3且符合.x.的子序列組成.x.x  
- 和所有長度為2的子序列組成..x  
- 和所有長度為1的子序列.x  
- 增加一個子序列x  

長度為5的子序列可以直接加進答案中，省下一個陣列。  

每個字元都要進行310次運算，時間可以視為O(310N)或是O(N)，而空間已經壓縮到O(310)或當作O(1)。  

```python
class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD=10**9+7
        ans=0
        dp1=[0]*10
        dp2=[0]*100      
        dp3=[0]*100   
        dp4=[0]*100    
        
        for c in s:
            x=int(c)
            # 5th 
            for i in range(100):
                if i//10==x:
                    ans+=dp4[i]
                
            # 4th
            for i in range(100):
                if i%10==x:
                    dp4[i]+=dp3[i]
                    
            # 3rd
            for i in range(100):
                dp3[i]+=dp2[i]
                
            # 2nd
            for i in range(10):
                dp2[i*10+x]+=dp1[i]
            
            # 1st
            dp1[x]+=1
        
        return ans%MOD
```
