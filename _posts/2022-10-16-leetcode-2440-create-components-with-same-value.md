--- 
layout      : single
title       : LeetCode 2440. Create Components With Same Value
tags        : LeetCode Hard Array Tree DFS Graph
---
雙周賽89。也很難，我有想出正確的分割思路，但是窮舉區塊大小的地方寫錯了。最後時間不夠我修正，好可惜。    

# 題目
有一棵n個節點無向樹，節點編號分別為0到n-1。  
輸入長度為n整數陣列nums，其中nums[i]表示第i個節點的值。還有一個長度為n-1的二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，表示樹中節點a<sub>i</sub>和b<sub>i</sub>之間的邊。  

你可以**刪除**一些邊，將樹分成多個連通塊。連通塊的**值**定義為連通塊中**所有**節點i的值總和。  
你可以刪除一些邊，使得所有連通塊的值都相同，並回傳**最多**可以刪除幾個邊。  

# 解法
題目說了是無向樹，那就代表所有的節點都有連通。又說了N個節點必定是N-1個邊，代表樹中不可能有環。  
根據以上推斷，我們可以定義方法ok(target)，試著將樹分成若干個正好為target的連通塊。  

整個樹的節點總和為sm，最小節點值為mn，有N個節點。最小可能的連通塊為mn；最大可能連通塊為sm，也就是不切割。  
窮舉mn\~sm之間的所有目標值t，只有在t整除sm時，才代表有可能使所有連通塊都為t。如果分割成功，則代表可以分成sm/t個連通塊，也就是刪除(sm/t)-1個邊；若全部分割失敗，則代表只能維持一個連通塊，回傳0。  

重點在於分割的判斷方法，裡面的dfs(i)定義為以節點i出發，所分割到連通塊總和值。如果分割失敗回傳-1；正好滿足target則成立新的連通塊，回傳0；否則回傳總和val。  
從任意節點開始分組都可以，但基於方便，總是從節點0開始。只要dfs(0)為0，則代表分組完全成功。  

每次檢查分割的成本為O(N)。根據其他大神的說法，10^6內的整數中，擁有的最多因數為240個，故時間複雜度為O(N\*240)。而dfs最差情況會需要N次遞迴，空間複雜度O(N)。  

```python
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        N=len(nums)
        sm=sum(nums)
        mn=min(nums)
        
        g=defaultdict(list)
        
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def ok(target):
            seen=set()
            
            def dfs(i):
                seen.add(i)
                val=nums[i]
                for j in g[i]:
                    if j not in seen:
                        inc=dfs(j)
                        if inc==-1:
                            return -1
                        val+=inc
                if val>target:
                    return -1
                if val==target:
                    return 0
                return val
            return dfs(0)
        
        for t in range(mn,sm):
            if sm%t==0 and ok(t)==0:
                return (sm//t)-1
            
        return 0
```
