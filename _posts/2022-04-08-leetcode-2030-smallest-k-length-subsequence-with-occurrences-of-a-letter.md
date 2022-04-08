---
layout      : single
title       : LeetCode 2030. Smallest K-Length Subsequence With Occurrences of a Letter
tags 		: LeetCode Hard Stack MonotonicStack Greedy String 
---
[316-Remove Duplicate Letters]({% post_url 2022-03-18-leetcode-316-remove-duplicate-letters %})的變種題。  
自己多寫幾次終於得到比較整潔的解法。

# 題目
輸入字串s，整數k，字元letter和整數repetition。  
以s組成長度為k的子序列，且letter至少出現repetition次的**最小字典順序**結果。

# 解法
最小順序這點和316題一樣，盡可能的把前方較大順序的字元pop掉。  

我們需要幾個變數來做輔助計算。c_remain表示接下來還有多少個字元可以用，l_remain表示接下來的字元中有幾個是letter，l_need表示還需要抓幾個letter進來。  
在pop的時考慮幾個問題： 
1. 上個字元是letter，丟掉的話，剩下的letter數量夠不夠？  
2. 丟掉上一個字元，剩下的字元夠不夠湊到k個？  

出現以上情形，則終止pop處理。把letter丟掉的話要記得回加l_need。  
pop完，若堆疊內元素不足k個，則判斷是否要將當前字元c加入堆疊：  
1. c=letter，直接加吧，多多益善。記得把l_need減1  
2. 當前數量+之後還會進來的l_need還不到k，就拿c湊數

最後更新c_remain和l_remain的值。整個字串s處理完後把堆疊串起來就是答案。

```python
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        N=len(s)
        c_remain=N
        l_remain=s.count(letter)
        l_need=repetition
        st=[]
        
        for c in s:
            while st and c<st[-1]:
                if st[-1]==letter and l_need==l_remain:
                    break
                if len(st)+c_remain==k:
                    break
                if st.pop()==letter:
                    l_need+=1
                    
            if len(st)<k:
                if c==letter:
                    l_need-=1
                    st.append(c)
                elif len(st)+l_need<k:
                    st.append(c)
                    
            if c==letter:
                l_remain-=1
            c_remain-=1
                    
        return ''.join(st)
```

