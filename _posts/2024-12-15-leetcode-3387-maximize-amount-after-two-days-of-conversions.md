---
layout      : single
title       : LeetCode 3387. Maximize Amount After Two Days of Conversions
tags        : LeetCode Medium Graph Tree DFS HashTable
---
weekly contest 428。  
又是一長串垃圾題目，而且跟 Q1 一樣疑惑，再加上一堆變數。  
而且浮點數運算還沒有給誤差允許範圍，非常爛的題。  

## 題目

輸入字串 initialCurrency，最初你擁有 1.0 的 initialCurrency。  

另外輸入四個陣列，兩個是兌換的幣值對，兩個是匯率。  

- pairs1[i] = [startCurrency <sub>i</sub>, targetCurrency <sub>i</sub>]。  
    代表你可以在**第一天**以匯率 rates1[i] 把 startCurrency <sub>i</sub> 換成 targetCurrency <sub>i</sub>。  
- pairs2[i] = [startCurrency <sub>i</sub>, targetCurrency <sub>i</sub>]。  
    代表你可以在**第一天**以匯率 rates2[i] 把 startCurrency <sub>i</sub> 換成 targetCurrency <sub>i</sub>。  
- 另外，也允許以 1 / rate 的匯率把 targetCurrency 換成 startCurrency。  

求**依序**經過兩天後，能夠持有的 initialCurrency **最大值**。  

注意：匯率在同一天內不會有矛盾或循環。  
兩天的匯率是各自獨立的。  

## 解法

老實說，搞懂題目是最難的點。  
光是題目就有 8 個段落，然後下面測資限制有 12 項。  
一下子說可以逆著把 target 轉回 start，下面又說保證沒有循環，這樣到底是不是循環？  

反正當天內換過的沒必要換回去，不影響做題。  

---

把匯兌的方向視作有向圖，start 換成 target 的匯率是 r；target 換成 start 的匯率是 1/r。  
可以看做是一個**有向圖**或是**樹**。  

---

好險測資不大，最多只有 M = N = 10 種匯兌方式。  

第一天，從 initialCurrency 開始 dfs，枚舉所有邊，並在過程中紀錄當前**幣值最大值**，記做 memo1。  
路徑不會回頭，每次複雜度 O(M^2)。  

但是第二天的初始幣值是根據第一天所剩，最多有 M = 10 種。  
枚舉第一天可得到的幣值，全都做一次 dfs，記錄第二天的**各幣值最大值**，記做 memo2。  
每次複雜度 O(N^2)，至多跑 M 次。  

答案為 memo2[initialCurrency]。  

時間複雜度 O(M^2 + MN^2)。  
空間複雜度 O(M + N)。  

```python
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        memo1 = defaultdict(lambda: -inf)
        dfs(initialCurrency, "", 1, pairs1, rates1, memo1)

        memo2 = defaultdict(lambda: -inf)
        for curr, cnt in memo1.items():
            dfs(curr, "", cnt, pairs2, rates2, memo2)
            
        return memo2[initialCurrency]

def dfs(curr, fa, cnt, pair, rate, memo):
    memo[curr] = max(memo[curr], cnt)
    for i, (s, e) in enumerate(pair):
        if s == curr and fa != e: # rate
            dfs(e, curr, cnt*rate[i], pair, rate, memo)
        if e == curr and fa != s: #  1 / rate
            dfs(s, curr, cnt/rate[i], pair, rate, memo)
```

把匯兌方式建圖可以優化枚舉的複雜度。  
start 到 target 邊權 rate；target 到 start 邊權 1/rate。  

---

仔細觀察貨幣兌換的過程：  
> 第一天從 init 換成 x，、二天再從 x 換回 init。  

可以枚舉中間貨幣 temp，以第一天 init 換 temp，第二天再把 temp 換回 init。  

但 dfs 求出的是 init 換成各貨幣的匯率，memo[temp] 代表 init 換 temp。  
可以對第二天**逆向建圖**；也可以使用**除法**當作反向匯兌。此處選擇後者。  

---

也可能不存在有效的中間貨幣，故答案初始值 1。  
枚舉 temp 並以 memo1[temp] / memo2[temp] 更新答案。  

另外兩天各只需要一次 dfs，不會有重複訪問，可以把 max 改回普通賦值。  

時間複雜度 O(M + N)。  
空間複雜度 O(M + N)。  

```python
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        g1 = make_graph(pairs1, rates1)
        memo1 = defaultdict(lambda: -inf)
        dfs(initialCurrency, "", 1, g1, memo1)

        g2 = make_graph(pairs2, rates2)
        memo2 = defaultdict(lambda: -inf)
        dfs(initialCurrency, "", 1, g2, memo2)

        ans = 1
        for temp in memo1: # enumerate middle currency
            ans = max(ans, memo1[temp] / memo2[temp])

        return ans

def make_graph(pairs, rates):
    g = defaultdict(list)
    for i, (s, e) in enumerate(pairs):
        g[s].append([e, rates[i]])
        g[e].append([s, 1/rates[i]])
    return g

def dfs(curr, fa, cnt, g, memo):
    memo[curr] = cnt
    for adj, rate in g[curr]:
        if adj == fa:
            continue
        dfs(adj, curr, cnt*rate, g, memo)
```
