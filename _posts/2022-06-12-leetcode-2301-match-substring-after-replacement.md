--- 
layout      : single
title       : LeetCode 2301. Match Substring After Replacement
tags        : LeetCode
---
雙周賽80。第一次碰到Q3是hard難度，本來想說涼涼，把它當作中等題來做，結果還真過了。

# 題目
輸入兩個字符s和sub，還有一個2D字串陣列mapping，其中mappings[i] = [oldi, newi]，代表可以用newi替換sub中任意數量的 oldi字元。且sub中的每個字元最多只能被替換一次。  

判斷是否有辦法透過替換某些字元使sub成為s中的子字串，可以則回傳True，否則回傳False。  

# 解法
看到s跟sub最大長度5000，總感覺O(N^2)有機會，破罐子破摔試著寫看看。  

首先用雜湊表建立字元的映射mp，遍歷mappings中的新舊字元a和b，將a加入mp[b]，代表b能夠由a替換而成。  
再寫一個輔助函數check(i)，代表檢查是否能將sub轉換為以s[i]為起點的子字串。  
sub的長度為M，所以需要檢查M個索引位置。若途中sub[j]和對應的s[i+j]不同，且無法透過替換而成，則代表子字串配對失敗，回傳false；順利檢查完畢則代表成功，回傳true。  

最後遍歷s的每個位置i，試著以i為起點，傳入check函數中檢查，若配對成功則回傳true。

```python
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        N = len(s)
        M = len(sub)
        mp = defaultdict(set)

        for a, b in mappings:
            mp[b].add(a)

        def check(i):
            for j in range(M):
                if s[i+j]!=sub[j] and sub[j] not in mp[s[i+j]]:
                    return False
            return True

        for i,c in enumerate(s):
            if i+M-1>=N:
                return False
            if c==sub[0] or sub[0] in mp[c]:
                if check(i):
                    return True

        return False
```
