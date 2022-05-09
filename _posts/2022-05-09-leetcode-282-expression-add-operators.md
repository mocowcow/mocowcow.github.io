--- 
layout      : single
title       : LeetCode 282. Expression Add Operators
tags        : LeetCode Hard String Math Backtracking
---
跟今天每日題有點像，特地回來複習。但是我又開始糾結backtracking和dfs到底差在哪裡？  
有一說是backtracaking在剪枝的時候會恢復上一動的狀態，以退回走過的路徑；又有一說dfs是處理顯式樹(路徑已經固定)，而backtracaking處理的是隱式樹(自己找可行路徑出來)。  
那麼這題符合隱式樹，只是沒有回退過的路徑，可能勉強算是backtracaking吧？

# 題目
輸入一個只包含數字的字串num，以及整數target。  
你可以在num中任意位置插入一個或多個'+', '-', '*'運算子，並使運算結果等於target，求所有可能的算式。  
注意，算式中的運算元**不可以有前導零**。

# 解法
這種題也沒什麼好辦法，只能用回溯暴力搜索，找到可行的答案。  
每次切割出1個以上的數字搭配三種運算，直到最後數字用完時，若算式結果剛好等於target則加入答案。  
比較麻煩的有兩個問題：  
1. 算式中第一個運算元只能直接加入，不能使用運算子  
2. 若切割運算元時，第一個數字就碰到0，則不能繼續加上其他數字  

而像是'0123'這種例子，上述兩種狀況會同時出現，算式中第一個數勢必為0。  
我們可以把將在切割完運算元之後，再判斷當前是否為算式中第一個。若是，則直接以當前數做為算式；否則分別套用上三種運算子。  

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N=len(num)
        ans=[]
        
        def bt(i,exp,val,prev):
            if i==N:
                if val==target:
                    ans.append(exp)
            else:
                for j in range(i,N):
                    if j>i and num[i]=='0':
                        break
                    nstr=num[i:j+1]
                    n=int(nstr)
                    if prev is None: # first number
                        bt(j+1,nstr,n,n)
                    else:
                        bt(j+1,exp+'+'+nstr,val+n,n) # add
                        bt(j+1,exp+'-'+nstr,val-n,-n) # minums
                        bt(j+1,exp+'*'+nstr,val-prev+prev*n,prev*n) # multiply
        
        bt(0,'',0,None)
        
        return ans
```
