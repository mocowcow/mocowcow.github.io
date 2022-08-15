--- 
layout      : single
title       : LeetCode 2376. Count Special Integers
tags        : LeetCode Hard DP Bitmask
---
周賽306。這題真是傷透我心，本來看測資範圍10位數應該也是可以回溯的，很抱歉不行。但是又聽說JAVA和C++能夠通過，看來又是歧視PY。  

# 題目
如果某個數字的所有位數都是不同，則稱為**特殊整數**。  
輸入正整數n，求介於區間[1, n]的**特殊整數**個數。  

# 解法
雖然以前有用過bitmask dp，但還不知道可以套在這種題型上，算是收穫一套強力模板。  

這種模板稱為數位dp，用來找到1~n範圍內的數字，每個數只能使用一次，且必須符合其他限制。  
定義dp(i,limit,mask)：表示目前要選擇第i位的數字，limit代表是否受限於n，而mask代表各數字的使用情形。  

轉移過程有點難寫成公式，簡單來講就是找到可用的數字j，加總所有j所產生的子問題。  
我覺得最精華的點在於**limit**，他代表當前選的數字j是否受限於n的第i個位數，例如：  
> n=245  
> 第一個數字必定不能大於n[0]=2  
> 若第一個數選擇2，產生的數字為2XX，則第二個數則不可大於n[1]=4；否則1XX、0XX的狀況下選擇任意數字都不會超過n。  

所以只有在當前為受限的情況下，且選擇了最大上限的數字n[i]，接下來的子問題才會持續受限；否則將不受限制，可以從0~9任意挑選。  

在來考慮前導0的特例，例如：  
> n=245  
> 3為特殊數字，但實際上的選擇過程為0 -> 0 -> 3  
> 加入前導0時，不視為選擇數字0使用   

所以mask為0時，可以持續加入前導0，limit設為false，且mask維持不變。  

```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s=str(n)
        N=len(s)
        
        @cache
        def dp(i,limit,mask):
            if i==N:
                return 1
            ans=0
            up=9 if not limit else int(s[i])
            for j in range(up+1):
                if (1<<j)&mask:continue
                if mask==0 and j==0:
                    ans+=dp(i+1,False,mask)
                else:
                    new_mask=mask|(1<<j)
                    ans+=dp(i+1,limit and j==up,new_mask)
            return ans
        
        return dp(0,True,0)-1
```
