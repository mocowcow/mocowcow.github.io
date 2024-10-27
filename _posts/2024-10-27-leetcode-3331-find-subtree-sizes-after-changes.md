---
layout      : single
title       : LeetCode 3331. Find Subtree Sizes After Changes
tags        : LeetCode Medium Tree Graph DFS HashTable Stack
---
biweekly contest 142。  

## 題目

輸入 n 個節點的樹，編號從 0 到 n - 1，且根節點為 0。  
以長度 n 的陣列 parent 表示，其中 parent[i] 代表節點 i 的副節點。  
由於 0 是根節點，因此 parent[i] = -1。  

另外輸入長度 n 的字串 s，其中 s[i] 代表節點 i 對應的字元。  

對於編號 1 到 n - 1 的所有節點，我們**同時**進行以下操作**一次**：  

- 找到**最靠近**節點 x，且具有相同字元的祖先節點 y，即 s[x] == s[y]。  
- 若不存在 y，無事發生。  
- 否則，將 x 與原父節點的連邊**刪除**，並在 x 和 y 之間連接一條邊，使 y 成為 x 的新父節點。  

回傳長度 n 的陣列 answer，其中 answer[i] 代表操作後，以節點 i 為根的子樹的**大小**。  

## 解法

根據題意模擬，構造出操作後的樹，然後求子樹大小。  

先來一次 dfs 構造新樹。  
每個節點的操作要**同時進行**，因此額外維護一個圖作為操作後的結果，而不直接修改原圖。  

要找的 y 必須是父節點，因此在向子節點遞迴的時候需要以節點 x 與字元 c 對應。  
但如果沒理解**dfs 遍歷順序**的同學可能就寫錯了。  
節點 x 離開遞迴時，必須將 x 與 c 的對應**恢復原狀**，否則會影響到不相干的子樹！  
而對應、取消的順序就與 dfs 相同，是後進先出，因此用**堆疊**實現剛剛好。  

最後第二次 dfs 求子樹大小即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N = len(parent)
        g = [[] for _ in range(N)]
        g2 = [[] for _ in range(N)]
        for i, fa in enumerate(parent):
            if i > 0:
                g[fa].append(i)

        # rebuild tree
        mp = defaultdict(list)
        def dfs(i):
            c = s[i]
            if i > 0:
                if mp[c]:
                    fa = mp[c][-1]
                else:
                    fa = parent[i]
                g2[fa].append(i)
            # i as ancestor
            mp[c].append(i)
            for j in g[i]:
                dfs(j)
            # resotre
            mp[c].pop()

        dfs(0)

        # count substree size
        ans = [0] * N
        def dfs2(i):
            nonlocal ans
            res = 1
            for j in g2[i]:
                res += dfs2(j)
            ans[i] = res
            return res

        dfs2(0)

        return ans
```
