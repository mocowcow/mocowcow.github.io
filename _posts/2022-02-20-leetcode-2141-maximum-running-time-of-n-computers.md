---
layout      : single
title       : LeetCode 2141. Maximum Running Time of N Computers
tags 		: LeetCode Hard BinarySearch Greedy Sorting Array
---
模擬周賽276。最後一題想了超久，總算解出來，只可惜不是真正參加周賽，不然積分要暴漲了。  
![排名圖](/assets/img/mock276-rank216.jpg)

# 題目
輸入整數n，代表你有n台電腦，整數列陣batteries，代表每顆電池能夠讓電腦運轉多久。  
每一台電腦同時只能接上一顆電池，而電池同時也只能給一台電腦供電。  
假設電池拆裝不需要耗時，求最多可以讓所有電腦保持運轉狀態幾分鐘。

# 解法
其實這題很類似什麼koko吃香蕉、魔法數字之類的，只要測資超大又沒什麼明顯特徵的話，八成會是二分搜。  
定義一個函數canRun(int time)，試算在是否能讓全部電腦運行time分鐘。準備二分搜找答案，時間沒有負數，lower bound
為0，電池最大電量為10^9，最多電池數為10^5，upper bound設為10^15。若成功運行mid分鐘則更新low=mid，否則high=mid-1。最後回傳low就是答案。  

重點就是這個canRun函數搞了好久才弄出來，只想說先從最大電量的電池開始用，其中哪個沒電了才換下一顆。苦思良久發現最關鍵的點：電池的電量p若超過運行時間time，因為電池只能接一台電腦，所以多餘的電量也沒辦法拿去給其他電腦用。  
我決定把電池由電量降冪排序，先找出n顆最大的電池，並維護變數lack代表不足電量，如果電量p少於time時，則將time-p加入lack。之後剩下的電池電量若能補足lack，
則代表可以成功運行。

```python
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=1)

        def canRun(time):
            lack = 0
            for p in batteries[:n]:
                if p < time:
                    lack += time-p
            for p in batteries[n:]:
                lack -= p
                if lack <= 0:
                    return True
            return lack <= 0

        low = 0
        high = 10**14
        while low < high:
            mid = (low+high+1)//2
            if canRun(mid):
                low = mid
            else:
                high = mid-1

        return low

```
