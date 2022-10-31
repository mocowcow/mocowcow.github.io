--- 
layout      : single
title       : LeetCode 2456. Most Popular Video Creator
tags        : LeetCode Medium Array String HashTable
---
周賽317。又是臭長題，我竟然沒出錯，給自己一個肯定。感覺這種很囉唆的題目還是乖乖拆成多個步驟來解比較好，為了省字數而拿到WA得不償失。  

# 題目
輸入兩個字串長度n的陣列creators和id，以及一個整數陣列views。平台上的第i個影片是由creator[i]投稿的，影片id為ids[i]，且有views[i]次觀看數。  

創作者的**人氣**是其所有影片的觀看次數總和。找到**人氣最高**的創作者以及他們**觀看次數最多**的的影片id。

如果多個創作者的人氣最高，則列出所有創作者。  
如果某個創作者有多個影片觀看次數最多，則選擇字典順序最小的id。  
回傳二維陣列answer，其中answer[i] = [creator<sub>i</sub>, id<sub>i</sub>] 表示 creator<sub>i</sub> 的人氣最高，id<sub>i</sub>是他們最多觀看的影片id。answer可以依照任何順序回傳。    

# 解法
分成三大步驟：  
1. 計算最高的總播放次，記為mx  
2. 找到所有總播放次數為mx的創作者們  
3. 把這些創作者們的**最高播放**中的**最小字典序id**  
4. 將作者和影片id加入答案  

時空間複雜度都是O(N)。雖然在篩選作者時用到兩層迴圈，但因為影片總數為N個，均攤下來最多還是O(N)。  

```python
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        tt_view=Counter()
        video=defaultdict(list)
        
        for c,id,v in zip(creators,ids,views):
            tt_view[c]+=v
            video[c].append([id,v])
                
        mx=max(tt_view.values())
        ans=[]
        for c,tt in tt_view.items():
            if tt==mx:
                mx_view=-inf
                mx_id=None
                for id,v in video[c]:
                    if v>mx_view:
                        mx_view=v
                        mx_id=id
                    elif v==mx_view and mx_id>id:
                        mx_id=id
                ans.append([c,mx_id])
                
        return ans
```
