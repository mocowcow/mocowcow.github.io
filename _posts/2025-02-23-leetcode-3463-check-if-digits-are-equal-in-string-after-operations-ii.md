---
layout      : single
title       : LeetCode 3463. Check If Digits Are Equal in String After Operations II
tags        : LeetCode Hard Math
---
weekly contest 438。  
根本是在上數學課，一大堆神奇定理。  
更神奇的有幾千人都知道這些東西怎麼用。  

還有人氣到在註解開罵，差點笑死：  

> 傻逼题目非要mod10 给个质数会死啊  

## 題目

<https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/description/>

## 解法

合併過程如下：  
> nums = [a, b, c, d]  
> 合併第一次 [ab, bc, cd]  
> 合併第二次 [a2bc, b2cd]  
> 合併第三次 [a3b3cd]  

只看係數：  
> [1, 1, 1, 1]  
> [11, 11, 11]  
> [121, 121]  
> [1331]  

發現有點類似**巴斯卡三角形**，或是**組合數**。  
感覺可以直接推算出某個元素在合併後的係數。  

---

設陣列大小為 N。  
對於 nums = [a, b, c, d] 來說，合併到最後時：  

- a 的係數正好是 comb(3, 0) = 1  
- b 的係數正好是 comb(3, 1) = 3  
- c 的係數正好是 comb(3, 2) = 3  
- d 的係數正好是 comb(3, 3) = 1  

假定 nums[i] 的係數會是 comb(N-1, i)。  

換個例子驗證。  
nums = [a, b, c, d, e]：  

- a 的係數正好是 comb(4, 0) = 1  
- b 的係數正好是 comb(4, 1) = 4  
- c 的係數正好是 comb(4, 2) = 6  
- d 的係數正好是 comb(4, 3) = 4  
- e 的係數正好是 comb(4, 4) = 1  

符合上述猜想。  

---

麻煩的問題來了，s 長度高達 N = 10^5，怎麼算組合數？  
遞推預處理組和需要 O(N^2)，肯定不行。  

回到高中學的公式：  
> comb(n, k) = n! / k!(n-k)!  

預處理 N 個階乘，並用**費馬小定理**算出階乘的**乘法逆元**。  
之後算組合數就是 O(1)。  

但是費馬小定理要求取餘數的 MOD **必須是質數** P。  
本題 MOD = 10 並非質數，所以不適用。  

---

還有另外一種求逆元的方式，叫做**歐拉定理**。  

對於正整數 n，歐拉函數 φ(n) 指的是：  
> 在小於等於 n 的正整數中，與 n 互質的數目  

只要整數 a 與模數 M **互質** (即 gcd(a, M) = 1)，即存在逆元 a^(φ(M)-1)。  

對於本題 MOD = 10，有 φ(10) = 4，因為 [1,3,7,9] 都和 10 互質。  
所以整數 a 的 3 次方就是逆元。  

---

壞消息：MOD = 10 有質因數 2 和 5。  
只要整數 a 是 2 或 5 的倍數，就不可能與 10 互質，所以沒有逆元。  

好消息：質因數只有 2 和 5。  
對於整數 a 來說，只要把他質因數分解，把所有的 2 和 5 提取出來，就和 10 互質了。  

例如：  
> a = 420 = 2 \* 2 \* 3 \*5 \* 7  
> a' = 3 * 7 = 21  
> cnt2(a) = 2, cnt5(a) = 1

a 可以表示成：  
> a = a' \* 2^cnt2(a) \* 5^cnt5(a)  
> a = 21 \* 2^2 \* 5^1  
> a = 420  

算階乘時，提取出 2 和 5，記做 cnt2[i] 和 cnt5[i]。  
提取後的階乘記做 f[i]，這下就能求逆元 f_inv[i] 了。  

算組合數 comb(n, k) 時，先算不含 2 和 5 的階乘：  
> f[n] \* f_inv[k] \* f_inv[n-k]  

然後補回 2 的出現次數：  
> 2^cnt2[n] / (2^cnt2[k] \* 2^cnt[n-k])  
> = 2^(cnt2[n] - cnt2[k] - cnt2[n-k])  

再補回 5 的出現次數：  
> 5^cnt5[n] / (5^cnt5[k] \* 5^cnt[n-k])  
> = 5^(cnt5[n] - cnt5[k] - cnt5[n-k])  

三個部分乘起來就是 MOD 10 之下的組合數了。  

---

最後回到題目本身。  
題目求的是倒數第二列的兩個結果，判斷是否相等。  

相當於 nums[0..N-2] 和 nums[1..N-1] 兩個三角形的最後一列。  
分別計算比較即可。  

預處理時間複雜度 O(MX log MX)，其中 MX = 10^5。  
空間複雜度 O(MX)。  

時間複雜度 O(N log CNT)，其中 CNT 是 cnt2 和 cnt5 的最大值。  
空間複雜度 O(1)。  

```python
MOD = 10
MX = 10 ** 5
f = [0] * (MX + 1)  # factorial[i] without factor 2 and 5
f[0] = 1
f_inv = [0] * (MX + 1)  # inverse of f[i]
f_inv[0] = 1
ps2 = [0] * (MX + 1)  # prefix sum of cnt2[i]
ps5 = [0] * (MX + 1)  # prefix sum of cnt5[i]
for i in range(1, MX + 1):
    x = i
    cnt2 = cnt5 = 0  # extract factor 2 and 5
    while x % 2 == 0:
        x //= 2
        cnt2 += 1
    while x % 5 == 0:
        x //= 5
        cnt5 += 1

    ps2[i] = ps2[i-1] + cnt2
    ps5[i] = ps5[i-1] + cnt5
    f[i] = f[i-1] * x % MOD
    f_inv[i] = f_inv[i-1] * pow(x, 3, MOD) % MOD


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        a = [int(x) for x in s]
        return self.solve(a[:-1]) == self.solve(a[1:])

    def solve(self, a):
        N = len(a)
        res = 0
        for i in range(N):
            # res += comb(N-1, i) * a[i]
            res += self.cnk_mod10(N-1, i) * a[i]
        return res % MOD

    def cnk_mod10(self, n, k):
        # n! / k!(n-k!)
        res = f[n] * f_inv[k] * f_inv[n-k]
        res *= pow(2, ps2[n] - ps2[k] - ps2[n-k])  # put factor 2 back
        res *= pow(5, ps5[n] - ps5[k] - ps5[n-k])  # put factor 5 back
        return res % MOD
```
