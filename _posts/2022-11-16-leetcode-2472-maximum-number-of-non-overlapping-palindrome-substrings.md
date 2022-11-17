--- 
layout      : single
title       : LeetCode 2472. Maximum Number of Non-overlapping Palindrome Substrings
tags        : LeetCode Hard Array String Greedy DP TwoPointers DFS
---
周賽319。說到palindrome八九不離十就是dp，我愛回文，回文愛我。  

# 題目
輸入字串s和正整數k。  

從字串s中找出一組滿足以下條件，且**不重疊**的子字串：  
- 子字串長度至少為k  
- 子字串必須是**回文**字串  

求最多可以同時找到**多少回文子字串**。  

# 解法
首先要建立記錄下子字串是否為回文，可以從[5. longest palindromic substring]({% post_url 2022-03-14-leetcode-5-longest-palindromic-substring %})裡面任選一種方法。這次我選擇的是top down的dp，因為寫起來最快。  

能夠快速查找某段子字串是否回文後，要怎麼找出不重疊的回文才是重點。  
我們先試想以下情況：  
> s = "aabcb", k = 1  
> 選了"aa"做回文，剩下s = "bcb"，可以再選擇"bcb"做回文  
> 選了"a"做回文，剩下s = "abcb"，一樣可以選"bcb"做回文  

由此可以推論出從同一個索引l開始，若以索引r為右邊界能夠找到符合條件的子字串，一定不會比r+1為右邊界得到更差的結果。  
開始貪心法找答案，定義dfs(i)代表由s[i:]中最多能夠同時存在幾個回文。只要i大於等於N，代表沒有剩餘的字元可以使用，回傳0。否則由i\~N-1窮舉右邊界r，每個右邊界由r\~i窮舉左邊界l，只要找到長度至少為k且回文的子字串，就直接以r+1為出發點，繼續dfs。  

dp計算回文時空間皆為O(N^2)，而dfs的部分是最差情況也是窮舉N^2個子字串，所以整體時空間都是O(N^2)。  

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        N=len(s)
        
        @cache
        def pa(i,j):
            if i>=j:return True
            return s[i]==s[j] and pa(i+1,j-1)
        
        def dfs(i):
            if i>=N:return 0
            for r in range(i,N):
                for l in reversed(range(i,r+1)):
                    if r-l+1>=k and pa(l,r):
                        return 1+dfs(r+1)
            return 0
        
        return dfs(0)
```

再來是中心擴展法找回文，再用dp求最大回文數。  

中心擴展法是窮舉每個索引i作為回文字串的中心，不斷向兩端增加子字串，直到子字串不是回文為止。但是回文的中心可能是一或二個字元，例如"abba"和"aba"，所以每個中心都要分別處理兩種情形。  

定義dp[i]：子字串s[:i]的最大回文數量。  
轉移方程式：dp[i]=max(dp[j] FOR ALL 0<=j<i)  
base case：f[0]為空字串，不特別處理。  

和原版中心擴展不同的是：我們一旦找到滿足k的回傳子字串，便立即停止擴張，所以實際上最多只會k/2次。  
窮舉了N個中心點，各擴張k次，時間複雜度O(Nk)，空間複雜度O(N)。  

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        N=len(s)
        dp=[0]*(N+1)
        
        for i in range(N):
            dp[i+1]=max(dp[i+1],dp[i])
            l=r=i
            while l>=0 and r<N and s[l]==s[r]:
                if r-l+1>=k:
                    dp[r+1]=max(dp[r+1],dp[l]+1)
                    break
                l,r=l-1,r+1
            l,r=i,i+1
            while l>=0 and r<N and s[l]==s[r]:
                if r-l+1>=k:
                    dp[r+1]=max(dp[r+1],dp[l]+1)
                    break
                l,r=l-1,r+1
                
        return dp[-1]
```