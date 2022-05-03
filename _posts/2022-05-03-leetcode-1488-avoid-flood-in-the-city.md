--- 
layout      : single
title       : LeetCode 1488. Avoid Flood in The City
tags        : LeetCode Medium Array HashTable Heap Greedy
---
二分搜學習計畫。雖然我覺得heap是比較好的解法。

# 題目
某座城市裡有無限座湖，起初都是空的，但只要湖上方降雨就會充滿水。若充滿水的湖上再次降雨，則會造成城市水災，你必須避免水災發生  
輸入陣列rains，rains[i]=n，若n>0代表在第i天，第n座湖會降雨；若n==0則代表當天不降雨，你可以選擇一座滿水的湖將其抽乾。  

回傳陣列ans，符合以下規則：  
- ans大小等於rains大小   
- 若rains[i]>0則ans[i]=-1　　
- 若rains[i]=0則ans[i]=被抽乾的湖編號  

如果有多種可能的答案，回傳其中一種；不能避免水災的話則回傳空陣列。  
注意：如果你選擇抽乾空的湖，則不會發生任何改變。  

# 解法
參考[這篇解法](https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697703/greedy-with-a-heap)，和我當初的想法比較接近。  
使用min heap紀錄最即將發生的淹水日，每次碰到rains[i]=0時，優先選擇最接近的一天，將其對應到的湖抽乾。  

rainyDay雜湊表保存各個湖的下雨日期，用於之後計算淹水日。  
floodDay是min heap，保存最即將發生的淹水日。  
fullLake集合標記已經滿水的湖。  

首先遍歷一次rains，將各降雨日分配到rainyDay中。再遍歷一次rains，如果當前降雨的湖已經滿了，代表無法避免淹水，直接回傳[]。否則依當日是否降雨進行相應動作。  
若當天不下雨，則選擇最即將會淹水的那天d，其淹水的湖rains[d]=x，將第x號湖抽乾；若當天下雨，則將n號湖標記滿水，並查看n號下次降雨是哪天，將那天加入淹水日期floodDay中。

```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rainDay=defaultdict(deque)
        floodDay=[]
        fullLake=set()
        ans=[-1]*len(rains)
        for i,n in enumerate(rains):
            rainDay[n].append(i)
        for i,n in enumerate(rains):
            if n in fullLake: # flood
                return []
            if n==0:
                if not floodDay:
                    ans[i]=1
                    continue
                d=heappop(floodDay) # nearst day to flood
                x=rains[d] # lake rains[d] will flood at day d
                ans[i]=x # dry lake
                fullLake.remove(x)
            else:
                fullLake.add(n)
                rainDay[n].popleft()
                if rainDay[n]:
                    heappush(floodDay,rainDay[n][0])
                    
        return ans
```

二分搜方法還不太好想，我又參考了[這篇](https://leetcode-cn.com/problems/avoid-flood-in-the-city/solution/avoid-flood-in-the-city-by-ikaruga/)。  

主要思路改為以dry紀錄不下雨的的日期，在可能會遇到淹水的時候，才回去dry裡面找哪天可以抽水。  
lastRain紀錄第n座湖上次下雨的日期，如果當前n已經滿了，則n找上一次下雨lastRain[n]後有沒有哪天可以抽水，找不到就淹水，回傳[]；找到記得把那天日期刪掉。  
最後dry若不為空，記得全部亂填一個數字。

```python
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lastRain={}
        dry=[]
        ans=[-1]*len(rains)
        for i,n in enumerate(rains):
            if n==0:
                dry.append(i)
            else:
                if n in lastRain:
                    idx=bisect_left(dry,lastRain[n])
                    if idx==len(dry): # flood
                        return []
                    day=dry[idx]
                    ans[day]=n
                    dry.remove(day)
                lastRain[n]=i
        
        for i in dry:
            ans[i]=1
        
        return ans
```