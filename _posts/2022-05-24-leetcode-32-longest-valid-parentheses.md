--- 
layout      : single
title       : LeetCode 32. Longest Valid Parentheses
tags        : LeetCode Hard String Stack
---
每日題。stack的經典題，有碰到括號的題目幾乎都能用stack解決。

# 題目
輸入只有包含'('和')'的字串，求最長的合法括號子字串的長度。

# 解法
合法的括號必須要由'('和')'各一個所組成，再多的'('也不會影響答案，一定要在出現')'時才有可能增加合法長度。  

維護堆疊st，初始化放一個-1，作為有效括號子字串的起點。  
遍歷每個字元s[i]，若s[i]是左括號，則將i押入堆疊中。  
若s[i]是右括號，有兩種可能：  
1. st中有許多左括號，去掉頂端的那個，並計算有效括號字串長度  
2. st中沒有左括號，所以把子字串起點更新為i  

因為我們碰到左括號時，每次都會將其索引押入st中，所以只有在左括號數量小於右括號數量時，st才會為空。這時只要將i放回st中，就可以字串更新起點。

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        ans=0
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans=max(ans,i-st[-1])
                    
        return ans
```
