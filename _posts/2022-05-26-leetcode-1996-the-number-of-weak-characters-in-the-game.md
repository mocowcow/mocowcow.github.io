--- 
layout      : single
title       : LeetCode 1996. The Number of Weak Characters in the Game
tags        : LeetCode Medium Array Greedy Sorting
---
某次周賽卡死沒做出來的題目，令我印象非常深刻。而且這還是Q2，當時真的非常懷疑人生，怎麼第二題就這麼難。  

# 題目
你在玩一個有許多角色的遊戲，每個角色都有屬性：攻擊和防禦。  
輸入二維整數陣列properties，其中properties[i] = [attacki, defencei]，表示遊戲中第i個角色的屬性。  
如果有任何其他角色的攻防等級都嚴格高於該角色的攻防，則稱該角色為弱。  
換句話說，如果有某個角色j，且j的攻防都比i高，則稱i為弱角色。  

回傳弱角色的數量。

# 解法
當初想著用攻擊當作key，把所有防禦放入對應的雜湊表裡面，逐一檢查每個角色能不能找到完全更強的，可惜在40/44就超時了。  

透過排序將二維問題簡化成一維，和[354. russian doll envelopes]({% post_url 2022-05-25-leetcode-354-russian-doll-envelopes %})是相同的概念。  
先以攻擊遞減排序，再以防禦遞增排序，如此一來，前方角色的攻擊力一定**不會小於**後方角色。  
而防禦力採取遞增，確保相同攻擊力的角色中，防禦越高的越晚出現，這樣我們只要追蹤出現過的最高防禦值，就可以簡單的判斷誰是弱角色。

```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        p=sorted(properties,key=lambda x:(-x[0],x[1]))
        weak=0
        mx_def=0
        for k,d in p:
            if d<mx_def:
                weak+=1
            else:
                mx_def=d
        
        return weak
```

過了好一陣子，竟然有人提出O(N)的解法，沒錯，正是bucket sort！  
首先遍歷一次所有角色，計算每個攻擊所出現的最高防禦值，儲存在mx_def中。  
然後從最高的攻擊往下遍歷，途中維護出現過最高的防禦值mx，並以mx值更新每個攻擊力所出現的最高防禦值。  
此時mx_def已經代表大於等於a會出現的最高防禦。  
最後再遍歷一次所有角色，以當前角色攻擊力a+1去找會碰到的最大防禦值，若大於當前角色防禦d，則此角色是弱角色。  

```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mx_def=[0]*100002
        for a,d in properties:
            mx_def[a]=max(mx_def[a],d)
        
        mx=0
        for a in reversed(range(100001)):
            mx=max(mx,mx_def[a])
            mx_def[a]=max(mx_def[a],mx)
            
        weak=0
        for a,d in properties:
            if mx_def[a+1]>d:
                weak+=1
                
        return weak
```