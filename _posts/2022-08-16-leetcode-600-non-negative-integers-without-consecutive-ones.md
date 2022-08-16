--- 
layout      : single
title       : LeetCode 600. Non-negative Integers without Consecutive Ones
tags        : LeetCode Hard DP Bitmask
---
數位DP練習題。

# 題目
輸入正整數n，回傳[0, n]範圍有多少個整數，其二進位表示中**不包含連續的1**。  

# 解法
這題滿奇妙的，給的n是十進位，檢查的規則卻是二進位，難到要我手動把n轉成二進位然後數位DP嗎？  
先算一下複雜度：n上限10^9，轉換成二進位會是30個位元。每個位元只有0和1兩種可能，轉移次數2次，且根據前一個數是否為1產生兩種狀態，總複雜度應該是O(30\*2\*2)，計算次數意外的少，就照著這個思路去實作了。  

試想以下例子：  
> n=5, binary='101'  
> 如果第一個數字選擇1，則之後必定1XX，所以第二個數字只能選0  
> 如果第一個數字選擇2，則之後必定0XX，所以後方的數字選什麼都不會超過5  

二進位也同樣也符合數位DP的規則。所以若受限於n，則上限設為s[i]；否則設為1。  
中途如果碰到兩個1連續出現，則略過不計算；若成功處理完30個位元，則產生一個合法的數字。  

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        s=bin(n)[2:]
        N=len(s)
        
        @cache
        def dp(i,is_limit,prev_one):
            if i==N:return 1
            up=int(s[i]) if is_limit else 1
            ans=0
            for j in range(up+1):
                if j==1 and prev_one:continue
                ans+=dp(i+1,is_limit and j==up,j==1)
            return ans

        return dp(0,True,False)
```
