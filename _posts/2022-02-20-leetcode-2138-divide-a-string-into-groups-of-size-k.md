---
layout      : single
title       : LeetCode 2138. Divide a String Into Groups of Size k
tags 		: LeetCode Easy String Simulation
---
模擬周賽276。這題解法還不少，我大概選了最懶的方式。

# 題目
輸入字串s及長度N還有字元fill，試將s切成數個長度k的子字串，若最後一部份長度不足k，則以fill填滿。  
例：  
> Input: s = "abcdefghij", k = 3, fill = "x"  
> Output: ["abc","def","ghi","jxx"]

# 解法
不管他三七二一，先確定字串長度N，直接把s後面接上k個fill，保證長度一定夠用。  
之後再從i=0開始，每次漸增k，將s[i:i+k]子字串加入答案即可。

```python
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        N = len(s)
        ans = []
        s += fill*k

        for i in range(0, N, k):
            ans.append(s[i:i+k])

        return ans

```

因為python字串slice功能其實是O(N)，而且+=運算也很貴，講求效率的話還是要修改一下。

```python
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        t = []

        for c in s:
            t.append(c)
            if len(t) == k:
                ans.append(''.join(t))
                t = []
        if t:
            for _ in range(k-len(t)):
                t.append(fill)
            ans.append(''.join(t))

        return ans

```