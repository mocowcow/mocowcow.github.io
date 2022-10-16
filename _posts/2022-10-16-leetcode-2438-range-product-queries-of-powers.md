--- 
layout      : single
title       : LeetCode 2438. Range Product Queries of Powers
tags        : LeetCode Medium Array BitManipulation PrefixSum
---
雙周賽89。在生成powers的部分卡了一下子，這種描述方式還真有意思，出題也是種藝術。  
可惜我被10^9+7騙一個WA。    

# 題目
輸入正整數n。有個陣列powers，其總和為n，且以**最小限度**的**2的次方數**所組成。powers陣列以非遞減排序，且保證只有一種組成方式。  

還有一個2D整數陣列querie，其中queries[i] = [left<sub>i</sub>, right<sub>i</sub>]。每個queries[i]代表一次查詢，你必須算出所有powers[j]的乘積，其中left<sub>i</sub> <= j <= right<sub>i</sub>。  

回傳一個和queries長度相等的陣列answer，其中answers[i]是第i個查詢的答案。由於查詢的答案可能很大，每個answers[i]要先模10^9+7。  

# 解法
一開始想不通要怎麼找powers，差點要用回溯法來暴搜找組合方式。好險及時想通，整數n的二進位表示，不就正好對應到某些**2的次方數**嗎？  
因為powers是非遞減，所以從n的LSB開始檢查，若為1 bit則將對應的整數加入powers中。  

queries的部分就很簡單，只是變形的前綴和。先對power做乘法的前綴和ps，每次查詢只要拿0\~right的乘積，除0\~left-1的乘積，就可以得到left\~right的乘積。  

```python
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        pw=[]
        MOD=10**9+7
        
        for i in range(30):
            if (1<<i)&n:
                pw.append((1<<i))
                
        ps=[1]
        for n in pw:
            ps.append(n*ps[-1])
            
        ans=[]
        for l,r in queries:
            x=ps[r+1]//ps[l]
            ans.append(x%MOD)
            
        return ans
```
