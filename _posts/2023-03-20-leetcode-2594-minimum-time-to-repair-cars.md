--- 
layout      : single
title       : LeetCode 2594. Minimum Time to Repair Cars
tags        : LeetCode Medium Array BinarySearch
---
雙周賽100。Q4竟然是Medium，似乎特殊日子就會放水。但我覺得這次Q1比Q4更難。  

# 題目
輸入整數陣列ranks，代表各技師的**排名**。一個排名r的技師修理n台車，需要花費r\*n^2分鐘。  

另外還有整數cars，代表要修理的車子數量。  

求**最少**要幾分鐘才能修完。  

注意：每個技工可以同時作業。  

# 解法
排名越後的技工修車越慢，且車數越多，時間也越久，時間呈現單調上升。  
假設在x分鐘內可以修完車，那麼x+1, x+2...肯定也行，符合二分答案。  

維護一個函數ok(t)，判斷是否能在t分鐘修完所有車子。  
下界為1，因為至少會有一台。上界為10^6\*10^6\*100，因為極端狀況下1個排名100的技工要修10^6台車。  
如果mid分修不完，更新下界為mid+1；否則更新上界為mid。最後下界就是答案。  

最後是ok(t)的實作，遍歷每個技工r，直接將t除4，然後開根號取整數，就是這個技工的修車數，加入cnt計數。如果cnt大於等於cars則代表修得完。  
注意，小數開根號必定不會有整數，所以t除r可以直接取整。而開完根號後的小數也要捨棄掉。  

時間複雜度O(N log (m\*c^2))，其中N為ranks長度，m為min(ranks)，c為cars。空間複雜度O(1)。  

```python
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def ok(t):
            cnt=0
            for r in ranks:
                n=int((t//r)**0.5)
                cnt+=n
            return cnt>=cars
        
        lo=1
        hi=10**14
        while lo<hi:
            mid=(lo+hi)//2
            if not ok(mid):
                lo=mid+1
            else:
                hi=mid
                
        return lo
```

使用內建函數的一行版本。  

```python
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        return bisect_left(range(10**14),True,key=lambda t:sum(int((t//r)**0.5) for r in ranks)>=cars)
```

因為ranks[i]的範圍不大，只有100，但是卻高達10^5個，可見有很多重複元素。  
可以先把ranks依照技工排名r分類，在二分檢查時直接把修車數乘上當前排名r的人數即可。  

時間複雜度O(N + R log (m\*c^2))，其中N為ranks長度，R為獨特的ranks[i]數量，m為min(ranks)，c為cars。空間複雜度O(1)。  

```python
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        d=Counter(ranks)
        
        def ok(t):
            cnt=0
            for r,v in d.items():
                n=int((t//r)**0.5)
                cnt+=n*v
            return cnt>=cars
        
        lo=1
        hi=10**14
        while lo<hi:
            mid=(lo+hi)//2
            if not ok(mid):
                lo=mid+1
            else:
                hi=mid
                
        return lo
```