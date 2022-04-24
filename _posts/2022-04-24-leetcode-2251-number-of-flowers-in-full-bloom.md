---
layout      : single
title       : LeetCode 2251. Number of Flowers in Full Bloom
tags 		: LeetCode Hard Array BinarySearch PrefixSum
---
周賽290。其實很簡單的題目，只是我看到寬度10^9又有range update，就跑去搞線段樹，好不容易弄出來又TLE，沒有好好把握住這次機會。  
周賽結束後改成前綴和5分鐘就寫完了，好可惜。

# 題目
輸入二維陣列flowers代表每朵花i的開花期[開花日i,開花最後一日i]，以及長度為N的陣列persons，代表第i人在第persons[i]天來賞花。  
回傳長度為N的陣列ans，ans[i]代表第i人可以看到幾朵盛開的花。

# 解法
先處理每個花的開花期，轉成花朵量改變事件，開花日花量+1，凋謝日花量-1。依照發生日期排序，使用差分前綴和，計算在第d日時的花數改變成多少。  
初始化psum=[(-1,0)]，代表第-1天時有0朵花，開始遍歷所有事件，並加入(第k天,花朵數n)到前綴和。  
> flowers = [[1,6],[3,7],[9,12],[4,13]]  
> psum = [(-1, 0), (1, 1), (3, 2), (4, 3), (7, 2), (8, 1), (9, 2), (13, 1), (14, 0)]   
> 代表：[(第-1天沒花),(第1天1花),(第3天2花),(第4天3花),(第7天2花),(第8天1花),(第9天2花),(第13天1花),(第14天沒花)]  

遍歷所有person，若他在第d日抵達賞花，則在psum中找第一個小於等於d的日期，就是他當天看到的開花數量。  
接續上例，若有人在第11日抵達看花：  
> 於psum中找到第一個小於等於11的日期 = 9  
> 因為從9日開始到13日，開花數都沒有改變，所以9日和11日開花數一樣  
> 答案應為第9日的開花數 = 2朵  

```python
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        d=defaultdict(int)
        for s,e in flowers:
            d[s]+=1
            d[e+1]-=1
        
        psum=[(-1,0)]
        for k in sorted(d.keys()):
            n=psum[-1][1]+d[k]
            psum.append((k,n))
            
        ans=[]
        for day in persons:
            lo=0
            hi=len(psum)-1
            while lo<hi:
                mid=(lo+hi+1)//2
                if psum[mid][0]>day:
                    hi=mid-1
                else:
                    lo=mid                
            ans.append(psum[lo][1])

        return ans
```

