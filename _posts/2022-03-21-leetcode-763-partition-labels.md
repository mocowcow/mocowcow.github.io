---
layout      : single
title       : LeetCode 763. Partition Labels
tags 		: LeetCode Medium String HashTable TwoPointers Greedy
---
每日題。  
原來以前寫過兩次，但那都是看著解答之後照做的，沒有完全理解。這次靠著自己寫出來，還能夠正確的描述邏輯，確定自己是有在進步的。

# 題目
字串s只包含小寫英文字母。所有相同的字母必須要被分在相同的子字串裡面，試著將子字串數量最大化，並回傳各子字串長度。  
> s = "ababcbacadefegdehijhklij"  
> 第一子字串為"ababcbaca"，裡面只有abc  
> 第二子字串為"defegde"，裡面只有defg  
> 第三子字串為"hijhklij"，裡面只有hijkl  
> 答案為[9,7,8]  

# 解法
當初看著分組方式不太明白，更簡單的說就是每種字母只能出現在一個子字串裡面。  
每加入一個字母c，如果c在之後某個位置x還會出現，就能確定分組範圍至少要包含到x為止。  

先建立每個字母最後的出現位置，存到雜湊表中備用。  
初始化分組起點start為-1，好用來計算分組大小。  
遍歷每個字母c，並以其最後出現位置更新分組終點end，如果當前位置i=end，就將分組大小start-end加入答案中，並更新end為i。

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen={c:i for i,c in enumerate(s)}
        ans=[]
        start=end=-1
        
        for i,c in enumerate(s):
            end=max(end,lastSeen[c])
            if i==end:
                ans.append(end-start)
                start=i
        
        return ans  
            
```

