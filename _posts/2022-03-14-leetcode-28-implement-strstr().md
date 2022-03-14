---
layout      : single
title       : LeetCode 28. Implement strStr()
tags 		: LeetCode Easy String TwoPointers
---
以前用暴力法可以過，最近加了新測資，舊方法就失效了。只能稍微用些奧步或是更有效率的演算法。

# 題目
兩個字串haystack和needle，找needle在haystack出現的第一個索引位置，若找不到則回傳-1。  
此功能相當於Java的String.indexOf()或是C的strstr()。

# 解法
暴力法，對每個位置開始掃描整個needle是否存在，最差情況O(M*N)。  
剛好最新的測資就是專門搞這種情況的，要在"aaaa...aaaa"中找"aaaa...aaab"，只要先檢查頭尾是否都符合，確定後再開始中間字串的檢查就能通過。  

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        M = len(haystack)
        N = len(needle)
        for start in range(M-N+1):
            if haystack[start] == needle[0] and haystack[start+N-1] == needle[-1]:
                found = True
                for i in range(1, N-1):
                    if haystack[start+i] != needle[i]:
                        found = False
                        break
                if found:
                    return start

        return -1

```

再來是KMP字串比對演算法，有著O(M+N)如此可怕的複雜度，真的是神人才能想出的辦法。  
我找了艇多篇文章來看，最能夠接受的說法大概是[這篇](https://blog.csdn.net/your_answer/article/details/79619406?spm=1001.2014.3001.5501)。  
整理一下該文的精華：KMP重點在於**盡可能減少比對子字串指針的倒退次數**。若在中途比對失敗，先試著找出已比對成功的部分是否可以重複利用，減少倒退去離。  

用以前錯過的測資來當範例，括號內為比對到的部分：  
> "mississippi", "issip"  
> "m[issi]ssippi", "[issi]p"  s和p比對失敗，子字串倒退至[i]  
> "miss[i]ssippi", "[i]ssip"  繼續比對  
> "miss[issip]pi", "[issip]"  比對成功  
>  此時父字串的指針應該會在p的位置，p扣掉子字串的長度則為起始索引。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        M = len(haystack)
        N = len(needle)

        # longest suffix-prefix
        lsp = [-1]*N
        if N > 1:
            lsp[1] = 0
            i, j = 1, 0
            while i < N-1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    lsp[i] = j
                else:
                    j = lsp[j]
        # kmp
        i = j = 0
        while i < M and j < N:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = lsp[j]

        if j == N:
            return i-j
        return -1
```
