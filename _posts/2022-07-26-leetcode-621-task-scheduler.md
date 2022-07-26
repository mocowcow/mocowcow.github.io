--- 
layout      : single
title       : LeetCode 621. Task Scheduler
tags        : LeetCode Medium Array HashTable Greedy
---
LC75學習計畫。這題雖然有heap標籤，和我一開始的想法相同，要應用起來卻很麻煩，最後選擇完全不同的方法。  

# 題目
輸入字串陣列tasks，代表一個cpu需要做的工作，其中每個字母代表一個不同的工作。每單位時間，cpu可以選擇完成任一項工作或是閒置。  
還有個整數n，代表兩個相同種類的工作需要間隔的時間。求cpu完成所有任務的最短耗時。  

# 解法
首先排除掉n為0的特例，沒有冷卻時間，可以連續執行相同工作，那麼耗時等同於工作總數。  

假設工作A有x次，冷卻時間n，那麼要完成x次A工作至少需要：(x-1)*(1+n)時間，再加上最後的1次工作。  
推廣至整個tasks，整體工時受限於出現最多次的任務，共有most次。光是要完成most次工作就需要(most-1)*(1+n)時間，但可能有多種任務同樣出現most次，故計算出現most次的工作共cnt個，加入耗時中。  

但是在以下的例子中會出現錯誤：  
> tasks = [A,A,B,C,D,E], n = 1  
> 套入前述公式得到(2-1)*(1+1)+1  
> 得到錯誤耗時3  

因為這個公式只有考慮到最高頻率的工作A耗時，並未包含其他零星工作。  
每次完成最高頻率的工作時，至少要穿插n個不同的其他工作(或是閒置)才合法，但是要插入超過n個工作當然也沒問題。實際上應如此排程：    
> tasks = [A,A,B,C,D,E], n = 1  
> 第一輪 = [A,B,C]  
> 第二輪 = [A,D,E]  

正確耗時為6，為tasks總數。故公式得到的數字必須和task大小取較大者才是正確答案。  

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        freq=Counter(tasks).values()
        most=sorted(freq)[-1]
        cnt=len([f for f in freq if f==most])
        
        return max(len(tasks),(most-1)*(1+n)+cnt)
```
