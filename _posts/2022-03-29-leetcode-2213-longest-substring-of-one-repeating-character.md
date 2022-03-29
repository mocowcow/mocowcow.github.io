---
layout      : single
title       : LeetCode 2213. Longest Substring of One Repeating Character
tags 		: LeetCode Hard String SortedList BinarySearch
---
周賽285沒做出來的。只有140個人通過，超級噁心。看一堆人都是用線段樹來解，但是我好像比較能夠接受sorted list。  
突然想起以前上課時，老師問到java有沒有sorted list？那時我還心想要這種東西幹嘛。果然太天真了。

# 題目
輸入字串s，之後會經過一串的修改，每次對位置i以新字元取代。queryCharacters[i]代表第i次修改的新字元，queryIndices[i]代表第i次修改的位置。  
回傳一個陣列，儲存每次修改後，由單一字元形成的子字串最大長度。  
> s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]  
> s[1]從a改成b，s=b**b**bacc，最大長度=3  
> s[3]從a改成c，s=bbb**c**cc，最大長度=3  
> s[3]從c改成b，s=bbb**b**cc，最大長度=4  

# 解法
周賽當時就有想到用list保存所有的連續子字串區段，然後每次修改用二分搜找位置，再進行刪除、合併、插入新區段，只是超級麻煩時間又不夠。  
後來知道有sorted list這東西，幫我完成搜尋插入的部分，實作起來就簡單不少了。  

先處理原字串s，轉換成tuple(start,end,c)，表示從start到end-1為止都是連續的字元c，保存在sl裡面，而長度end-start保存在longest，longest的最後一個元素就是最大長度。  
> s = "babacc"  
> sl = [(0, 1, 'b'), (1, 2, 'a'), (2, 3, 'b'), (3, 4, 'a'), (4, 6, 'c')]  
> longest[-1] = 2

開始處理每一次的修改。以修改位置s[i]在所有有序區段中找到所屬的區段j，若區段j的組成字元與目標相同則不動作，最大長度直接加到ans；否則進行一系列的區段修改：  
1. 若s[i]所屬的區段j長度大於1，則此修改會產生新的子區段。如"aaa"將s[1]修改成b，會產生"a"、"b"和"a"區段  
2. 若s[i]位於區段j的最左或是最右方，則試著與相鄰的同組成區段合併  
3. 刪除所有修改過的舊區段，加入所有新的區段
4. 加入最大長度到ans

需要注意的是，一定要先暫存所有異動的區段，等待計算完成後才一次更新，否則會出現錯誤。  
[參考來源](https://leetcode.com/problems/longest-substring-of-one-repeating-character/discuss/1865727/Python-SortedList-solution)。

```python
from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # build segments
        sl = SortedList()
        longest = SortedList()
        start = 0
        for newC, times in groupby(s):
            size = sum(1 for _ in times)
            longest.add(size)
            sl.add((start, start+size, newC))  # s[start:end] with same character
            start += size

        # queries
        ans = []
        for i, newC in zip(queryIndices, queryCharacters):
            j = sl.bisect_right((i, math.inf))-1
            if sl[j][2] == newC:  # same characater
                ans.append(longest[-1])
            else:  # modify s[i] with newC
                start, end, c = sl[j]
                toRemove = [sl[j]]
                toAdd = []

                # split original segment if size more than 1
                if end-start > 1:
                    if i == start:  # modify leftmost
                        toAdd.append((start+1, end, c))
                    elif i == end-1:  # modify rightmost
                        toAdd.append((start, end-1, c))
                    else:  # modify middle
                        toAdd.append((start, i, c))
                        toAdd.append((i+1, end, c))

                # merge with neighbors
                newStart, newEnd = i, i+1
                if sl[j][0]==i and j > 0 and sl[j-1][2] == newC:  # merge left
                    newStart = sl[j-1][0]
                    toRemove.append(sl[j-1])
                if sl[j][1]==i+1 and j+1 < len(sl) and sl[j+1][2] == newC:  # merge right
                    newEnd = sl[j+1][1]
                    toRemove.append(sl[j+1])
                toAdd.append((newStart, newEnd, newC))

                # remove old segments
                for x in toRemove:
                    sl.remove(x)
                    longest.remove(x[1]-x[0])

                # add new segments
                for x in toAdd:
                    sl.add(x)
                    longest.add(x[1]-x[0])

                ans.append(longest[-1])

        return ans
```

