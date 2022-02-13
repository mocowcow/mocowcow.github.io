---
layout      : single
title       : LeetCode 78. Subsets
tags 		: LeetCode Medium Array Backtracking DP
---
每日題。突然發現沒有寫過回溯法的題解，今天剛好碰上。

# 題目
輸入不重複的整數陣列nums，回傳nums的所有子集合(冪集合)。

# 解法
如何找出所有組合？對於每個元素，都有拿、不拿兩個分支可走，多一個元素，子集合數量便會*2。  
根據定義，冪集合也包含空集合，總共有2^N個子集合。  
從空集合開始，對nums中每個元素，可以選擇是否加入。處理完所有元素，則將子集合加入ans。  

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []

        def bt(i, curr):
            if i >= N:
                ans.append(curr[:])
            else:
                bt(i+1, curr)
                curr.append(nums[i])
                bt(i+1, curr)
                curr.pop()

        bt(0, [])
        return ans
```

官方標籤沒有DP，這邊提供另一個思路。  
一開始只有一個包含空集合的集合S，S={{}}，當S碰到新的元素1，可以選擇加不加，加了會產生新的集合T={{1}}，此時將T加回S，S={{},{1}}。又碰到新的元素2，T={{2},{1,2}}，加回S={{},{1},{2},{1,2}}，以此類推。

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for n in nums:
            dp += [x+[n] for x in dp]

        return dp
```

還有一種是我當初最早認識的解法，使用位元操作。  
對於[1,2,3]，若使用二進位1/0表示拿或不拿，111代表{1,2,3}，110代表{1,2}，以此類推，從0到2^N-1正好2^N種集合，程式碼就不付上了。