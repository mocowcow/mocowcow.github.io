---
layout      : single
title       : LeetCode 3447. Assign Elements to Groups with Constraints
tags        : LeetCode Medium Math HashTable
---
weekly contest 436。

## 題目

<https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/>

## 解法

MX = max(groups) = 10^5。  

改成枚舉 elements[j] 不超過 MX 的倍數並標記。  
至多 N = 10^5 個不同的元素 [1,..,N]，分別枚舉倍數到 MX，所需循環次數分別為：  
> MX / 1 次  
> MX / 2 次  
> ...
> MX / N 次  

把 MX 提出來，剩下：  
> 1 / 1  
> 1 / 2  
> ...  
> 1 / N  

是**調和級數**，複雜度 O(log N)。所以枚舉所有倍數的時間是 O(MX log N)。  

---

枚舉完 elements 的倍數之後，只要對每個 groups[i] 去查表填答案就行。  

時間複雜度 O((MX log N) + M)，其中 MX = max(groups)。  
空間複雜度 O(MX)。  

```python
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        MX = max(groups)
        d = [-1] * (MX + 1) # multiple map to elements[j]
        vis = set()
        for j, x in enumerate(elements):
            if x in vis:
                continue

            vis.add(x)
            mult = x 
            while mult <= MX:
                if d[mult] == -1:
                    d[mult] = j
                mult += x

        ans = []
        for x in groups:
            ans.append(d[x])

        return ans
```
