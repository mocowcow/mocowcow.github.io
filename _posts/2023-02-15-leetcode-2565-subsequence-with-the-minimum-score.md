--- 
layout      : single
title       : LeetCode 2565. Subsequence With the Minimum Score
tags        : LeetCode Hard Array String PrefixSum
---
周賽332。雖然用思考的能夠理解，但是寫code寫了三天才發現錯在哪。我恨死**前後綴分解**了。  

# 題目
輸入字串s和t。  

你可以從t中刪除任意個字元。  

如果沒有從t刪除任何字元，則分數為0；否則：  
- 令left為被刪除字元中最小的索引  
- 令right為被刪除字元中最大的索引  

然後，t的分數為right-left+1。  

求能夠使t成為s的**子序列**所需的**最小分數**。  

# 解法
相似題[2483. minimum penalty for a shop]({% post_url 2022-11-28-leetcode-2483-minimum-penalty-for-a-shop %})。雖然這題看分數不高，但我卻寫得很痛苦。確實對這類型不拿手。  

題目說的left和right很繞口，看起來只要刪掉這區間某些字元，其實全部刪掉也不會影響結果。問題轉換成：在t中刪除最短的子陣列，使得t為s的子序列。  

對於長度為M的字串s來說，我們會有M+1個分割點，左半邊從t的前方開始配對，而右半邊從t的後方開始配對，找到某個切割點使得配數總數最多。  

例如：  
> s = "abacaba", t = "bzaa"  
> s長度為7，共有8種切割  
> "" | "abacaba"  
> t前綴""，t後綴"aa"  
> "a" | "bacaba"  
> t前綴""，t後綴"aa"  
> "ab" | "acaba"  
> **t前綴"b"，t後綴"aa"**  
> "aba" | "caba"  
> **t前綴"b"，t後綴"aa"**  
> "abac" | "aba"  
> t前綴"b"，t後綴"a"  
> "abaca" | "ba"  
> t前綴"b"，t後綴"a"  
> "abacab" | "a"  
> t前綴"b"，t後綴""  
> "abacaba" | ""  

可以看到最多能夠配對到t的前後共3個字元，所以要刪掉的字元只有1個。  

但有一種例外情況：  
> s = "aa", t = "a"  
> "" | "aa"  
> t前綴""，t後綴"a"  
> "a" | "a"  
> **t前綴"a"，t後綴"a"**  
> "aa" | ""  
> t前綴"a"，t後綴""  

發現前後綴配對有可能超過原本t的長度。為了避免這種情況，當前後綴滿足t的長度時，即代表t被完整配對，值接回傳0。  

為了實現上述的切割、前後綴配對，我們可以先預處理每個切割點所配對到的前綴、後綴，分別為pref和suff陣列。pref[i]代表s從0到i為止這部分所配對到t的前綴長度，suff[i]代表s從i到M-1為止所配對到t的後綴長度。  
最後窮舉所有切割點，t的長度N扣掉前後綴長度即為需要刪除的部分，更新答案。  

時間複雜度O(M)，其中M為t的長度。空間複雜度O(M)。  

```python
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        M,N=len(s),len(t)
        
        pref=[0]*M
        cnt=0
        j=0
        for i in range(M):
            if j<N and s[i]==t[j]:
                cnt+=1
                j+=1
            pref[i]=cnt
            
        suff=[0]*(M+1)
        cnt=0
        j=N-1
        for i in reversed(range(M)):
            if j>=0 and s[i]==t[j]:
                cnt+=1
                j-=1
            suff[i]=cnt
            
        ans=N-suff[0] # 前半段為""，右半段為s  
        for i in range(M):
            left=pref[i]
            right=suff[i+1]
            if left+right>=N:
                return 0
            ans=min(ans,N-left-right)
            
        return ans
```
