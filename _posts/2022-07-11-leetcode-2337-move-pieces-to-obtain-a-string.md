--- 
layout      : single
title       : LeetCode 2337. Move Pieces to Obtain a String
tags        : LeetCode Medium Array TwoPointers
---
周賽301。這題我也卡了很久，最後才想出一個很醜的解法。最近兩次周賽表現實在不太行。

# 題目
輸入兩個長度為n的字串start和target，其中只包含字元"L"、"R"和空白"_"。  
空白符號"_"表示可以被任何"L"或"R"所佔據的位置。"L"在左側為空白時，可以往左側移動；同理，"R"在右側為空白時，可往右側移動。  

如果可以通過移動start移動任意次，使得start與target相等，則回傳true，否則回傳false。  

# 解法
一開始會錯題義，以為是start和target都可以移動，浪費了不少時間。正確應該是只能移動start才對。  

每個L或是R都只能往空格移動，不可能越過其他的L或R，這代表無視所有空格之後，start和target必須要是相同的字串。  
撰寫一個輔助函數groupby，將所有相鄰的L和分成幾個小區塊，每個區塊中記錄著L或R字元的索引位置。  
根據上述規則，start和target所得到的相對結構必須相同，否則直接回傳false。  

start分組後記作S，target分組後記作T。如果結構相同，再來進一步檢查每個區塊：  
- 如果區塊由L組成，則S中的索引都必須小於等於T中的索引  
- 如果區塊由R組成，則S中的索引都必須大於等於T中的索引  

如果其中一項不符合，即回傳fals。順利完成檢查則回傳true。  

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        def groupby(s):
            group=[]
            t=None
            for i,c in enumerate(s):
                if c=='_':
                    continue
                if c!=t:
                    t=c
                    group.append([c,[]])
                group[-1][1].append(i)
            return group
        
        S=groupby(start)
        T=groupby(target)
        if len(S)!=len(T):
            return False
        
        for g1,g2 in zip(S,T):
            if g1[0]!=g2[0]:
                return False
            if len(g1[1])!=len(g2[1]):
                return False
            for i,j in zip(g1[1],g2[1]):
                if g1[0]=='L':
                    if i<j:
                        return False
                else:
                    if i>j:
                        return False
            
        return True
```
