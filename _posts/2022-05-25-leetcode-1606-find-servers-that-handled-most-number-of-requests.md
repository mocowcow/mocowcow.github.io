--- 
layout      : single
title       : LeetCode 1606. Find Servers That Handled Most Number of Requests
tags        : LeetCode Hard Array Greedy SortedList Heap
---
模擬雙周賽36。沒什麼難度的Q4，單純考資料結構而已。

# 題目
有k個伺服器，編號從0到k-1，用於同時處理多個請求。每台伺服器一次只能處理一個任務。任務根據以下演算法分配：  
- 第i個抵達的任務  
- 如果全部伺服器都在忙，則丟棄任務  
- 否則優先分配給第(i mod k)個伺服器  
- 如果第i個伺服器不可用，則嘗試第i+1個，以此類推  

輸入嚴格遞增的正整數陣列arrival和load，其中arrival[i]表示第i個任務的抵達時間，load[i] 表示第i個任務的占用時間。  
你要找到最忙的伺服器，如果某些伺服器處理的任務數量最多，則被視為最忙的。  

回傳一個陣列，包含所有最忙的伺服器id。可以以任何順序回傳。

# 解法
依照題意，我們會需要將閒置的伺服器依序排列，才可以使用二分搜在短時間內找到適合的伺服器。  
有什麼資料結構可以維持有序的數列？我們最愛的sorted list！  

再來需要處理繁忙伺服器，要取出時間最接近當前的繁忙伺服器，確認是否已經結束。  
使用sorted list也是可以，但是用heap好像感覺更好，畢竟每次只取第一個元素。  

資料結構決定好之後就沒什麼問題了，初始化cnt陣列做為每個伺服器處理的任務計數，整數mx紀錄一台伺服器最多處理多少任務。  
一開始所有伺服器都是閒置的，通通加入free裡面。  
開始遍歷所有arrival及load，重複以下流程：  
- 先檢查最小堆疊busy，將完成任務的伺服器重新加回free中  
- 如果沒有可用的閒置伺服器，直接放棄這個任務  
- 二分搜找最適合的伺服器，如果超出free索引，代表需要回頭，直接選擇第0個  
- 被選中的伺服器任務計數+1，更新mx，最後丟到busy中  

所有任務處理完成後，在cnt查看有哪些伺服器執行了mx個任務，將其加入答案中回傳即可。

```python
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        N=len(load)
        cnt=[0]*k
        mx=0
        busy=[] # heap, (time,server)
        free=SortedList()
        for i in range(k):
            free.add(i)
        
        for i in range(N):
            curr=arrival[i]
            cost=load[i]
            
            # release finished
            while busy and busy[0][0]<=curr:
                _,id=heappop(busy)
                free.add(id)
                
            # all busy
            if not free:
                continue
                
            # process
            target=i%k
            idx=free.bisect_left(target)

            # go front
            if idx==len(free): 
                idx=0
            
            id=free[idx]
            heappush(busy,(curr+cost,id))
            cnt[id]+=1
            free.pop(idx)
            mx=max(mx,cnt[id])
            
        return [id for id,n in enumerate(cnt) if n==mx]
```
