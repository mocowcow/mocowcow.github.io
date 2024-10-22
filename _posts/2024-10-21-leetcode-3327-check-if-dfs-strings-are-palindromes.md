---
layout      : single
title       : LeetCode 3327. Check if DFS Strings Are Palindromes
tags        : LeetCode Hard String DFS
---
weekly contest 420。  
難得有我一次寫對的 Q4，可惜當天有事沒打。打虛擬賽有 300 名，虧慘了。  

## 題目

輸入一棵有 n 個節點，編號由 0 到 n - 1，且根節點為 0 的樹。  
以長度 n 的陣列 parent 表示，其中 parent[i] 是節點 i 的父節點。因節點 0 是根，所以 parent[0] = -1。  

另外輸入長度 n 的字串 s，其中 s[i] 是節點 i 對應的字元。  

最初你有空字串 dfsStr，且定義遞迴函數 dfs(int x)，輸入節點 x，並依次執行以下操作：  

- 按照**節點編號升序**遍歷 x 的所有子節點 y，並調用 dfs(y)。  
- 將字元 s[x] 追加到 dfsStr 的末尾。  

注意：遞迴函數 dfs 共享全域變數 dfsStr。  

求長度 n 的布林陣列 answer，對於 0 到 n - 1 的每個索引 i 都執行以下操作：  

- 將 dfsStr 清空，並調用 dfs(i)。  
- 若 dfsStr 是**回文**，將 answer[i] 設為 true；否則設為 false。  

回傳陣列 answer。  

回文指的是一個字串從前往後與從後往前寫法相同。  

## 解法

首先建圖，因為本身就是依序將節點 parent[i] 連到 i 上，保證子節點都是有序的，不須另外排序。  

仔細看看 dfs 行為就是**後序遍歷**，在遞迴處理所有子節點之後判斷回文串。  
例如節點 i 的字串為：  
> sub1 + sub2 + .. subn + s[i]。  

---

題目最後一句話具有非常大的提示作用：  
> 前往後與從後往前寫法相同。  

將反轉字串和原字串比對是一種經典的回文判斷方式。  
我們只需要同時維護兩個方向串接的字串，判斷兩者是否相同即可。  
例如某節點 s[i] = "a"，且子節點字串依序為 "a", "c", "b"：  
> 正序 "a" + "c" + "b" + "a"  
> = "acba"  
> 逆序 "a" + "b" + "c" + "a"  
> = "abca"  

可以看出**正序**反轉之後就是**逆序**字串，只要兩者相同則代表回文。  

---

但是字串串接的複雜度非常高，每次構造一個新字串都需要 O(M+N)，字串比對也需要 O(min(M,N))。  
而 **rolling hash** 以準確度為代價，換取了 O(1) 的查詢以及操作成本。  

字串雜湊通常以一個多項式來表示，將每個字元乘上係數後加總。係數代表他在字串中的位置。  
例如長度 N 的字串 s，其雜湊多項式為：  
> (s[0] \* base^0) + (s[1] \* base^1) + .. (s[N-1] \* base^(N-1))。  

將字串反轉的話只需將係數反轉：  
> (s[0] \* base^(N-1)) + (s[1] \* base^(N-2)) + .. (s[N-1] \* base^0)。  

按照這個規則實現字串操作即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MX = 10 ** 5 + 5
MOD = 1_000_000_003
base = 87
base_pow = [1] * (MX + 1)
for i in range(MX):
    base_pow[i+1] = (base_pow[i] * base) % MOD

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        N = len(s)
        g = [[] for _ in range(N)]
        for i in range(1, N):
            g[parent[i]].append(i)

        ans = [False] * N

        def dfs(i): # return (sz, hash1, hash2)
            sz = h1 = h2 = 0
            # concat dfs(j)
            for j in g[i]:
                t = dfs(j)
                # h1 + sub
                h1 = h1 * base_pow[t[0]] + t[1]
                # sub + h2
                h2 = t[2] * base_pow[sz] + h2
                sz += t[0]

            # append s[i]
            delta = ord(s[i])
            # h1 + s[i]
            h1 = (h1 * base + delta) % MOD
            # s[i] + h2
            h2 = (delta * base_pow[sz] + h2) % MOD
            sz += 1

            # check if palindrome
            if h1 == h2:
                ans[i] = True
            return sz, h1, h2

        dfs(0)

        return ans
```
