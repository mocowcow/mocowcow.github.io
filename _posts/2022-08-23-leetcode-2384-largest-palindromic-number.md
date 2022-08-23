--- 
layout      : single
title       : LeetCode 2384. Largest Palindromic Number
tags        : LeetCode
---
周賽307。被隱藏測資卡掉不少時間，先跳去寫Q3，寫過才回來。不過Q2就來隱藏測資是真的有點過分。  

# 題目
輸入由數字組成的字串num。  
回傳使用從num中所有數字所組成的最大回文整數(字串格式)，且不可含前導零。  

註：至少要使用一個數字，且數字可以重新排序。  

# 解法
至少要使用一個數字，應該就是很明顯的提示edge case，結果我沒發現，吃了三次WA。  

因為回文可以通常切割成三個部分，左右兩段是等價的，中間依情況加上一個字元，所以我們只需要建立左半邊，之後反轉就好。  
總之先統計各數字的出現次數。題目要的是**最大的整數**，那應該要把較大的數字放在外圈，從9遍歷到0。  
每次都要在左右兩段加上相同的東西，出現次數一定要是偶數。但是中間部分只需要一個，只有在還沒找到的時後才要更新。  

題目說了不能有前導零，如果0不幸的出現在最外圈，記得要拔掉。  
但是碰到num='00'的情況，pair='0'且one=''，拔掉前導零後會剩下空字串。題目又要求至少使用一個數字，要手動回傳'0'。  

除此之外的一般況狀將pair反轉得到另一半，再夾住中間部分的one就可以了。  

```python
class Solution:
    def largestPalindromic(self, num: str) -> str:
        d=Counter(num)
        one=''
        pair=''
        
        for k in range(10,-1,-1):
            k=str(k)
            v=d[k]
            if v&1 and one=='':
                one=k
            pair+=k*(v//2)
            
        while pair and pair[0]=='0':
            pair=pair[1:]
            
        if pair==one=='':
            return '0'
            
        return pair+one+pair[::-1]
```
