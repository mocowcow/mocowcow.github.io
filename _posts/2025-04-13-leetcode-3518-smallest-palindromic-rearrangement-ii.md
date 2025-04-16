---
layout      : single
title       : LeetCode 3518. Smallest Palindromic Rearrangement II
tags        : LeetCode Hard Math
---
weekly contest 445。  
以前總是抱怨 python 卡常數打比賽沒優勢，原來其實在暴力排列組合有巨大優勢，只是我不敢用。  
本周兩場真的在大數上吃了不少甜頭。  

## 題目

<https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/>

## 解法

和前一題一樣，回文串只需要處理其中一半。  
問題簡化成左半邊字串 half 第 k 小的**不同的**排列。  

相似題 [3470. permutations iv]({% post_url 2025-03-12-leetcode-3470-permutations-iv %})。  

---

設 half 長度為 sz，則全排列有 sz! 種。  
但題目要求的是**不同的**排列，所以對於每種元素都要去重。  
若對於 c 總共出現 v 次，則要除以 v! 種重複排列。  

若去重後的總排列數 tot 不足 k，沒有答案，直接回傳空字串。  

---

接著從小到到枚舉要填的元素。  
設當前填第 i 位，剩餘排列數有 rem_ways 種。  
如果填了字元 c，則分子會少乘一個 (sz-i)，分母會多乘一個 cnt[c]。  
代表由 c 開頭的共有 ways = rem_ways \* cnt[c] / (sz-i) 種排列。  

如果 k <= ways，則代表第 k 小的選法包含在這組內。答案填入 c，更新 c 的剩餘數量與剩餘排列數。  
否則 k > ways 代表 k 不屬於這組。直接從 k 中排除掉 ways 個更小的排法。  

最後填完把左半邊翻轉，並加上中心元素即可。  

---

也不知道是測資太弱，還是出題者允許大數運算，我換了 go 也是可以過。  

至於複雜度就很尷尬。  
至多 D = 26 種字元，有 N 個位置，每次試填需枚舉 D 個字元。
如果把大數運算看做 O(1)，那硬要說整體是 O(N \* D) 好像也不能說不對。  

```python
f = cache(factorial)

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        N = len(s)
        half = s[:N//2]
        mid = "" if N % 2 == 0 else s[N//2]
        sz = len(half)

        tot = f(sz)
        cnt = Counter(half)
        for v in cnt.values():
            tot //= f(v)

        # 排列數不足
        if tot < k:
            return ""

        rem_ways = tot
        ans = []
        for i in range(sz):
            for c in ascii_lowercase:
                if cnt[c] == 0:
                    continue
                ways = rem_ways*cnt[c]//(sz-i)
                if k <= ways:
                    ans.append(c)
                    rem_ways = ways
                    cnt[c] -= 1
                    break
                k -= ways

        pre = "".join(ans)

        return pre + mid + pre[::-1]
```

那如果不用大數，有什麼辦法不溢位又能算出正確的排法？  

當初在做 3470 題，只要排列數超過 MXK 就直接停止，後面的不需要繼續算，反正已經知道答案要填什麼。  
但是這種**不盡相異物排列**扣除各元素重複排法，必須要先算完分子才能算分母，可能中途就溢位了。  
> "aabbc" 的排法  
> 5! / (2!2!1!)  
> = 30 種排法  

改從組合的角度來看，往空格中逐次填入不同元素：  
> "#####" 最初 5 個空格  
> 在 5 格中選 2 格填 a。剩 3 格
> 在 3 格中選 2 格填 b。剩 1 格  
> 在 1 格中選 1 格填 c。剩 0 格  
> 共有 comb(5,2) \* comb(3,2) \* comb(1,1)  
> = 30 種選法  

兩種方式其實是等價的。  
如此一來，每次試填只需要算 D 個組合數相乘，只要一達到 MXK 就馬上中止。  

---

注意：下述 k 是指組合數取 k 個物品，與題目給定的第 k 小排法無關。  
MXK 才是第 k 小排法的上限。  

對於組合數來說，comb(n,k) 等價於 comb(n,n-k)。  
取 k = min(k,n-k)，保證 k <= n-k。  

但是組合數同樣也是要先算分子，然後才扣掉分母。  
> comb(n,k) = n! / (k!(n-k)!)  

例如：  
> comb(5,2) = 5! / (2!3!)  
> 階乘展開後  
> 分子 = 5 4 3 2 1  
> 分母 = 2 1 3 2 1

剛好分子和分母的後 n-k 項可以消掉，實際上剩下 k 項：  
> 分子 = 5 4
> 分母 = 2 1  

簡單來說，因為每 x 個數會出現一個 x 的倍數，若以分子遞減、分母遞增的順序計算，可以保證乘積一定能被分母整除。  
> 5 4 3 有 3 個數，其中 5 是 1 的倍數、4 是 2 的倍數、3 是 3 的倍數  
> 所以 (5/1) \* (4/2) \* (3/3) 肯定能整除  

又因為先前取了 k = min(k, n-k)，保證不會出現配對的分子小於分母的情形，所以乘積肯定是遞增的，在計算途中乘積達 MXK 可以安全中止。  
並且因為每次乘上的 (分子/分母) 不為 1，只需要 O(log MXK) 次計算，而不需跑滿 O(k) 次循環。  

---

共需要 N 次試填，每次試填要算 D 次組合數，每次組合數複雜度 log MXK。  

時間複雜度 O(N \* D \* log MXK)。  
空間複雜度 O(N + D)。  

```python
def get_comb(n, k):
    k = min(k, n-k)
    res = 1
    for i in range(1, k+1):
        res *= n-i+1  # from n to n-k+1
        res //= i  # from 1 to k
        if res >= MXK:
            return MXK
    return res 

def get_ways(cnt):
    ways = 1
    space = sum(cnt.values())
    for v in cnt.values():
        ways *= get_comb(space, v)
        space -= v
        if ways >= MXK:
            return MXK
    return ways

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        N = len(s)
        half = s[:N//2]
        mid = "" if N % 2 == 0 else s[N//2]
        sz = len(half)
        cnt = Counter(half)

        # 排列數不足
        if get_ways(cnt) < k:
            return ""

        ans = []
        for _ in range(sz):
            for c in ascii_lowercase:
                if cnt[c] == 0:
                    continue
                cnt[c] -= 1
                ways = get_ways(cnt)
                if k <= ways:
                    ans.append(c)
                    break
                cnt[c] += 1
                k -= ways

        pre = "".join(ans)

        return pre + mid + pre[::-1]
```
