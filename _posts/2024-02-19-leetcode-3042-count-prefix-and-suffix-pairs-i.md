---
layout      : single
title       : LeetCode 3042. Count Prefix and Suffix Pairs I
tags        : LeetCode Easy String Trie
---
周賽385。最近字串題是真的很多，有好好補題的同學應該上了不少分。  

## 題目

輸入字串陣列 words。  

定義**布林**函數 isPrefixAndSuffix，接收兩個字串參數 str1 和 str2。  

- 若 str1 同時是 str2 的前綴及後綴，則回傳 true；否則回傳 false  

例如 isPrefixAndSuffix("aba", "ababa") 回傳 true，因為 "aba" 既是 "ababa" 的前綴，也是後綴；而 isPrefixAndSuffix("abc", "abcd") 回傳 false，因為 "abc" 不是 "abcd" 的後綴。  

求**有多少** isPrefixAndSuffix(words[i], words[j]) 為 true、且滿足 i < j 的數對 (i, j)。  

## 解法

在字串不多的時候，可以用暴力法。  
直接枚舉所有數對 (i, j)，斷 words[i] 是否為 words[j] 的前後綴。  

在判斷 s1 是否為 s2 的前綴時，直接取 s2 前方和 s1 長度相等的子字串，判斷是否等於 s1 即可；反之，後綴就取後方相等長度。  

時間複雜度 O(N^2 \* L)，其中 L = max(len(words[i]))。  
空間複雜度 O(L)，原地比較字串可達 O(1)。  

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, s1 in enumerate(words):
            size = len(words[i])
            for s2 in words[i+1:]:
                pref = s2[:size]
                suff = s2[-size:]
                if s1 == pref and s1 == suff:
                    ans += 1
                    
        return ans
```

測資大一點就不行了，要想想優化方法。  
對於前綴後綴問題，**字典樹**是個不錯的選擇。  

根據不同的遍歷順序，可以在字典樹中維護其**前綴**或是**後綴**。  
按照這個邏輯，我們要檢查某字串是否是其他人的**前後綴**，那麼維護兩個字典樹不就好了？  
試想以下例子：  
> words = ["a", "ab", "ba"]  
> 前綴樹 = []  
> 後綴樹 = []  
> words[i] = "ba"，找不到前後綴  
> 前綴樹 = ["b", "ba"]  
> 後綴樹 = ["a", "ba"]  
> words[i] = "ab"，找不到前後綴  
> 前綴樹 = ["b", "ba", "a", "ab"]  
> 後綴樹 = ["a", "ba", "b", "ab"]  
> worwds[i] = "a"，在前後綴樹都找到 "a"  

但前綴 "a" 是來自 "ab"，而後綴的 "a" 是來自 "ba"，根本不屬於同個字串。  
這種作法還得判斷是誰生出來的，比如在節點上維護來源字串的索引，在對兩節點上的編號求交集。  
但但又會衍生別的問題。試想以下例子：  
> words = ["a", "a", "a", ...]  

每個 words[i] 都會產生前後綴 "a"，所以節點上維護的來源索引會不斷增長到 N 個。  
這樣求兩節點交集的時候，複雜度是 O(N)。而且總共要求 N 次，總共需要 O(N^2)，還是無法接受。  

---

我想了半小時，才想到解決方案：把前後綴**綁在一起**判定不就好了？  
> words[i] = "abc"  
> 前綴是依照 a, b, c 的順序生成  
> 後綴是依照 c, b, a 的順序生成  
> 把前後綴的字綁在一起  
> 變成 (a, c), (b, b), (c, a)  

隨便找一個前後綴都是 "abc" 的字串驗證看看：  
> words[j] = "abc...abc"  
> 前後綴 (a, c), (b, b), (c, a) ...

還真沒錯。那麼只要在經過的每個節點上維護**前後綴**數量即可。  

---

在 i < j 的前提下，我們想要知道 words[i] 是那些 words[j] 的前後綴。  
因此 words[j] 需要比 words[i] 更先插入字典樹中，故採倒序遍歷。  

對於 words[i] 來說，有兩件事情要做：  

1. 在字典樹中按照 words[i] 的前後綴路徑走，將最後節點 (即相同前後綴的 words[j]) 的計數加入答案  
2. 將 words[i] **所有**前後綴節點的計數加 1  

這兩件事情其實可以在一起完成，只是最後節點的計數已經被加了 1，所以加到答案的計數要記得扣掉 1。  

時間複雜度 O(L)，其中 L = sum(words[i])，題目保證不超過 5\*10^5 。  
空間複雜度 O(L)。  

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = TrieNode()
        ans = 0
        for w in reversed(words): # enumerate words[i]
            curr = root
            # build trie with pref / suffix
            for key in zip(w, w[::-1]):
                curr = curr.child[key]
                curr.cnt += 1
                
            # count of words[j] with same prefix / suffix
            ans += curr.cnt - 1
            
        return ans
        
class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0

```

上面的方法是枚舉 words[i]，其實改成枚舉 words[j] 也可以。  
只是變成在建樹的過程中，檢查先前有多少字串和當前的前後綴相同。  
建完樹後，才對完整的前後綴計數加 1。  

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = TrieNode()
        ans = 0
        for w in words: # enumerate words[j]
            curr = root
            # build trie with pref / suffix
            for key in zip(w, w[::-1]):
                curr = curr.child[key]
                ans += curr.cnt
                
            # increase pref / suff count 
            curr.cnt += 1
            
        return ans
        
class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0
```

其實看到**前綴**和**後綴**，應該會想到 z-function。但我比賽中沒想通，還得賽後讓人提點提點。  

根據定義，z[i] 指的是 s 和 s[i..] 的最長共通前綴 LCP。  
對於 s 來說，存在某個長度為 i+1 的前綴 s[..i+1]。若其同時是 s 的後綴，那麼對應 z[len(s) - 1 - i] 的值應該正好等於 前綴長度，也就是 i+1。  

透過 z 值的幫助下，先確定 words[j] 的某段前綴是否**等於**相同長度的後綴。若相等才需要找等同於該前綴的 words[i]。  
如此一來，字典樹便回歸最初始的功能：字串計數。  

注意：一般來說 z-function 的 z[0] 值不會計算，因為字串 s 和自己匹配沒有意義，故維持 0。  
在本題來說卻代表了與 s 相同的前後綴，所以要填上 len(s)。

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = TrieNode()
        ans = 0
        for w in words: # enumerate words[j]
            curr = root
            z = z_function(w)
            # build trie with pref
            for i, c in enumerate(w):
                curr = curr.child[c]
                pref_size = i + 1
                if z[-pref_size] == pref_size:
                    ans += curr.cnt
                
            # increase pref count 
            curr.cnt += 1
            
        return ans
        
class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0
        
def z_function(s):
    N = len(s)
    z = [0]*N
    z[0] = N # important !!
    L = R = 0
    for i in range(1, N):
        if R < i:  # not covered by previous z-box
            # z[i] = 0
            pass
        else:  # partially or fully covered
            j = i-L
            if j+z[j] < z[L]:  # fully covered
                z[i] = z[j]
            else:
                z[i] = R-i+1

        while i+z[i] < N and s[i+z[i]] == s[z[i]]:  # remaining substring
            z[i] += 1
        if i+z[i]-1 > R:  # R out of prev z-box, update R
            L = i
            R = i+z[i]-1
    return z
```
