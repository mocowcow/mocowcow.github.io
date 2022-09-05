--- 
layout      : single
title       : LeetCode 2397. Maximum Rows Covered by Columns
tags        : LeetCode Medium Array Matrix Backtracking HashTable BitManipulation Bitmask
---
雙周賽86。這題目描述真的超級爛，看半天才搞懂意思。除此之外本身倒是沒什麼難度。  

# 題目
輸入m\*n的二進制矩陣mat和一個整數cols，代表你必須選擇其中cols個不同的行數。  
對於第r列來說，其中所有值為1的行數都有被選中，則稱這列**被覆蓋**。  

求選擇cols行的形況下，**最多可以覆蓋多少列**。  

# 解法
列數m和行數n最大都只有到12，回溯法生成所有選擇cols行的組合，複雜度為O(12!)，還算可行。  
檢查m列是否被覆蓋，每檢查一列的複雜度為行數，也就是O(n)，總共是O(m\*n)。  
複雜度上限為O(12!\*12\*12)，但其實需要檢查到的組合也沒這麼多，實際上應該差不多O(n!)。  

維護一個函數bt做回溯，從所有行數中挑cols後，使用檢查函數check來確認各列是否被覆蓋。統計覆蓋列數cnt後更新答案。  
這裡使用到set來保存被選擇的行數，所以check函數只要確保值為1的列數存在於列數集合中。  

```python
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        M,N=len(mat),len(mat[0])
        ans=0
        
        def check(row,chosen):
            for i,n in enumerate(row):
                if n==1 and i not in chosen:return False
            return True
        
        def bt(i,chosen):
            nonlocal ans
            if i==N:
                if len(chosen)==cols:
                    cnt=0
                    for row in mat:
                        if check(row,chosen):cnt+=1
                    ans=max(ans,cnt)
                return 
            bt(i+1,chosen)
            chosen.add(i)
            bt(i+1,chosen)
            chosen.remove(i)

        bt(0,set())
        
        return ans
```

另外一種思考方向，是**每個行選或不選**的組合，這時候就可以用到bitmask，若某行被選中則將其對應的位元設為1。  
N個行可以產生2^N種組合，複雜度O(2^N)。  
同時也需要各列轉換為bitmask，複雜度為O(M\*N)。  

之後遍歷所有選擇行數的組合comb，只處理**正好cols行的**的選法：  
- 找出被覆蓋的row，若row的所有1位元都被選到，則row與comb做AND運算會保持原值  
- 以被覆蓋的列數，更新答案  

對於每個組合需要檢查M列，每次複雜度O(1)。整體複雜度為O(M\*2^N)。  

```python
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        M,N=len(mat),len(mat[0])
        ans=0
        
        rows=[]
        for row in mat:
            mask=0
            for i,n in enumerate(row):
                if n==1:mask|=(1<<i)
            rows.append(mask)
            
        # 0 ~ (i<<N)-1, total 2^N combs
        for comb in range(1<<N): 
            # if comb.bit_count()==cols:
            if bin(comb).count('1')==cols:
                cnt=0
                for row in rows:
                    if row&comb==row:cnt+=1
                ans=max(ans,cnt)    
                    
        return ans
```