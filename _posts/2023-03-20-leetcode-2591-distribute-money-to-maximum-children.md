--- 
layout      : single
title       : LeetCode 2591. Distribute Money to Maximum Children
tags        : LeetCode Easy Math Greedy
---
雙周賽100。這可能是全站最困難的easy題，我手滑按出了8次WA，搞到心態崩潰，太痛苦了。  
中國的朋友表示這是迷信的**忌四喜八**，非常貼切。  

# 題目
輸入整數money和children，代表你有money塊錢要分給children個人。  

你必須按照以下規則：  
- 所有錢都要分完  
- 每個人至少拿到1塊  
- 但是不可以有人拿到4塊  

求在遵守規則的情況下，**可以讓幾個人拿到**正好8塊錢**。如果不可能達成則回傳-1。  

# 解法
錢比人還少，一定有人拿不到錢，直接回傳-1。  

最佳狀況下剛好每個人都可以拿8塊，如果錢等於人\*8，直接回傳人數。  

否則窮舉(children-1)\~0個人拿8塊的情形合不合法，若合法直接回傳，否則最後回傳-1。  
仔細想想，如果剩下1人+4塊，一定不合法；那麼是2人+8塊呢？不管怎樣一定都可以避免拿到4塊。  
前面已經過濾掉錢不足的情況，至少每個人都拿的到1塊錢，所以最後在0人拿8塊的情況下一定可以成立。  

時間複雜度O(children)。空間複雜度O(1)。  

```python
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        
        if children*8==money:
            return children
        
        for i in reversed(range(children)):
            ppl_remain=children-i
            money_remain=money-8*i
            if ppl_remain==1 and money_remain==4:
                continue
            if money_remain>=ppl_remain:
                return i
```
