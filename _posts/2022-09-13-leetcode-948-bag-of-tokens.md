--- 
layout      : single
title       : LeetCode 948. Bag of Tokens
tags        : LeetCode Medium Array TwoPointers Sorting Greedy
---
前幾天的每日題。很適合資料練習雙指針和雙向佇列。  

# 題目
你的初始力量為power，初始分數為0，還有一袋代幣tokens，其中tokens[i]是第i個代幣的值。  

你可以對每個代幣執行其中一種操作：  
- 如果當前的力量至少有tokens[i]，你可以將其面朝上打出，失去tokens[i]力量、獲得1分  
- 如果當前的分數至少有1，則可以將其面朝下打出，獲得tokens[i]力量、失去1分  

每個代幣最多可以以任何順序打出一次，且不必打出所有代幣。  
求最多可以獲得多少分數。  

# 解法
代幣打出順序隨意，那我們可以將tokens排序，以便取得最大最小值。  
而最佳策略是將較大值的代幣打出反面，獲得較多的力量值，以爭取將更多較小代幣以正面打出。  

維護雙指針lo指向0，hi指向最後一個索引，分別代表當前所剩最小/最大的代幣值。  
重複執行以下動作：  
- 若剩餘力量足夠，則將lo以正面打出、得分  
- 若力量不足，但是分數還有剩，則將hi以反面打出、扣分  
- 力量分數都不足，停止操作  

途中以score更新答案最大值，代幣處理完後回傳答案。  
時間複雜度受限於排序O(N log N)，空間複雜度O(1)。  

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N=len(tokens)
        tokens.sort()
        lo=0
        hi=N-1
        score=0
        ans=0
        
        while lo<=hi:
            if power>=tokens[lo]:
                score+=1
                power-=tokens[lo]
                lo+=1
            elif score:
                score-=1
                power+=tokens[hi]
                hi-=1
            else:
                break
            ans=max(ans,score)
                
        return ans
```

以雙向佇列代替雙指針，可讀性和效能都大幅上升。  

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        q=deque(sorted(tokens))
        score=0
        ans=0
        
        while q:
            if power>=q[0]:
                score+=1
                power-=q.popleft()
            elif score:
                score-=1
                power+=q.pop()
            else:
                break
            ans=max(ans,score)
                
        return ans
```