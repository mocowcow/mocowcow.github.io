---
layout      : single
title       : LeetCode 2193. Minimum Number of Moves to Make Palindrome
tags 		: LeetCode Hard Greedy TwoPointers
---
雙周賽73。一直想不到怎麼處理奇數字元，比賽結束後馬上看到別人的正確方法，自己修改後成功AC，也算是睡前的安慰吧。

# 題目
字串s，每次可以將任意兩個相鄰的字元交換位置，求最少需要幾次交換可以將s變成回文字串。

# 解法
很直覺知道回文一定要用到雙指標，左右邊往內夾，若碰到字元不同就開始交換。  
先決定移動左半邊的字串，來和右半邊達到平衡。  
當s[left]!=s[right]時，指標ll為預訂和left交換的位置，將ll不斷右移直到s[ll]與s[right]相同後停止。若ll小於right則代表該字元確實有剩餘兩個以上，將ll左移至left後，左右指標內縮一步，繼續處理下一批字元；但如果該字元只剩下一個，理當是要擺正中間去，比賽時我一直想著要先把他移到中間去，試著不少次都沒成功。後來看到[這篇文](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/discuss/1821967/Python-2-solutions%3A-O(n2)-and-O(n-log-n)-explained)才知道原來只需要把那個奇數字元先往中間靠一步，左右指標不變，再次處理即可，如此一來該奇數字元最後依然會跑到中間去。

```python
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        N = len(s)
        s = list(s)

        def shift(left, ll):
            while left < ll:
                s[ll-1], s[ll] = s[ll], s[ll-1]
                ll -= 1

        step = 0
        left = 0
        right = N-1

        while left < right:
            ll = 0
            if s[left] != s[right]:
                ll = left+1
                while s[ll] != s[right]:
                    ll += 1
                if ll == right:
                    step += 1
                    shift(right-1, right)
                else:
                    step += ll-left
                    shift(left, ll)
            else:
                left += 1
                right -= 1

        return step
```

2022/3/8更新list版解法。  

```python
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        li = list(s)
        step = 0
        while len(li) > 1:
            if li[0] == li[-1]:
                li = li[1:-1]
            else:
                idx = 1
                t = 1
                while li[idx] != li[-1]:
                    idx += 1
                    t += 1
                if idx == len(li)-1:
                    li[-1], li[-2] = li[-2], li[-1]
                    step += 1
                else:
                    step += t
                    li = li[:idx]+li[idx+1:-1]

        return step

```