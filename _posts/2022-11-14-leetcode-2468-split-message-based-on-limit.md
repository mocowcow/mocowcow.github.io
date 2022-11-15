--- 
layout      : single
title       : LeetCode 2468. Split Message Based on Limit
tags        : LeetCode Hard Array String PrefixSum
---
雙周賽91。比賽時覺得是二分法，但是寫著怪怪的又轉回去窮舉，可惜時間不夠沒寫出來。  

# 題目
輸入一個字串message和一個正整數limit。  

你必需根據limit將message拆分為一個或多個**部分**。每個部分都要帶有後綴"<a/b>"其中"b"為部分的總數，而"a"為該部分的編號，從1開始遞增到b為止。除了最後一個部分之外，每個加上後綴的部分的長度必須等於limit。  

這些加上後綴的**部分**，去掉後綴再連接起來必須等於message，且拆分出的部分總數越少越好。  

求拆分為多個**部分**後的**字串陣列**，若無法拆分則回傳空陣列。  

# 解法
每個長度為part的部分，其後墜可以分成兩個部分：  
- 固定的</>符號加上分母part  
- 由1\~part的分子  

分母和符號的部分可以直接由分母轉成字串後的長度帶入公式求出。而分子就比較麻煩，本來想對個十百千位分別計算數量，後來想到一個更好的方法：前綴和。不管分母為何，分子的長度永遠是固定的，透過預計算所有分子長度加上前綴和，可以在O(1)時間內得到N項分母的長度總和。  

現在我們可以在常數時間內得到拆成part個部分的符號所佔據的長度了，又因為每個部分至少要有包含一個來自message的符號，所以總長度limit\*part = total扣掉符號長度token後，至少要有剩餘N個空位來放message。若符合則直接組成字串陣列回傳；否則在最後回傳空陣列。  

message長度為N，每次將整數轉成字串為O(log N)，預計算分子前綴和時間O(N log N)，空間O(N)。每次使用計算part字數為O(1)+O(log N)，part數不可能超過N，故最多計算N次，時間複雜度O(N log N)，不計算答案輸出的空間複雜度O(1)。  
整體時間O(N log N)，空間O(N)。如果改在窮舉過程中才計算前綴和，可以把空間壓到O(1)。  

```python
psum=[0]*100005
for i in range(1,100005):
    psum[i]=psum[i-1]+len(str(i))

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        N=len(message)
        
        for part in range(1,N+1):
            total=limit*part
            token=psum[part]+(len(str(part))+3)*part
            
            if total-token>=N:
                ans=[]
                idx=0
                x=1
                while idx<N:
                    suffix=f"<{x}/{part}>"
                    size=limit-len(suffix)
                    t=message[idx:idx+size]+suffix
                    idx+=size
                    x+=1
                    ans.append(t)
                return ans
        
        return []
```
