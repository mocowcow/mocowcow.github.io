--- 
layout      : single
title       : LeetCode 3. Longest Substring Without Repeating Characters
tags        : LeetCode Medium String HashTable SlidingWindow
---
每日題。難得出現這麼前面的題號。

# 題目
輸入字符s，找出**不含重複字元**的最長子字串長度。  

# 解法
子字串必須是一個連續的範圍，我們可以想像有一個矩形從s[0]開始向右拓展，而碰到重複字元時收縮左邊界，直到字元不重複為止。  

為了要計算各字元的出現次數，可以使用雜湊表，每當加入新的字元c時，則將其計數+1。  
列舉每個字元c以及其所引位置right作為右邊界，將c加入子字串中。有可能以前就有出現過c，那麼就要縮減左邊界，直到把舊的c彈出為止。  
左邊界和右邊界調整固定後，以當前的大小更新最大長度。因為每個字元最多只會存取到兩次，時間複雜度是O(N)。  

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ctr=Counter()
        left=0
        ans=0
        for right,c in enumerate(s):
            ctr[c]+=1
            while ctr[c]>1:
                ctr[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
            
        return ans
```

再仔細想想，我們每次加入新的字元c之後，有可能出現重複的字元當然也是c，而且c的總數也只可能是2。那麼直接將左邊界收縮到c的上次出現位置之後不是更快？  

使用雜湊表last紀錄每個字元的上次出現位置，每次加入新字元c時，如果c以前有出現過，且正好在[left,right]之間，那麼則將做邊界left更新為c最後的出現位置後一格，剛好可以排除掉c。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last={}
        ans=0
        left=0
        for right,c in enumerate(s):
            if c in last:
                left=max(left,last[c]+1)
            last[c]=right
            ans=max(ans,right-left+1)
            
        return ans
```
