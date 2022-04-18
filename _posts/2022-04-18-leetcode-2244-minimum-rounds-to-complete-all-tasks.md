---
layout      : single
title       : LeetCode 2244. Minimum Rounds to Complete All Tasks
tags 		: LeetCode Medium Array Math Greedy
---
周賽289。

# 題目
輸入整數陣列task，代表各任務的難度。  
每一輪工作時間，你可以選擇完成2或3個**相同難度**的任務，求最少需要幾輪才能做完所有工作。若無法做完，則回傳-1。

> tasks = [2,3,3]  
> 難度2的工作只有1個。每次只能選擇做2或3個，故無法完成，回傳-1

# 解法
每次只能做同樣難度的工作，先用雜湊表把各難度分類計數，個別處理。  
題目很好心的告訴我們，若數量只有1時無法完成，那麼有沒有其他狀況也不能完成？2和3當然可以，4,5,6..都可以由2和3組成，全部都沒問題。  
想要最少的工作輪數，盡可能每次做3個工作，先考慮工作數不被3整除的情況：  
> 工作4，可以拆成2+2  
> 工作5，可以拆成3+2  
> 工作7，可以拆成3+2+2  
> 工作8，可以拆成3+3+2  

很明顯可以看出來(工作數/3)向上取整就是最少輪數。

```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ctr=Counter(tasks)
        ans=0
        for v in ctr.values():
            if v==1:
                return -1
            ans+=math.ceil(v/3)
            
        return ans
```

改成不靠內建含函數的方法。  
一個數n除x，想要改成向上取整的話，可以將n加上x-1。  
> n=9, x=3  
> (9+3-1)/3=3  
> n=10, x=3  
> (9+3-1)/3=4

此題x為3，故先加上2後再除法。

```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ctr=Counter(tasks)
        ans=0
        for v in ctr.values():
            if v==1:
                return -1
            ans+=(v+2)//3
            
        return ans
```

