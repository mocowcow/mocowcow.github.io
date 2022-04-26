---
layout      : single
title       : LeetCode 1987. Number of Unique Good Subsequences
tags 		: LeetCode Hard String DP
---
以前做過的題目，不知道那時候怎麼想得出來，這次複習竟然想了一陣子，寫完還真不太好解釋想法。

# 題目
輸入只由0和1組成的字串binary，求binary可以產生多少種獨特**好的子序列**。  
**好的子序列**指的是非空且沒有前導0的子序列(除了"0"以外)。例：  
> binary = "001"  
> unique good = ["0","1"]

# 解法
先定義dp0為以0結尾的子序列，dp1為以1結尾的子序列。  
每當讀入新的0，可以在已有的所有子序列最後方加上0；讀入新的1，在已有的所有子序列最後方加上1，並產生一個長度為1的子序列[1]。  
試試看"111"會是什麼結果：  
> binary = "111"  
> 讀入1 dp0=[], dp1=[1]  
> 讀入1 dp0=[], dp1=[1,11]  
> 讀入1 dp0=[], dp1=[1,11,111]  
> 總共3種，沒有錯  

那麼"000"會如何：  
> binary = "000"  
> 讀入0 dp0=[], dp1=[]  
> 讀入0 dp0=[], dp1=[]  
> 讀入0 dp0=[], dp1=[]  
> 算出來是0，正確答案應為1，因為[0]也是好的子序列 

既然如此，我們需要另外判斷整個binary中是否有出現過0，若有則手動將答案+1。[0]不能額外產生其他子序列，最後才加入也不影響答案。  
最後再帶入混合測資驗算：  
> bianry = "01011"  
> 讀入0 dp0=[], dp1=[]  
> 讀入1 dp0=[], dp1=[1]  
> 讀入0 dp0=[10], dp1=[1]  
> 讀入1 dp0=[10], dp1=[1,11,101]  
> 讀入1 dp0=[10], dp1=[1,11,111,1011,101]  
> dp0有1種，dp1有5種，加上[0]，共7種  

利用變數has0紀錄是否有0出現過，整個binary遍歷完之後，回傳dp0+dp1+has0就是**好的獨特子序列**總數。

```python
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD=10**9+7
        has0=dp0=dp1=0
        for c in binary:
            if c=='0':
                dp0=(dp0+dp1)%MOD
                has0=1
            else:
                dp1=(dp0+dp1+1)%MOD
        
        return (dp0+dp1+has0)%MOD

```

