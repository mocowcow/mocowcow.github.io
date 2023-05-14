--- 
layout      : single
title       : LeetCode 2682. Find the Losers of the Circular Game
tags        : LeetCode Easy Array Simulation
---
周賽345。題目好長，比賽中看到快吐，寫題解也打到手好痠。  

# 題目
有n個朋友一起玩遊戲，他們圍成一圈，並依照順時鐘方向分別編號為1\~n。  

遊戲規則如下：  
最初由1號朋友接球。  
- 然後，1號朋友將球交給順時鐘距離k的朋友  
- 然後，接球的朋友將球交給順時鐘距離2k的朋友  
- 然後，接球的朋友將球交給順時鐘距離3k的朋友，依此類推  

也就是說，在第i輪拿到球的人，必須要將球交給順時鐘距離i*\k步的人。  

當有人拿到球第二次時，遊戲結束。  
沒有拿過球的人稱為**輸家**。  

輸入整數n和k，依**升序排序**回傳所有輸家。  

# 解法
雖然題目是由1\~n編號，但是這樣模運算處理很麻煩。所以先以0\~n-1處理，建構答案時後再補上1。  

維護陣列cnt記錄拿球次數，以及當前拿球的人i，還有下次要傳球的距離step。  
持續傳球，直到有人拿到第二次，跳出迴圈並構造答案。否則標記i拿過球，傳遞step步後使step遞增k。  

最差情況下每個人都拿到一次球，時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt=[0]*n
        i=0
        step=k
        while True:
            if cnt[i]==1:
                break
            cnt[i]=1
            i=(i+step)%n
            step+=k
            
        loser=[]
        for i in range(n):
            if cnt[i]==0:
                loser.append(i+1)
                
        return loser
```
