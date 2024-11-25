---
layout      : single
title       : LeetCode 3367. Maximize Sum of Weights after Edge Removals
tags        : LeetCode Hard Tree Graph DP Greedy Sorting
---
weekly contes 425。  
個人覺得想變數名稱比做法還難。  

## 題目

有個 n 節點的無向樹，節點編號從 0 到 n - 1。  
輸入長度 n - 1 的二維整數陣列 edges，其中 edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]，代表節點 u<sub>i</sub> 和 v<sub>i</sub> 之間存在一條權重為 w<sub>i</sub> 的邊。  

你的目標是刪除**零**或**更多**的邊，使得：  

- 每個節點至多有 k 個連向其他節點的邊。  
- 剩餘的邊權總和**最大化**。  

求進行必要的刪除之後，剩餘邊的邊權**最大和**。  

## 解法

隨便舉個簡單的例子：  
> edges = [[0,1,1], [1,2,10], [2,3,1]], k = 1  

每個節點最多只能連一條邊。  
很明顯要留 [1,2,10] 這條，他比其他兩邊更大。  

換個例子：  
> edges = [[0,1,10], [1,2,1], [2,3,10]], k = 1  

同樣最多一條邊。  
但是要改成留 [0,1,10] 和 [2,3,10] 這兩條。  

樹的結構相同，卻沒有固定選法，無法直接判斷要選刪 (或保留) 哪條邊。  

---

既然沒有選擇規律，那就只能枚舉每條邊**選或不選**。  
對 edges 中的每條邊枚舉**連或不連**，先前邊的不同選法可能會剩下相同的子樹與連接限制，有**重疊的子問題**，考慮 dp。  

節點連接數受限於 k，勢必需要額外的狀態來計數各節點的連接數。  
而節點數和邊數的上限 N = 10^5，會產生 10^10 個狀態，明顯不可行。  

---

本題測資是**樹**，又想考慮 dp，那就是樹狀 dp。  

樹就是**沒有循環**的圖。選擇任意節點做為根，從根出發都能夠完整遍歷整棵樹的**所有節點各一次**，不重不漏。  
利用這個特性，在 dfs 節點的過程中，可以一次**枚舉所有子樹**連或不連的邊權最大和，並選擇最佳的 k 個子結果更新當前子樹的答案。  

dfs 時，參數需要紀錄當前節點 i。為了防止往回走，需紀錄父節點 fa。  
本題限制節點的邊數至多為 k0，有兩種情形：  

- i 與 fa 不連邊，所以 i 可以找 k0 = k 條邊。  
- i 與 fa 連邊，所以 i 可以再找 k0 = k-1 條邊。  

以參數 fa_conn=0/1 表示 i 是否與父節點相連。  

---

那麼假設當前節點 i 有兩個子節點，但只能選一個連。  
> edges = [[i,j1,w1], [i,j2,w2]], k0 = 1  

討論子節點 j 連不連的情況：  

- 連 j，有 take = w + dp(j, fa_conn=1)  
- 不連 j，有 notake = dp(j, fa_conn=0)  

連 j1，不連 j2。答案為：  
> = take1 + notake2  

不連 j1，連 j2。答案為：  
> = notake1 + take2  

如何決定選或不選好？討論**選 j 會產生的損益**。  
相似題 [2611. mice and cheese]({% post_url 2023-04-04-leetcode-2611-mice-and-cheese %})。  

- 不選 j，得到 notake  
- 選 j，得到 take  

因此選 j 的損益為 delta = **take - notake**。  
根據損益遞減排序，**貪心**地選前 k0 大收益的節點連邊，加 take；剩餘的都不連，加 notake。  

注意：損益有可能是**負數**，就是**虧錢**，別考慮了千萬別選。  

---

最後依照上述內容實作樹狀 dp。  

定義 dp(i, fa_conn=0/1)：以 i 為根的子樹中，每個節點至多 k 條邊的邊權最大和。fa_conn 為 1 代表與父節點相連。  
轉移：dp(i) = sum(前 k0 損益連邊) + sum(其餘不連邊)。  

選 0 當根節點，根無父節點，答案入口 dp(0, -1, 0)。  

時間複雜度 O(N log N)，瓶頸在排序。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])


        @cache
        def dp(i, fa, fa_conn):
            cand = []
            res = 0
            for j, w in g[i]:
                if j == fa:
                    continue
                take = dp(j, i, 1) + w
                notake = dp(j, i, 0)
                if notake >= take: # must no take
                    res += notake
                    continue
                delta = take - notake
                cand.append([take, notake, delta])
            
            # sort by delta, take first k0
            k0 = k - fa_conn # only take k-1 when connected to fa
            cand.sort(reverse=True, key=itemgetter(2))
            for i, x in enumerate(cand):
                if i < k0:
                    res += x[0]
                else:
                    res += x[1]
            return res

        return dp(0, -1, 0)
```
