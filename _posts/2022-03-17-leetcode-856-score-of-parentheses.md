---
layout      : single
title       : LeetCode 856. Score of Parentheses
tags 		: LeetCode Medium String Stack 
---
每日題。stack連續第五天，這周根本是stack之周。  

# 題目
字串s只由'('和')'組成，用下列規則計算得分：  
- 如果出現空括號'()'則得到1分  
- 多個分數相鄰則等於其加總，如'()()'為2分  
- 括號包含其他分數，則將其加倍，如'(())'為1*2=2分

# 解法
測資傳入的一定是合法輸入，不需要考慮到非成對的括號，且長度至少為2，那我們只要簡單歸納會出現的狀況：  
1. 碰到'('，之後一定會')'把他關起來。先押入stack中  
2. 碰到')'，且stack頂端是'('，是空括號。彈出一個元素並押入1  
3. 碰到')'，但stack頂端是數字。初始和為0，不斷加總數字，直到碰到'('為止，將總和*2後押入stack

最後stack中一定只剩下一堆數字，加總就是答案。

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        for c in s:
            if c=='(': #case1
                st.append(c)
            elif c==')':
                if st[-1]=='(': #case2
                    st.pop()
                    st.append(1)
                else:
                    n=0
                    while st[-1]!='(': #case3
                        n+=st.pop()
                    st.pop()
                    st.append(n*2)
                    
        return sum(st)
```

