--- 
layout      : single
title       : LeetCode 2745. Construct the Longest New String
tags        : LeetCode Medium DP Greedy
---
雙周賽107。雖然我感覺有公式解，但是測資不大就算了，賽後再來補。  

# 題目
輸入三個整數x, y和z。  

你有x個字串"AA"，y個"BB"，還有z個"AB"。　　
你想選擇任意個(也可能為零個)字串連接在一起，但不可以出現"AAA"或"BBB"子字串。  

求串接的**最大**字串長度。  

# 解法
開頭選AA、BB或是AB都沒關係，答案至少是2。  
之後根據前一個選擇prev，當前的選項也會改變：  
- prev是AA，只能接著選BB  
- prev是BB，能接著選AA或AB  
- prev是AB，能接著選AA或AB  

發現前者是BB跟AB都相同的，只要判斷前一個是不是AA就好。  
起始各有(x,y,z)個，選擇順序AA, BB, AB和AB, AA, AB都會導向同一個重疊的子問題(x-1,y-1,z-1)，因此可以考慮dp。  

定義dp(x,y,z,prev_is_AA)：當三個字串各剩下x,y,z個，且前一個選擇為prev時，可以組成的最大長度。  
轉移方程式：若prev是AA，則dp(x,y,z,prev_is_AA)=2+dp(x,y-1,z,False)；  
否則dp(x,y,z,prev_is_AA)=2+max(dp(x-1,y,z,True), dp(x,y,z-1,False))  
base cases：當x,y,z都為0時，已經沒有可以使用的字串，回傳0；亦或x,y,z其中一者小於0時，代表不合法的狀態，回傳-2扣掉先前增加的長度。  

最後只要分別以x,y,z為開頭，取最大者就是答案。  

dp有四個狀態，x,y,z最多50，prev_is_AA只有2種。每個狀態最多轉移2次。  
時間複雜度O(x\*y\*z)。  
空間複雜度O(x\*y\*z)。  

```python
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
        @cache
        def dp(x,y,z,prev_is_AA):
            if x<0 or y<0 or z<0:
                return -2
            
            if x==y==z==0:
                return 0
            
            if prev_is_AA:
                return 2+dp(x,y-1,z,False)
            else:
                return 2+max(
                    dp(x-1,y,z,True),
                    dp(x,y,z-1,False)
                )
        
        return 2+max(
            dp(x-1,y,z,True),
            dp(x,y-1,z,False),
            dp(x,y,z-1,False)
        )
```

再來複習一次連接規則：  
> AA -> BB  
> BB -> AA or AB  
> AB -> AA or AB  

發現AB可以無限連接自己，代表AB不管怎樣都可以全部用掉。  
而AA可以接AB，AB又可以接回AA，倆倆成對，可以等比例消費掉。  
AA可以比AB多一個，長成這樣：  
> [ABAB...], AA, AB, AA  
也可以是AB比AA多一個：  
> BB, AA, BB, [ABAB...]  

結論：  
- AA跟AB一樣多，則三種可以全部用完  
- AA跟AB不一樣，則m=min(x,y)，共可以使用m\*2+1+z個  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x==y:
            return (x+y+z)*2
        else:
            return (min(x,y)*2+1+z)*2
```