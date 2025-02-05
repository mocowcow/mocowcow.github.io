---
layout      : single
title       : LeetCode 3445. Maximum Difference Between Even and Odd Frequency II
tags        : LeetCode Hard PrefixSum SlidingWindow TwoPointers Greedy
---
weekly contest 435。  

## 題目

<https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/>

## 解法

會用到以下兩題的技巧，建議先做過原題再來：  

[1371. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)。  
前綴內元素的狀態表示法。  

[2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/)。  
如何在限制下更新可用的前綴。  

---

設 a, b 分別為子陣列出現奇數與偶數次的元素。碰到 a 對答案貢獻 1；碰到 b 對答案貢獻 -1；其餘元素不影響。
問題轉換成**最大子陣列和**。  

但還有三個額外限制：  

- a, b 至少都出現一次。  
- 子陣列長度至少 k。  
- a 出現奇數次，b 出現偶數次。  

---

求最大子陣列和，原本是枚舉右端點 i，並以前綴和 ps[i+1] 減去最小的 ps[j]。  
但本題限制 a, b 數量，所以前綴必須分開獨立計算。  

定義 ps[i+1][j]：前綴 s[..i] 中元素 j 的個數。  
當奇偶元素為 a, b 時，整個前綴的和變成 ps[i+1][a] - ps[i+1][b]。  
要減去的變成 ps[j+1][a] - ps[j+1][b]。  

j 的初始值是 -1，代表空陣列。  
只有在 ps[i+1][a] > ps[j+1][a] 時才能保證刪掉前綴後，子陣列中至少有一個 a；  
同理，在 ps[i+1][b] > ps[j+1][b] 保證只少有一個 b。  
如此便滿足第一個限制。  

第二個限制也很簡單，若刪除前綴 s[..j] 之後，剩下的子陣列就是 s[j+1..i]。  
保證這段長度至少 k 才更新前綴，即 i-(j+1)+1 >= k。  

---

最後一項限制 a 要奇數，b 要偶數。做法和 1371 相同。  

分類討論 a 的情況：  

- 若 ps[i+1][a] 為偶數，則 ps[j+1][a] 必須也是偶數。  
- 若 ps[i+1][a] 為奇數，則 ps[j+1][a] 也必須是奇數。  

分類討論 b 的情況：

- 若 ps[i+1][b] 為偶數，則 ps[j+1][b] 必須是奇數。  
- 若 ps[i+1][b] 為奇數，則 ps[j+1][b] 必須是偶數。  

a, b 奇偶性 pa/pb 共有 00/01/10/11 四種狀態。  
以 pre[pa][pb] 分別按照限制一、二去更新即可。  

時間複雜度 O(N \* MX^2)，其中 MX 為 s 中不同元素個數。  
空間複雜度 O(N \* MX)。  

```python
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        N = len(s)
        s = [ord(c) - ord("0") for c in s]

        # prefix sum for each char
        ps = [[0] * 5 for _ in range(N + 1)]
        for i in range(N):
            for j in range(5):
                ps[i+1][j] = ps[i][j] + int(s[i] == j)

        ans = -inf
        # enum odd freq char a
        # and even freq char b
        for a in range(5):
            for b in range(5):
                # find max subarray s[j..i]
                # = (ps[i+1][a] - ps[j][a]) - (ps[i+1][b] - ps[j][b])
                # = (ps[i+1][a] - ps[i+1][b]) - (ps[j][a] - ps[j][b])

                # maitain min (ps[j][a] - ps[j][b])
                # pre[pa][pb]
                # pa 0/1 = parity of a
                # pb 0/1 = parity of b
                pre = [[inf, inf], [inf, inf]]

                # count max subarray end with i
                j = -1
                for i in range(N):
                    cnta = ps[i+1][a]
                    cntb = ps[i+1][b]

                    # apply valid prefix s[..j]
                    # ensure [j+1..i] at least size k
                    while i-(j+1)+1 >= k and cnta > ps[j+1][a] and cntb > ps[j+1][b]:
                        pa = ps[j+1][a] % 2
                        pb = ps[j+1][b] % 2
                        pre[pa][pb] = min(pre[pa][pb], ps[j+1][a] - ps[j+1][b])
                        j += 1

                    # update answer and
                    # parity of a in prefix is NOT pa
                    # parity of b in prefix is pb
                    pa = cnta % 2
                    pb = cntb % 2
                    curr = cnta - cntb
                    ans = max(ans, curr - pre[pa ^ 1][pb])

        return ans
```
