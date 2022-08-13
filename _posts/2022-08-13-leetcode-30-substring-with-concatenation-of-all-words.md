--- 
layout      : single
title       : LeetCode 30. Substring with Concatenation of All Words
tags        : LeetCode Hard Array String HashTable SlidingWindow
---
每日題。有點麻煩的題，雖然測資範圍很大，但是好像暴力法也能過，可能因為這樣才一堆人按爛。  

# 題目
輸入字串s，還有一個由相同長度字串組成的陣列words。回傳s中子字串的所有起點索引，其正好是words每個單字正好出現一次所組成。  
你可以由任何順序回傳答案。  

# 解法
words中的每個單字長度相同，記為word_size。words裡面共有M個單字，而要找的是所有單字都出現一次，所以總長度total_size正好會是word_size*M。  

首先將words中所有單字裝入雜湊表target中計數，之後對s中每個索引i以滑動窗口來找到合法的起點索引。  
從i開始，每次取word_size個字元組成子字串，加入window中，共需要使用到total_size個字元。  
因為不可以包含非words的字元，所以在窗口移動的過程中，若出現不在words中的子字串，則可以直接剪枝，結束這次檢查。  
最後檢查window中所包含的子字串是否和target相同，若是則將起點索引i加入答案中。  

每次滑動窗口複雜度為O(M\*word_size)，共需要重複N次，整體複雜度為O(N\*M\*word_size)。  

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N=len(s)
        M=len(words)
        word_size=len(words[0])
        total_size=M*word_size
        target=Counter(words)
        ans=[]
        
        for i in range(N-total_size+1):
            window=Counter()
            for j in range(i,i+total_size,word_size):
                w=s[j:j+word_size]
                window[w]+=1
                if window[w]>target[w]:break
            if window==target:
                ans.append(i)
                
        return ans
```
