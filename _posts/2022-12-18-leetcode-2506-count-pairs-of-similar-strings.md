--- 
layout      : single
title       : LeetCode 2506. Count Pairs Of Similar Strings
tags        : LeetCode Easy Array String HashTable Bitmask
---
周賽324。

# 題目
輸入字串陣列words。  

若兩個字串由相同種類的字母所組成，則視為**相似的**：  
- 例如"abca"和"cba"都由'a', 'b'和'c'組成  
- 而"abacba"和"bcfd"的組成字母不同，則不相似  

求有多少數對(i, j)使得words[i]和words[j]相似，且0 <= i < j < len(words)。  

# 解法
首先當然是暴力法，窮舉所有(i, j)，全部裝進集合中去重複，看看相不相等。  

時間複雜度O(N^2\*M)，其中N = len(words)，M = len(words[i])。每次同時存在兩個集合，且字母最多只有26種，可以視為常數，空間複雜度O(1)。  

```python
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        N=len(words)
        ans=0
        for i in range(N):
            for j in range(i+1,N):
                if set(words[i])==set(words[j]):
                    ans+=1
                    
        return ans
```

每次都重新建集合很沒效率，但集合又不能hash。  
可以把集合排序過後轉成tuple或是字串，這樣就可以放進雜湊表計數了。  

在遍歷words過程中順便求相似數對，只需要一次遍歷。  

時間複雜度降低到O(NM)。空間複雜度比前一種方法稍高，為O(N)。  

```python
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans=0
        d=Counter()
        for w in words:
            s=str(sorted(set(w)))
            ans+=d[s]
            d[s]+=1
                    
        return ans
```

又因為字母只有26個，剛好可以用bitmask來代表各字母的出現狀態。  
'a'出現則將第一個位元設為1，而'b'則是第二個位元，以此類推。  

時間複雜度O(MN)。空間複雜度O(N)。  
理論上運算次數應該比較少才對，執行卻比第二種方法慢。

```python
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans=0
        d=Counter()
        for w in words:
            mask=0
            for c in w:
                mask|=(1<<(ord(c)-97))
            ans+=d[mask]
            d[mask]+=1
                    
        return ans
```