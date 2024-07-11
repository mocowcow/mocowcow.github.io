---
layout      : single
title       : LeetCode 3213. Construct String with Minimum Cost
tags        : LeetCode Hard Array String DP Trie HashTable
---
周賽 405。  
這題也是很神秘，測資範圍 N = 5e4，依我經驗一看就覺得 python 寫很容易出事。  
一般來說測資超過 1e4 之後，O(N^2) 的做法都會超時。  
但因為少了最極端的測資，不少人交 O(N^2) 答案竟然過了，甚至賽後看到官方提示也是叫人家用這種作法。  

如果說本來就預期 O(N^2) 解，那就是測資範圍設錯，誤導作題者。但是 8 分難度好像又配不上。
如果說測資強度太差，有些人交了 O(N sqrt(N)) 正確答案卻又超時，真的是魔法遊戲。  

## 題目

輸入字串 target，字串陣列 words，還有整數陣列 costs。兩個陣列的長度都相同。  

最初存在一個空字串 s。  
你可以執行以下操作任意次：  

- 選擇 [0, words.length - 1] 之間的索引  
- 將 words[i] 加入 s 後方  
- 成本增加 costs[i]  

求使得 s 等於 target 的最小成本。若不可能則回傳 -1。  

## 解法

在 s 等於 target 之前，我們必須重複決定**選哪個** words[i] 來加入。  
根據不同的選擇方式，有可能構成**相同的結果**，故考慮 dp。  

定義 dp(i)：構造子字串 target[i..N-1] 所需的最小成本。  
轉移：dp(i) = max(dp(j + 1) + cost) for ALL target[i..j] in words
base：當 i = N 時，字串構造完畢，回傳 0。  

每個 dp(i) 對應 N 個子字串 target[i..j]，且每次生成子字串都要 O(N) 時間，因此時間複雜度 O(N^3)。  

---

為了加快字串匹配的速度，先把 words 中所有字串加入字典樹中。  
之後枚舉 i 開始的子陣列，每次加入一個新的字元只需要 O(1) 時間匹配。  
並且，若樹中不存在 target[i..j] 的前綴，則可以直接剪枝。  

時間複雜度 O(N^2 + L)，其中 L = sum(words[i].length)。  
空間複雜度 O(N + L)。  

```python
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        N = len(target)
        trie = Trie()
        for w, c in zip(words, costs):
            trie.add(w, c)

        @cache
        def dp(i):
            if i == N:
                return 0
            res = inf
            curr = trie.root
            for j in range(i, N):
                c = target[j]
                if c not in curr.child:
                    break
                curr = curr.child[c]
                res = min(res, curr.val + dp(j + 1))
            return res 

        ans = dp(0)
        if ans == inf:
            return -1
        
        return ans


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.val = inf


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s, val) -> None:
        curr = self.root
        for c in s:
            curr = curr.child[c]
        curr.val = min(curr.val, val)
```

注意到測資範圍寫著：  
> The total sum of words[i].length is less than or equal to 5 * 10^4.  

總長度 L 限制了 words[i] 所可能出現的長度。  
最差情況下 words[i] 長度有 1,2,3,...n，求等差數列和公式 = n *(n + 1) / 2。  
滿足 n \* (n + 1) / 2 <= L，可得最後一項長度 n 大約為 sqrt(L)。  

之前我們枚舉 target[i..j] 時，大概是 O(N) 時間。其實只需要枚舉有出現過的 words[i] 長度，只需要 O(sqrt(L))。  
因此 dp 部份的正確時間複雜度是 O(N \* sqrt(L))。  

---

但字典樹會一直走到樹的葉節點為止，在 target = "aaa...aaa", words = ["a","aaa......aaa"] 的極端情況下，複雜度同樣會上升到 O(N^2)，需要想想其他字串匹配的替代方案。  

正確方式是使用 rolling hash 做字串雜湊，預處理所有 words[i] 及 target，即可用 O(1) 的時間查詢子字串是否存在。  

時間複雜度 O(N \* sqrt(L))，其中 L = sum(words[i].length)。  
空間複雜度 O(N)。  

```python
MOD = 1000015279
BASE = 87
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        N = len(target)
        
        # hash target for substrings
        h_target = [0] 
        base_pow = [1]
        for c in target:
            h_target.append((h_target[-1] * BASE + ord(c)) % MOD)
            base_pow.append((base_pow[-1] * BASE) % MOD)
            
        # hash all words
        # and collect valid sizes
        h_words = defaultdict(lambda: inf)
        sizes = set()
        for word, cost in zip(words, costs):
            sizes.add(len(word))
            h = 0
            for c in word:
                h = (h * BASE + ord(c)) % MOD
            h_words[h] = min(h_words[h], cost)
        sizes = sorted(sizes)
        
        @cache
        def dp(i):
            if i == N:
                return 0
            res = inf
            for sz in sizes:
                j = i + sz - 1
                if j >= N:
                    break
                h_sub = (h_target[j + 1] - h_target[i] * base_pow[sz]) % MOD
                if h_sub in h_words:
                    res = min(res, h_words[h_sub] + dp(j + 1))
            return res
        
        ans = dp(0)
        if ans == inf:
            return -1
        
        return ans
```
