--- 
layout      : single
title       : LeetCode 2273. Find Resultant Array After Removing Anagrams
tags        : LeetCode Easy Array String Sorting
---
周賽293。超大一長串的垃圾描述，不少人被誤導吃了WA，包括我。

# 題目
輸入索引從0開始的字串陣列words。  
重複執行以下操作直到條件不滿足為止：  
1. 找到索引i，符合0<i<words.length  
2. words[i]和words[i-1]是**異位構詞**
3. 刪除words[i]  

無法繼續刪除後，回傳words。你可以假設任意順序刪除都會得到相同的結果。

# 解法
剛開始看到anagram，直覺要用雜湊表，但想說測資很小乾脆就用排序。  

題目講了太多東西，誤會成每種anagram只能出現一次，就吃到WA。正確應該是**anagram不能連續出現**。  

釐清題意就簡單多了，每次加入新的word前，先檢查和上一個word不是anagram。

```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[]
        for w in words:
            if not ans or sorted(ans[-1])!=sorted(w):
                ans.append(w)
        
        return ans  
```
