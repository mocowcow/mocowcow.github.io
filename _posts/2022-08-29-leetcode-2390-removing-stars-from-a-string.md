--- 
layout      : single
title       : LeetCode 2390. Removing Stars From a String
tags        : LeetCode Medium Array String Stack
---
周賽308。滿傻眼的，stack經典題換皮，而且還沒有edge case，放到Q1也不為過吧。 

# 題目
輸入字串s，其中包含一些字元和星號\*。  

每次動作中，你可以：  
- 在s中選擇一顆星  
- 移除最靠近其左側的非星形字元，並移除星號本身  

求移除完所有星號的字串。  

注意：  
- 輸入的字串s保證每次刪除都是合法的  
- 答案只有一種  

# 解法
題目很好心的告訴我們每個星號都有東西刪，那就不用考慮左方沒東西的情況了。  

維護一個堆疊st，遍歷s中所有字元c，如果c是星號，則刪除堆疊頂端字元；否則將c加入堆疊。最後把所有字元拼成字串回傳。  
遍歷s的複雜度O(N)，彈出或是壓入堆疊的操作O(1)共N次，最後串接字串最多N個字元，整體複雜度O(N)。  

```python
class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        
        for c in s:
            if c=='*':
                st.pop()
            else:
                st.append(c)
                
        return ''.join(st)
```
