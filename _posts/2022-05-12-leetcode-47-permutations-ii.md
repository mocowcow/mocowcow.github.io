--- 
layout      : single
title       : LeetCode 47. Permutations II
tags        : LeetCode Medium Array Backtracking HashTable
---
每日題。突然又變成回溯了，抓不到規律的每日題選題方式。

# 題目
輸入可能有重複的陣列nums，以任何順序回傳所有可能的排列。

# 解法
先當作普通的排列來處理，只是要排除重複的結果，所以把所有排列裝進set中去重複。

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        N=len(nums)
        
        def bt(i):
            if i==N:
                ans.add(tuple(nums))
            else:
                for j in range(i,N):
                    nums[i],nums[j]=nums[j],nums[i]
                    bt(i+1)
                    nums[i],nums[j]=nums[j],nums[i]
            
        bt(0)
        
        return ans
```

上面那種方法真的有點太混了，考慮看看別的方法。  
先用雜湊表將元素分組計數，以為元素組別考慮是否加入，而非個別的位置。  
例如：  
> [1,1,2]  
> 1出現兩次，2出現1次  
> 對於1，可以選擇[1]或是[1,1]  
> 組成[1,2]和[1,1,2]  
> 再透過[1,2]組成[1,2,1]

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        N=len(nums)
        ctr=Counter(nums)
        
        def bt(i,curr):
            if i==N:
                ans.append(curr[:])
            else:
                for k in ctr:
                    if ctr[k]>0:
                        curr.append(k)
                        ctr[k]-=1
                        bt(i+1,curr)
                        curr.pop()
                        ctr[k]+=1
                
        bt(0,[])
        
        return ans
```

還有一種方式是透過排序，保證相同的元素出現在一起，並以used陣列紀錄是否使用過。  
當某索引i的元素與i-1相同，而且i-1並沒有使用過，這時候加入i的話就會出現重複的組合，所以跳過這個位置。

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N=len(nums)
        used=[False]*N
        ans=[]
        
        def bt(i,curr):
            if i==N:
                ans.append(curr[:])
            else:
                for j in range(N):
                    if used[j] or j>0 and nums[j]==nums[j-1] and not used[j-1]:
                        continue
                    curr.append(nums[j])
                    used[j]=True
                    bt(i+1,curr)
                    curr.pop()
                    used[j]=False
                  
        bt(0,[])
                
        return ans
```