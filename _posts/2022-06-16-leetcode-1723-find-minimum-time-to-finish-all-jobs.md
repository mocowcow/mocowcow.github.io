--- 
layout      : single
title       : LeetCode 1723. Find Minimum Time to Finish All Jobs
tags        : LeetCode Hard Array Backtracking Sorting 
---
相似題[2305. fair distribution of cookies]({% post_url 2022-06-13-leetcode-2305-fair-distribution-of-cookies %})。與其說相似不如說是升級版，測資更大而已。  

# 題目
輸入整數陣列jobs，其中jobs[i]是完成第i個工作的所需時間。  
你要將所有工作分給k個工人。試找出一個最佳分配，使所有工人中的最大工作時間最小化。  

回傳**最大工作時間**的**最小值**。  

# 解法
這題N最大值到12，還在回溯法的合理範圍內，只是需要更多的優化技巧和剪枝。  

第一個技巧是排序，將耗時較久的工作排在前方，可以減少分支數量。  
再來是**檢查上一個工人的工時是否與當前相同**，若相同則代表給誰都一樣，重複的就不嘗試了。  
最後排除比已知答案更差的選擇。  

```python
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N=len(jobs)
        worker=[0]*k
        ans=inf
        jobs.sort(reverse=True) # 先分配較耗時的工作
        
        def bt(i):
            nonlocal ans
            if i==N:
                ans=min(ans,max(worker))
                return 
            for j in range(k):
                if j>0 and worker[j]==worker[j-1]: # 相同的分支，不嘗試
                    continue
                if worker[j]+jobs[i]>ans: # 比已知結果更差，不嘗試
                    continue
                worker[j]+=jobs[i]
                bt(i+1)
                worker[j]-=jobs[i]
            
        bt(0)
        
        return ans
```
