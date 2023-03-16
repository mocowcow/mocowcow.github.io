--- 
layout      : single
title       : LeetCode 2589. Minimum Time to Complete All Tasks
tags        : LeetCode Hard Array Greedy Sorting
---
模擬周賽336。測資放水了，如果範圍改大一些是真的難。  

# 題目
有一台可以**同時**執行無限行程的電腦。輸入二維陣列tasks，其中tasks[i] = [start<sub>i</sub>, end<sub>i</sub>, duration<sub>i</sub>]，代表第i個任務至少需要執行duration<sub>i</sub>秒，且只能在閉區間[start<sub>i</sub>, end<sub>i</sub>]內執行。  

你可以只在需要的時候運行電腦。如果沒有任務，也可以將他關閉。  

求電腦**最少需要運行多久**才能完成所有任務。  

# 解法
一個任務必須盡量拖時間，直到最後一刻才開始執行，因為這樣才有更多機會和較早結束其他任務共用運行時間。  

以範例1為例：  
> tasks = [[2,3,1],[4,5,1],[1,5,2]]  
> 在第3秒的時候，tasks[0]只剩下1秒的機會，不做不行  
> 所以在第3秒運行，同時tasks[2]也可以受益  
> 變成tasks = [[2,3,0],[4,5,1],[1,5,1]]  
> 最後在第5秒，tasks[1]和tasks[2]都還需要1秒  
> 所以在第5秒運行，完成所有任務  
> 總共運行2秒  

先將tasks以結束時間排序，窮舉每一個時間點time。每一秒檢查所有行程tasks[i]，如果當前時間time到結束時間e剛好相等，則代表這秒鐘必須得運行電腦，才能使得所有任務都及時完成。  
若在第time秒鐘運行電腦，答案加1，並將所有符合s <= time <= e的行程所需時間減1。  

時間複雜度O(N\*T)，其中N為tasks大小，T為max(end<sub>i</sub>)。直接在tasks上修改，空間複雜度O(1)。  

```python
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=itemgetter(1))
        
        ans=0
        for time in range(2001):
            on=False
            for s,e,d in tasks:
                if time>e or time<s:continue
                if time+d-1==e:
                    on=True
                    break
            
            if on:
                ans+=1
                for i,(s,e,d) in enumerate(tasks):
                    if time>e or time<s:continue
                    tasks[i][2]-=1
                    
        return ans
```

上面方法是以每個時間點來考慮，檢查是當前秒數是否有某些行程必須運行，並將運行到的行程時間扣除。  
也可改成檢查每個行程運行時間是否足夠，若不足夠則從後往前將某些秒數設為運行。  

維護整數陣列run，初始全為0，代表不運行；設為1則代表該時間點將運行電腦。  
遍歷每個行程，先檢查其允許範圍內run[s,e]是否滿足d秒。若不滿足則從e向前將某些秒數設為1，直到滿足為止。  
最後run的總和就是答案。  

時間複雜度O(N\*T)，其中N為tasks大小，T為max(end<sub>i</sub>)。空間複雜度O(T)。  

```python
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=itemgetter(1))
        run=[0]*2001
        
        for s,e,d in tasks:
            for i in range(s,e+1):
                d-=run[i]
            if d>0:
                for i in range(e,s-1,-1):
                    if run[i]==0:
                        run[i]=1
                        d-=1
                        if d==0:break
                            
        return sum(run)
```