---
layout      : single
title       : LeetCode 3035. Maximum Palindromes After Operations
tags        : LeetCode Medium Array String HashTable Greedy Sorting
---
周賽384。

## 題目

輸入長度 n 的字串陣列 word。  

你可以執行以下操作**任意次** (包含 0 次)：  

- 選擇整數 i, j, x, y，滿足 0 <= i, j < n, 0 <= x < words[i].length, 0 <= y < words[j].length
- 然後將 words[i][x] 和 words[j][y] 交換  

求任意次操作後，**最多**可以組成幾個**回文**字串。  

注意：i 和 j 可以相同。  

## 解法

交換字母不能改變字串長度，因此能夠組成的回文字串受限於原有的字串長度。  
並且，長度 x 的回文必須從 x-1 或是 x-2 甚至更短的回文組成。  
按照貪心的想法，先構造最短的回文總是更好的選擇。  

而回文可以由好幾組**成對**的字元組成，可以擁有最多一個**落單**的字元作為中心。  
因此先統計所有字元的總出現次數，若成對出現則計入 pair；有落單的則計入 single。  

根據剛才得出的貪心結論，先從較短的字串長度 x 開始嘗試構造回文。  

- 若 x 是偶數，則只能使用成對的字元構成  
- 若 x 是奇數，除了成對的字元，還需要一個落單的  

若滿足條件，則扣除相應的需求字元，並將答案加 1。  

但碰上以下情況會算錯：  
> words = ["a", "a"]  
> "a" 總共出現 2，pair = 1, single = 0  
> 按照上述邏輯，構造長度 1 的回文至少需要一個 single，構造失敗  
> 得到錯誤答案 0  

但答案應為 2。正確作法是在 single 不足時隨便挑一組成對的拆開來用，剩下的丟回 single。  

時間複雜度 O(N log N)。  
空間複雜度 O(N log N)。  

```python
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        sizes = []
        d = Counter()
        for w in words:
            sizes.append(len(w))
            d += Counter(w)
            
        single = pair = 0
        for v in d.values():
            pair += v // 2 * 2
            if v % 2 == 1:
                single += 1
                
        sizes.sort()
        ans = 0
        for x in sizes:
            pair_need = x // 2 * 2
            if x % 2 == 1: # odd
                if single > 0 and pair >= pair_need:
                    ans += 1
                    single -= 1
                    pair -= pair_need
                elif pair >= x:
                    ans += 1
                    pair -= pair_need + 2 # break extra pair into single
                    single += 1
                    
            else: # even
                if pair >= pair_need:
                    ans += 1
                    pair -= pair_need

        return ans
```
