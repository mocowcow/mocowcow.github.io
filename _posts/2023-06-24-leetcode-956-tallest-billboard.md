--- 
layout      : single
title       : LeetCode 956. Tallest Billboard
tags        : LeetCode Hard Array DP
---
每日題。還滿有意思

# 題目
你想要立一個廣告牌，越高越好。一個廣告牌需要由兩支長度相同的支架來支撐。  

輸入陣列rods，代表不同鐵桿的長度，你可以把若干個鐵桿焊接在一起。  
例如你有長度分別為[1,2,3]的鐵桿，可以焊成一個長度6的鐵桿。  

求廣告牌可以架設的最大高度。若無法架設則回傳0。  

# 解法
我們需要湊出兩個同樣長度、盡可能長的支架。  
對於每個鐵桿，有三種選擇：  
1. 焊到第一個支架上  
2. 焊到第二個支架上  
3. 丟掉不用  

根據以上規則可以定義出dp(i,bar1,bar2)：代表剩前i個鐵桿，且兩個支架分別為bar1和bar2長度時，可以得到的最大高度。  
但是鐵桿有20支，窮舉每個選或不選高達2^20種可能，還要乘上20個狀態，複雜度還是略高。  

首先對於兩個支架來說先後**順序不重要**，例如dp(i,x,y)和dp(i,y,x)的結果是相同的。  
在者，同樣高度的部分可以先提取出來，例如dp(i,2,10)等價於2+dp(i,0,8)。  
最後，我們只要確保兩支架長度相同，可以直接紀錄差值，dp(i,0,8)和dp(i,8,0)可以分別表示為dp(i,8)和dp(i,-8)。  
又根據上述提到**順序不重要**，所以dp(i,-8)等價於dp(i,8)，直接取絕對值即可。  

舉個例子：  
> rods=[2,2,1,1]  
> 如果前兩個長度1鐵桿分給兩個支架，答案會是1+dp(1,0)  
> 如果前兩個長度1鐵桿都不選，答案會是dp(1,0)  
> 這兩者都會使用到到dp(1,0)這個狀態  

定義dp(i,bar)：剩下前i個鐵桿，且支架長度差為bar時，可以得到的最大高度。  
轉移方程式：dp(i,bar)=min( dp(i-1,bar), dp(i-1,bar+rods[i]), dp(i-1,abs(bar-rods[i])+min(bar,rods[i])) )
base cases：當i<0，代表沒有鐵桿了，支架差值bar=0代表兩者長度相同，回傳0；否則代表長度不同，回傳-inf使答案無效化。  

時間複雜度O(N\*S)，其中N為rods長度，S為sum(rods)。  
空間複雜度O(N\*S)。  

```python
code class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        N=len(rods)
        
        @cache
        def dp(i,bar):
            if i<0 and bar==0:
                return 0
            if i<0:
                return -inf
            x=rods[i]
            # no take
            ans=dp(i-1,bar)
            # add to long bar
            ans=max(ans,dp(i-1,bar+x))
            # add to short bar and extract common height
            common=min(bar,x)
            ans=max(ans,dp(i-1,abs(bar-x))+common)
            return ans
        
        return dp(N-1,0)

```
