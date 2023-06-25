--- 
layout      : single
title       : LeetCode 2747. Count Zero Request Servers
tags        : LeetCode Medium Array TwoPointers SlidingWindow Sorting HashTable
---
雙周賽107。聽說時間限制給很緊，10^6會被卡掉，有點機車。  

# 題目
輸入整數n，代表伺服器的數量。輸入二維整數陣列logs，其中logs[i] = [server_id, time]，代表伺服器server_id在時間點time收到一次請求。  

還輸入一個整數x，和整數陣列queries。  

回傳和queries相同長度的整數陣列arr，其中arr[i]代表在區間[queries[i]-x, queries[i]]**沒有收到任何請求**的伺服器數量。  

# 解法
對於每個查詢q，要找的是[q-x, q]區間**沒有收到請求**的伺服器，馬上就想到**滑動框口**。  
枚舉每個時間點q作為滑動窗口的右端點，q-x作為左端點，維護這個區間內各個伺服器收到的請求數量。  

要維護**無請求**伺服器比較麻煩，需要兩個雜湊表，一個計請求數，一個裝無請求的編號；反過來想，既然知道伺服器總共有n個，那麼只用一個雜湊表freq計請求數就好，在雜湊表內出現過的就是**有請求**伺服器，用n減掉freq的大小就是**無請求**數量。  

因為quries是無序的，先以查詢值q將查詢id分組，以遞增順序遍歷所有查詢q，將窗口移動到適當位置後才把對應的id填上答案。  

瓶頸在於排序，時間複雜度O(M log M + Q log Q)，其中M為logs大小，Q為查詢次數。  
空間複雜度O(n + Q)。  

```python
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        N=len(logs)
        Q=len(queries)
        ans=[0]*Q
        qid_group=defaultdict(list)
        for qid,qtime in enumerate(queries): # sort qid by query time
            qid_group[qtime].append(qid)

        logs.sort(key=itemgetter(1)) # sort logs by time
        freq=Counter()
        left=0
        right=0
        for qtime in sorted(qid_group):
            while right<N and logs[right][1]<=qtime: # expand window
                freq[logs[right][0]]+=1
                right+=1
                    
            while left<N and logs[left][1]<qtime-x: # shrink window
                freq[logs[left][0]]-=1
                if freq[logs[left][0]]==0: # delete key with frequency 0 
                    del freq[logs[left][0]]
                left+=1

            for qid in qid_group[qtime]: # answer queries
                ans[qid]=n-len(freq)
            
        return ans
```
