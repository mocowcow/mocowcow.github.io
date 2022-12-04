--- 
layout      : single
title       : LeetCode 2491. Divide Players Into Teams of Equal Skill
tags        : LeetCode Medium Array Sorting TwoPointers
---
周賽322。一場比賽中選手所產生精彩的化學反應，這詞用的真有意境。  

# 題目
輸入長度為n，且保證為**偶數長度**的整數陣列skill，代表第i個選手的技巧。  
將所有選手分成n/2個組別，使得每組的技巧總和**相等**。  

一個組別的**化學反應**等於兩個選手的技巧乘積。  

求所有組別的**化學反應**總和。若無法使得每組技巧相同，則回傳-1。  

# 解法
要想要使數個選手倆倆平均分配，需要用最大配最小，當然先排序。  

若選手技巧總和為sm，需要分成N/2組，那麼可以求出每兩人總和需為target。  
遍歷N/2組，若配對到的技巧總和不為target則直接回傳-1；否則將其乘積加入答案。  

時間瓶頸為排序O(N log N)，空間只需要固定的變數，所以為O(1)。  

```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N=len(skill)
        sm=sum(skill)
        skill.sort()
        team=N//2
        target=sm//team
        
        ans=0
        for i in range(N//2):
            if skill[i]+skill[N-1-i]!=target:return -1
            ans+=skill[i]*skill[N-1-i]
        
        return ans
```

上方計算索引不太直觀，可以使用雙指針紀錄兩選手位置，每次成功配對後收縮指針。  

時空間複雜度同上。  

```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N=len(skill)
        sm=sum(skill)
        skill.sort()
        team=N//2
        target=sm//team
        
        ans=0
        lo=0
        hi=N-1
        while lo<hi:
            if skill[lo]+skill[hi]!=target:return -1
            ans+=skill[lo]*skill[hi]
            lo+=1
            hi-=1
            
        return ans
```