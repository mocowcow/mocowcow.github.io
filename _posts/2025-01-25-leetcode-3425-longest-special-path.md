---
layout      : single
title       : LeetCode 3425. Longest Special Path
tags        : LeetCode Hard Graph Tree DFS PrefixSum Stack
---
biweekly contest 148。  
這題是真的猛，我想了好久才懂，但細節很難寫，變數名也很難取。  

## 題目

<https://leetcode.com/problems/longest-special-path/>

## 解法

以下稱 nums[i] 為 i 節點的**顏色**。  

首先最重要的，**節點 0 是根**。  
如果沒有指定根節點，則每個點都可能做為路徑起點，需要 O(N^2) 才能找到所有路徑。  
但指定根節點後，就可以從 0 出發開始 dfs，只需要 O(N) 時間。  

---

從特殊到一般，先考慮樹的特殊情況：形成一條直線。  
相當於 [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)。  

枚舉節點做為右端點，只要當前節點的顏色在路徑中出現超過一次，就收縮左端點。  
但在子樹向下分岔時，左邊界可能不同，無法重複利用。因此改用**路徑深度**的**前綴和**的角度去思考。  
假設直線樹的節點顏色為 "RBRB"，向下枚舉節點做為右端點：  
> 深度 0，路徑顏色 = "R"  
> 深度 1，路徑顏色 = "RB"  
> 深度 2，路徑顏色 = "RBR"。需扣掉前段的 "R"，剩下 "BR"  
> 深度 3，路徑顏色 = "RBRB"。需扣掉前段的 "RB"，剩下 "RB"  

觀察發現，對於路徑 [0, i] 來說，則上一個與 i 顏色相同的節點 last，**至少**要刪除掉 [0, last] 這段，才不會有重複顏色。  
為什麼說至少？舉個例子 "BRRB"：  
> 對於 "BRRB" 來說，深度 3 的節點顏色是 "B"  
> "B" 上次出現的深度是 0，所以路徑 [0, 0] 這段必須刪掉。  
> 但是對於深度 2 的節點顏色 "R" 來說， "R" 上次出現的深度是 1  
> 所以 [0, 1] 這段也必須刪掉。  
> 因此以深度 3 結尾的最長路徑是 [2, 3] = "RB"  

各種顏色都可能重複，要刪除的重複路徑必須取**最大值**。  

---

注意，對於路徑 [0, i] 來說，若存在需刪除的重複路徑 [0, last]，刪除後實際的路徑為 [last+1, i]。  \
即深度 last+1 的節點為起點，深度 i 為終點。  

在 dfs 向下遞迴過程中，維護變數 start_depth 代表起點。以及 path_len[depth] 代表路徑深度 [0, depth] 的長度和。  
實際路徑的長度和為 path_len[depth] - path_len[start_depth]
實際路徑的節點數為 i - start_depth + 1。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b, l in edges:
            g[a].append([b, l])
            g[b].append([a, l])

        ans_len = 0
        ans_node = 1
        path_len = [0] * N  # 到各深度時的路徑長度和
        last = defaultdict(list)  # 各節點顏色的上一次出現深度

        def dfs(i, fa, depth, start_depth):
            nonlocal ans_len, ans_node
            color = nums[i]

            # 若當前顏色出現過，則更新起點深度
            if last[color]:
                start_depth = max(start_depth, last[color][-1] + 1)

            # 更新答案
            valid_len = path_len[depth] - path_len[start_depth]
            valid_node = depth - start_depth + 1
            if valid_len > ans_len:
                ans_len = valid_len
                ans_node = valid_node
            elif valid_len == ans_len and valid_node < ans_node:
                ans_node = valid_node

            last[color].append(depth)  # 紀錄當前顏色出現的深度，供子節點判斷
            for j, l in g[i]:
                if j == fa:
                    continue
                path_len[depth+1] = path_len[depth] + l
                dfs(j, i, depth+1, start_depth)
            last[color].pop()  # 遞迴結束，恢復現場

        dfs(0, -1, 0, 0)

        return [ans_len, ans_node]
```
