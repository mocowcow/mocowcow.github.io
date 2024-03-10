---
layout      : single
title       : LeetCode 3076. Shortest Uncommon Substring in an Array
tags        : LeetCode Medium Array String HashTable
---
周賽388。

## 題目

輸入長度 n 的**非空字串**陣列 arr。  

求長度同為 n 的字串陣列 answer：  

- answer[i] 是 arr[i] 的**最短**子字串，且不為 arr 中其他字串的子字串  
- 若有多個答案，則選擇字典序最小者；若不存在答案，則為空字串  

回傳陣列 answer。  

## 解法

這題有點不好寫，光是生成字串 s 的所有子字串就需要兩層迴圈，寫成函數會方便很多。  

題目要求 answer[i] 只能是 arr[i] 的子字串，但不可是其他字串的子字串。  
所以我們可以先統計每個**子字串**在多少個 arr[i] 出現過。若只出現一次，則滿足條件。  

---

統計完各子字串的出現次數後，接下來就可以枚舉答案了。  

再次拿出剛才求出的 arr[i] 的所有子字串，並先以長度排序、再以字典序排序，依序枚舉可能的子字串 x。  
如果 x 只出現於一個字串，寫入答案並跳出迴圈；最後沒找到則填入空字串。  

N 為 arr 長度，M 為 max(arr[i])。  
每個字串有 M^2 個子字串，長度最多為 M，所以產生所有子字串需要 O(M^3)。  
有 N 個字串，總共是 O(NM^3)。  

但是還要排序 M^2 個子字串共 N 次，所以排序部分的成本是 O(NM^2 log M^2)。  
這複雜度我自己寫得都覺得很怪。  

時間複雜度 O(NM^3) + O(NM^2 log M^2)。  
空間複雜度 O(NM^2)。  

```python
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        @cache
        def get_sub(s): # O(M^3)
            sub = set()
            for i in range(len(s)):
                for j in range(i, len(s)):
                    sub.add(s[i:j+1])
            return sub
        
        d = Counter()
        for s in arr: # O(N) * O(M^2)
            sub = get_sub(s)
            for x in sub:
                d[x] += 1
                
        ans = [] 
        for s in arr: # O(N) * O(M^2 log M^2)
            sub = get_sub(s) 
            sub = sorted(sub, key=lambda x: (len(x), x)) # sort by size then lexicographic 
            for x in sub:
                if d[x] == 1: # found
                    ans.append(x)
                    break
            else:
                ans.append("")
        
        return ans
```

比較微妙的是純暴力法竟然能過，而且還更快。可能是有很多迴圈沒有執行到就中斷了。  

時間複雜度 O(N^2 \* M^4)。  
空間複雜度 O(M)。  

```python
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        def ok(i, sub):
            for j, s in enumerate(arr):
                if i != j and sub in s:
                    return False
            return True
        
        ans = []
        for i, s in enumerate(arr):
            M = len(s)
            res = ""
            for size in range(1, M + 1):
                for start in range(M - size + 1):
                    sub = s[start:start+size]
                    if (not res or sub < res) and ok(i, sub):
                        res = sub
                if res: # found
                    break
                        
            ans.append(res)
            
        return ans
```
