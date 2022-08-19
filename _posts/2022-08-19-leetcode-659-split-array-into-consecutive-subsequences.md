--- 
layout      : single
title       : LeetCode 659. Split Array into Consecutive Subsequences
tags        : LeetCode
---
每日題。

# 題目
輸入**非遞減**的整數陣列nums。  
檢查是否能將nums拆分為一個或多個子序列，使其符合以下條件：  
- 每個子序列都是一個連續遞增的序列，且每個整數正好比前一個整數大一  
- 所有子序列的長度至少為3  

如果可以成功拆分，回傳true；否則回傳false。  

# 解法
要組成遞增數列，意味著數字n只能接在n-1的後面才合法。  
又因為要求所有的數列至少長度3以上，所以每次串接都要挑長度最短數列，才能使數列盡可能變長。  

我們要依照結尾數字將數列分組，故使用雜湊表。而分完組的數列又要依長度排序，所以使用heap。  
遍歷nums中所有數字n，找找看有沒有以n-1結尾的數列，若有則挑選最短的進行串接；否則產生長度為一的新數列[n]。  
最後檢查所有不同數字結尾的分組，若發現有數列長度不足3則回傳false。  

數字範圍從-1000\~1000，共兩千個。建立數列的複雜度為O(N log N)，最後檢查長度為O(2000)，整體為O(N log N)。  

```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        end_with=defaultdict(list)
        
        for n in nums:
            if not end_with[n-1]:
                size=0
            else:
                size=heappop(end_with[n-1])
            heappush(end_with[n],size+1)
            
        for h in end_with.values():
            if h and h[0]<3:return False
            
        return True
```

結果竟然有O(N)的方法，想了一段時間還是不太能完全理解怎麼想到這種魔法。  

首先用雜湊表free紀錄各數字的出現次數，因為我們在遍歷的過程中需要向後方**預借**數字來組成新數列。  
另外用雜湊表end_with來紀錄各數字結尾的數列個數。  

遍歷nums中所有數字n，同樣先找有沒有n-1結尾的數列，若有則隨便挑一個串接上；否則檢查後方是否有剩餘的n+1和n+2可用，用來組成新的長度三數列[n,n+1,n+2]；若無法組成則代表拆分失敗，回傳false。  

需要注意的是：要優先考慮串接現有的數列，而非建立新的數列。  
考慮以下情況：  
> nums = [1,2,3,4,5,5,6,7]  
> seq = [[1,2,3]], n = 4  
> 這時若建立新的數列[4,5,6]會剩下5,7無法使用  
> 故優先將4接在[1,2,3]後  
> 正確切分為[1,2,3,4,5],[5,6,7]  

```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        free=Counter(nums)
        end_with=Counter()
        
        for n in nums:
            if free[n]==0:continue
            free[n]-=1
            
            if end_with[n-1]:
                end_with[n-1]-=1
                end_with[n]+=1
            elif free[n+1] and free[n+2]:
                end_with[n+2]+=1
                free[n+1]-=1
                free[n+2]-=1
            else:
                return False
            
        return True        
```