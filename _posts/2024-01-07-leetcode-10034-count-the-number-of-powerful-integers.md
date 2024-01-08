---
layout      : single
title       : LeetCode 10034. Count the Number of Powerful Integers
tags        : LeetCode Hard String DP
---
雙周賽121。一眼就知道是數位dp。可惜我被那個 limit 搞死，這場周賽真的和我不合。  

## 題目

輸入三個整數 start, finish 和 limit。還有一個**正**整數字串 s。  

若一個正整數 x 以 s 結尾 (s 是 x 的後綴)，且 x 中的每個數位都不超過 limit，則稱為**強大的**。  

求區間 [start, finish] 中有多少**強大的**數字。  

## 解法

s剛好和我習慣的變數名重疊，以下將輸入的後綴s稱作suff。  

根據排容原理，先求出 f(finish)的合法數，再扣掉 f(start-1)的合法數就是答案。  

---

和大部分的數位dp 相同，先將上限值轉成長度 N 的字串 s，並枚舉第 s[i]要選哪個數字。  
需要維護狀態變數 is_limit，表示當前第i位的選擇是否受限於 s[i]。  
測資保證了 suff 沒有**前導零**，因此不管怎樣最後都是正整數，不需要 is_num 這個狀態變數。  
定義 dp(i,is_limit)：當前是否受限於 s，且索引 i 之後的數字有多少填法能夠滿足 limit 以及 suff 的限制。  

---

不同的是，一般來說選填的數字上限 up 只會受限於 s[i]，這邊額外給了一個 limit 的限制。  
因此在枚舉選哪個數字時，超過 limit 就該停止。  

注意：不能直接 up 和 limit 取最小值！！  
不能直接 up 和 limit 取最小值！！  
不能直接 up 和 limit 取最小值！！

很重要所以要講三次。  
我因為這個地方卡了好久好久都找不出問題，最後看了大神的[題解](https://www.bilibili.com/video/BV1Fg4y1Q7wv)才領恍然大悟。  

舉個例子：  
> s = "51..", limit = 3, prefix = ".."  
> i = 0 且 is_limit = True  
> 受限於 s[i] = 5 ，只能選填 1\~5。同時受限於 limit = 3  

如果直接讓 up 取 min(s[i], limit)，則 up 變成 3。  
這時候選了3，會造成之後dp(i+1)維持 is_limit = True，那麼 i+1 又會受限於 s[i+1]。  
這是不對的！因為之前選了 3，那麼不管是 30\~39 全部小於 51，現在卻只能枚舉 30\~31，恭喜答錯。  

這題帶給我的最大收穫：**上界 up 是維護 is_limit 的重要參考**，不要亂動。  

---

搞定了 limit 之後，還必須滿足後綴 suff 的限制。  

做數位dp 時，s 有 N 個數字要填。而後綴 suff 的長度是 M，則最後的 M 個數字都必須填得跟 suff 相同。  
因此索引是 0 <= i < N-M 的前半段可以根據 num 和 limit 的限制選填，後半段的 N-M <= i < N 都是 suff。  
直接空想有點複雜，列出索引範圍會清晰許多：  

- 共 N 位數  
- 後綴佔 M 位，索引範圍 [0, N-M-1]  
- 前綴佔 N-M 位，索引範圍 [N-M, N]  

前綴占了 N-M位，所以當第 i 位是後綴時，對應的後綴索引 suff_idx = i-(N-M)。  
記得後綴沒有前導零，我們只需要確保 s[i] 同時小於 limit 和 up 即可。  

時間複雜度 O(N \* D)，D = 10 種數字，N 為 finish 轉成字串的長度。  
空間複雜度 O(N)。  

```python
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suff: str) -> int:
        M=len(suff)
        
        def f(num):
            s=str(num)
            N=len(s)
            suff_from=N-M
            
            if N<M:
                return 0

            @cache
            def dp(i,is_limit):
                if i==N:
                    return 1 
                
                up=int(s[i]) if is_limit else 9
                down=0 
                ans=0
                if i>=suff_from: # must be suff
                    suff_idx=i-suff_from
                    j=int(suff[suff_idx])
                    if j<=min(up,limit):
                        new_limit=is_limit and j==up
                        ans=dp(i+1,new_limit)
                else:
                    for j in range(down,min(up,limit)+1):
                        new_limit=is_limit and j==up
                        ans+=dp(i+1,new_limit)
                return ans
            return dp(0,True)

        ans=f(finish)-f(start-1)
        
        return ans
```
