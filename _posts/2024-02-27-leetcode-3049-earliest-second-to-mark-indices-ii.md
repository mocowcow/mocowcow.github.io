---
layout      : single
title       : LeetCode 3049. Earliest Second to Mark Indices II
tags        : LeetCode Hard Array HashTable BinarySearch Greedy Heap
---
周賽386。看起來上一題有點像，但邏輯幾乎不一樣。  

## 題目

輸入**索引從 1 開始**的整數陣列 nums 和 changeIndices，兩者大小分別為 n 和 m。  

起初，nums 中的所有索引都是**未標記**的，而你必須要標記他們。  
依序從 1\~m 中的第 s 秒，你可以執行以下操作**之一**：  

- 選擇 [1, n] 之間的索引 i，並使 nums[i] 減 1  
- 將 nums[changeIndices[s]] 設成任意的**非負**整數  
- 選擇 [1, n] 之間的索引 i，如果 nums[i] 等於 0，則標記索引 i
- 不做任何事  

求 [1, m] 之間的一個整數，代表在最佳情況下，能夠標記**所有**索引的**最早秒數**。若無法全部標記則回傳 -1。  

## 解法

繼續沿用上一題說過的考試/複習比喻，答案同樣可以二分，但是細節稍有不同。  

每門課程都各自需要複習 nums[i] 次，然後參加一次考試。  
對於第 s 天來說，有效選項有：  

1. 複習任意課程  
2. 參加任意課程考試  
3. **修改**第 changeIndices[s] 門課的**複習次數**  

求所有課程**複習且考試完**最快要多久。  

---

這個修改複習次數非常厲害啊，雖然說可以改成任意數字，其實只有改成 0 是最佳選擇，相當於一天複習 nums[i] 次。  
以下稱此操作為**快速複習**(~~課金複習??~~)。  

那怎樣使用快速複習比較有效率？  
首先，複習次數本身不能是 0，不然根本沒用，還浪費一天。  
如果某課程要快速複習，就不要浪費時間做普通複習了，同樣沒有意義。  

再來，如果同一門課有好幾天可以快速複習，選哪天更好？  
別忘記複習完還要考試，試想以下例子：  
> nums = [10], changeIndices = [1,1]  
> 選第一天快速複習，第二天還能考試  
> 選第二天快速複習，來不及考試了  

為保留更多的考試時間，快速複習**越早越好**。  
因此我們只記錄**複習次數非零**課程的最早(靠左)出現位置。  

---

如果不考慮快速複習，那麼完成所有複習 + 考試至少需要 sum(nums) + len(nums) = tot 天。  
fast 代表快速複習省下的天數，那麼最後所需天數是 tot - fast。  
對於這題來說，每天都可以**普通複習**或**考試**，因此可以併做一個變數 cnt 來維護。  

要記得快速複習之後還需要考試，因此我們從後往前遍歷，在碰到**快速複習**的日期時，還得保證至少有一天的空閒日期，才能夠順利考試。  

若要順利在期限內完成考試，必須滿足 cnt >= tot - fast。  

但有時候無法讓全部科目快速複習，而且剛好還先碰到不划算的。例如：  
> nums = [10,1,0], changeIndices = [3,3,1,2,3]
> 空閒日 cnt = 0
> changeIndices[4] = 3 不是快速複習，cnt = 1  
> changeIndices[3] = 2 可以快速複習，cnt = 0  
> changeIndices[2] = 1 可以快速複習，但空閒日 cnt = 0 後面來不及考試  

其實五天應該是足夠的，但是偏偏算錯，要怎麼找到更划算的科目來快速複習？  

---

可以維護**已完成的**快速複習，如果當前科目能夠省更多天，那就把之前的**退掉**。此技巧稱為**反悔貪心**。  
繼續來看剛才的例子：  
> nums = [10,1,0], changeIndices = [3,3,1,2,3]
> changeIndices[2] = 1 可以快速複習，但是 cnt = 0 無法考試  
> 已完成的快速複習的只有科目2  
> 若使用快速複習，科目2 只省下一天，當前的科目1 可以省下十天  
> 因此把科目2 退掉，改成快速複習科目1  
> 而原本快速複習科目2 當天，**也會變成空閒日**。cnt = 1  
> 剩下兩天也是空閒日，cnt = 3

如此一來，第三、第五天拿來快速複習科目1 並考試。  
剩餘三天空閒日處理科目2 和科目3，剛剛好。  

代入上一段的公式：  
> cnt >= tot - fast  
> 本題基本天數 tot = 11 + 3 = 14
> 快速複習節省天數 fast = 10，剩餘空閒日 cnt = 3。  
> 得到 3 >= 14 - 10  
> 3 >= 4  

咦好像怪怪的，但是五天應該可以才對？  
原來不小心忘記，分配快速複習的當下**已經扣除一天空閒日**，實際上的空閒日還要再加上快速複習次數才對。  
> count(fast) + cnt >= tot - fast  
> 1 + 3 >= 4  

這樣就對了。  

---

最後只要決定如何維護已完成快速複習中**節省天數**最小值。  
反正只要取最小，那就選擇 min heap 即可。  

時間複雜度 O(M log(M \* min(M, N)))。  
空間複雜度 O(N)。  

```python
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        N = len(nums)
        M = len(changeIndices)
        tot = sum(nums) + N # 普通複習 + 考試
        
        fast_day = set()
        seen = set()
        for day in range(M):
            idx = changeIndices[day] - 1
            if nums[idx] > 0 and idx not in seen:
                fast_day.add(day)
            seen.add(idx)
            
        def ok(limit):
            cnt = 0 # 空閒日
            h = [] # 已完成的快速複習
            for day in reversed(range(limit)):
                idx = changeIndices[day] - 1
                val = nums[idx]
                if not day in fast_day: # 非快速複習日，即空閒日  
                    cnt += 1
                    continue
                
                # 快速複習日
                if cnt > 0: # 有空閒日，快速複習，並拿一天空閒來考試
                    heappush(h, val)
                    cnt -= 1 
                    continue
                    
                # 否則試著退掉一科較差的快速複習
                if h and h[0] < val: # 退成功，改快速複習當前科目
                    heappop(h)
                    heappush(h, val)
                cnt += 1 # 有退成功，退掉當天變空閒；沒退成功，本日空閒
                    
            return cnt + len(h) >= tot - sum(h) # 空閒日 + 已考試日 >= 基本天數 - 已省天數
            
        ans = 1 + bisect_left(range(1, M + 1), True, key=ok)
        
        if ans > M:
            return -1
        
        return ans
```

參考 awice 大神的[題解](https://leetcode.com/problems/earliest-second-to-mark-indices-ii/discuss/4778732/Python3-Binary-Search-%2B-Heap)，他的貪心邏輯真的是有夠簡潔。  

只要是快速複習日，不管空閒日夠不夠，都直接塞進 min heap。因為：  

- 空閒日夠，那就空閒加 1  
- 不夠  
  - 能退，退出最小的，空閒加 1
  - 不能退，退出**當前的**，空閒加 1  

處理邏輯剛好相符，整個濃縮起來。  

```python
        def ok(limit):
            cnt = 0 # 空閒日
            h = [] # 已完成的快速複習
            for day in reversed(range(limit)):
                idx = changeIndices[day] - 1
                val = nums[idx]
                if not day in fast_day: # 非快速複習日，即空閒日  
                    cnt += 1
                else: # 快速複習日
                    heappush(h, val)
                    if cnt > 0: # 有空閒日，快速複習，並拿一天空閒來考試
                        cnt -= 1 
                    else: # 不管有沒有退成功，至少一天會變空閒
                        cnt += 1
                        heappop(h)
            return cnt + len(h) >= tot - sum(h) # 空閒日 + 已考試日 >= 基本天數 - 已省天數
```
