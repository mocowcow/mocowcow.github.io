---
layout      : single
title       : LeetCode 3145. Find Products of Elements of Big Array
tags        : LeetCode
---
雙週賽 130。又是難題，比賽中連完整做法都想不出來。我猜應該有 2900 分。  

## 題目

一個整數 x 的**強陣列**指的是由二的冪組成，且和為 x 的有序陣列。  
例如 11 的 強陣列是 [1, 2, 8]。  

big_nums 是由無限**遞增**的正整數數列 [1, 2, 3, ...] 的**強陣列**串接組成。  
big_nums 的開頭為 [<u>1</u>, <u>2</u>, <u>1, 2</u>, <u>4</u>, <u>1, 4</u>, <u>2, 4</u>, <u>1, 2, 4</u>, <u>8</u>, ...]。  

輸入二維整數陣列 queries，其中 queries[i] = [from<sub>i</sub>, to<sub>i</sub>, mod<sub>i</sub>]，你必須計算 (big_nums[from<sub>i</sub>] \* big_nums[from<sub>i+1</sub>] \* ... \* big_nums[to<sub>i</sub>]) % mod<sub>i</sub>。

回傳整數陣列 answer，其中 answer[i] 代表第 i 次查詢的答案。  

## 解法

首先注意到 big_nums 的查詢範圍高達 10^15，不可能真的生出整個陣列。  
而區間 [s, e] 的**乘積**等價於 [0, e] 的乘積除 [0, s - 1] 的乘積，有點類似前綴和的關係。  

查詢要對 mod 求餘數，會想到**乘法逆元**。很可惜 mod 不是質數，派不上用場。  

---

仔細看看**強陣列**的定義，都是由**二的冪次**所組成。  
例如：強陣列 [1, 2, 8] 的乘積可以看做 2^0 \* 2^1 \* 2^3，也就是 2^4 = 16。  
如此一來，可以改求 [0, x] 的**冪次和**，再透過前綴和得出 [s, e] 的冪次和 p，答案為 2^p。
但是 p 可能很大，暴力計算會超時，記得使用**快速冪**。  

查詢部分的程式碼大概是這樣。  

```python
def answer(s, e, mod):
    exp = prefix_sum(e) - prefix_sum(s - 1)
    return pow(2, exp, mod)
```

---

再來觀察每個整數是如何構造出**強陣列**：  
> 0 = 0b0000 = 0  
> 1 = 0b0001 = 2^0  
> 2 = 0b0010 = 2^1  
> 3 = 0b0011 = 2^0 + 2^1  
> 4 = 0b0100 = 2^2  
> 5 = 0b0101 = 2^0 + 2^2  
> 6 = 0b0110 = 2^1 + 2^2  
> 7 = 0b0111 = 2^0 + 2^1 + 2^2  
> 8 = 0b1000 = 2^3  

從整數 0 開始看，發現每個位元 (二的 i 次) 都按照某種週期出現。  
像第 0 位元的週期是 2 個數，例如 [0,1], [2,3], [4,5] 為一週期。每個週期前半段的數會是 0，後段才是 1，所以 1, 3, 5, 7,..包含第 0 位元。  
而第 1 位元的週期是 4 個數，例如 [0,1,2,3], [4,5,6,7] 為一週期。所以 2, 3, 6, 7,.. 擁有第 1 個位元。  

整理出規律：第 i 個位元的週期是 2^(i+1)。  
不成完整週期的部分，則只有後半段計入。例如區間 [0, 2] 的第 1 個位元不滿一個週期 (也就是 [0,1,2,3])，但是數字 2 屬於後半週期，所以 2 也會擁有第 1 個位元。  

透過這個規律，我們單獨處理不同位元，直接求出區間 [0, x] 所對應的 big_nums **位元個數**及**冪次和**。  

```python
# bit count and power sum of [0, x]
def count(x): 
    x += 1
    bit_cnt = 0 # size of big_nums
    pow_sum = 0 # 2 ^ pow_sum = big_nums[1] * ... * big_nums[x]
    for i in range(x.bit_length()):
        base = i 
        rep_size = 1 << (i + 1)
        full_rep = x // rep_size
        
        # add full rep
        cnt1 = (rep_size // 2) * full_rep
        bit_cnt += cnt1
        pow_sum += base * cnt1
        
        # add extra bit
        extra = (x % rep_size) - (rep_size // 2)
        if extra > 0:
            bit_cnt += extra
            pow_sum += base * extra
    return bit_cnt, pow_sum
```

---

這時候就有疑問了：啊我要的是 big_nums[0..index]，你搞出一個算 [0, x] 多少位元的函數要幹嘛？  
雖然沒辦法一次定位 big_nums[0..index] 對應的區間 [0, bound] 是多少，但我可以隨便選一個 [0, x] 看他長度夠不夠。  
沒錯，正是**二分搜**。  

透過二分搜搭配 count(x)，找到第一個包含 big_nums[index] 的區間 [0, bound]。  
每個整數至少會提供一個位元，二分上界姑且設為 index。  

```python
# find lower bound of [0, x] that cover big_nums[0..index]
def find_bound(index): 
    lo = 0
    hi = index
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid)[0] < index:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

有了這兩個，就能實現一開始想要的**冪次前綴和**的功能了。  

先拿二分函數找到合適的 bound，然後計算 [0, bound] 所擁有的**位元個數**和**冪次和**。  
[0, bound] 有可能因為最後一個數 bound 所產生的**強陣列**太大，包含太多位元。這時就從 bound 的最高位元往下扣除，直到數量正確為止。  

```python
# power sum of big_nums[0..index]
def prefix_sum(index):
    index += 1
    bound = find_bound(index)
    bit_cnt, pow_sum = count(bound)
    
    # delete extra bit
    i = bound.bit_length() - 1
    while bit_cnt > index:
        if bound & (1 << i):
            bit_cnt -= 1
            pow_sum -= i
        i -= 1
    return pow_sum
```

全部拼起來就大功告成了。  
每次 count(x) 需要 O(log x)；每次二分需要 O(log index) 次 count(index)。  

時間複雜度 O(Q \* (log MX) ^ 2)，其中 Q = len(queries)，MX = index 上限。  
空間複雜度 O(1)，答案空間不計入。  

```python
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        
        # bit count and power sum of [0, x]
        def count(x): 
            x += 1
            bit_cnt = 0 # size of big_nums
            pow_sum = 0 # 2 ^ pow_sum = big_nums[1] * ... * big_nums[x]
            for i in range(x.bit_length()):
                base = i 
                rep_size = 1 << (i + 1)
                full_rep = x // rep_size
                
                # add full rep
                cnt1 = (rep_size // 2) * full_rep
                bit_cnt += cnt1
                pow_sum += base * cnt1
                
                # add extra bit
                extra = (x % rep_size) - (rep_size // 2)
                if extra > 0:
                    bit_cnt += extra
                    pow_sum += base * extra
            return bit_cnt, pow_sum
        
        # find lower bound of [0, x] that cover big_nums[0..index]
        def find_bound(index): 
            lo = 0
            hi = index
            while lo < hi:
                mid = (lo + hi) // 2
                if count(mid)[0] < index:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        # power sum of big_nums[0..index]
        def prefix_sum(index):
            index += 1
            bound = find_bound(index)
            bit_cnt, pow_sum = count(bound)
            
            # delete extra bit
            i = bound.bit_length() - 1
            while bit_cnt > index:
                if bound & (1 << i):
                    bit_cnt -= 1
                    pow_sum -= i
                i -= 1
            return pow_sum
        
        def answer(s, e, mod):
            exp = prefix_sum(e) - prefix_sum(s - 1)
            return pow(2, exp, mod)
        
        return [answer(*q) for q in queries]
```
