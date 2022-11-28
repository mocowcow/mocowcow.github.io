--- 
layout      : single
title       : LeetCode 2483. Minimum Penalty for a Shop
tags        : LeetCode Medium Array String PrefixSum Greedy
---
雙周賽92。這題和我的相性不太好，長度N的陣列對應到N+1種選擇，花了一點時間才想通。  
再加上字元的"N"和我用來計算輸入常數的N衝突，想變數名稱卡好久，最後選了小寫n, y來計算字元"N", "Y"感覺很不舒服。  

# 題目
輸入由Y和N組成的字串customers，代表商店的來客紀錄：  
- 如果customers[i]為Y，則代表第i小時有客人  
- 反之，若為N，則代表第i小時沒客人  

商店可以在第0\<=j<=n小時之中選擇任一時間點打烊，並計算**懲罰值**：  
- 對於每個小時，如果商店營業中，但卻沒來客，懲罰+1  
- 對於每個小時，如果商店已打烊，但卻有來客，懲罰+1  

求商店可以得到**最小懲罰值**，且**最早**打烊的時間點j。  

注意：在第j小時打烊，代表從包含j之後的所有時間都是關門狀態。  

# 解法
對於每個時間j來說，若關門，懲罰為j之前的N總數+j之後(含)的Y總數，所以要先計算懲罰值後才對NY做增減。  
因為剩餘的Y和已知的N都呈現單調增減，所以可以用前綴和來維護其數量。若當前時間j的懲罰值低於最低值，則更新答案。  

處理完customers陣列後，記得還要處理第N小時，也就是完全不關門，**懲罰值=已知N總數**的情況。  

總共需要遍歷陣列兩次，時間O(N)，空間O(1)。  

```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N=len(customers)
        y=customers.count("Y")
        n=0
        mn=inf
        ans=None

        for i,c in enumerate(customers):
            penal=n+y
            if penal<mn:
                mn=penal
                ans=i
            if c=="Y":
                y-=1
            else:
                n+=1
            
        if n<mn:
            mn=n
            ans=N
            
        return ans
```
