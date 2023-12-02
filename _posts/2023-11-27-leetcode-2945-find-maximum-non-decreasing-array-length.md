---
layout      : single
title       : LeetCode 2945. Find Maximum Non-decreasing Array Length
tags        : LeetCode Hard Array DP PrefixSum Math MonotonicStack Stack BinarySearch MonotonicQueue
---
雙周賽118。我連怎麼下手都不知道，最後不到50個人做出來的樣子，有機會刷新全站最高難度。  

題外話，本題似乎是amazon辦的某個比賽的原題，然侯第一個做出來的印度老哥正好是該公司員工，然後跟著就冒出一堆印度老哥也做出來了。  
這次前25名竟然有一半都是印度人，而且有兩個才1700分，連簡單的Q2都沒做出來，竟然能做出這題大概2800分的題，真有點意思。  

## 題目

輸入整數陣列nums。  

你可以執行任意次操作，每次操作可以從nums中選擇一個**子陣列**，並將其替換成元素和。  
例如[1,3,5,6]選擇子陣列[3,5]進行操作，得到[1,**8**,6]。  

求任意次操作後，使得陣列滿足**非遞減**條件下所能得到的**最大**長度。  

## 解法

搞好幾天才弄懂，感覺上有兩道門檻，光是要找到入口就有點難度。  

大佬說了一句話：  
> 貪心的盡頭是dp  

貪心是一種求局部最佳解的方式，而dp求的是全局最佳解。  
若剛好全局最佳解是由各個局部最佳所求出，那麼兩者都能夠找出答案；但有時局部最佳並無法構成全局最佳，這時候只能靠dp來解決。  
個人理解為，當**發現無法貪心**(局部最佳非全局最佳)時，應當及時回頭，改朝著dp去思考。  

從範例三可以看出，貪心的合併並不是最佳解，轉去想dp吧。  
定義dp[i]：以i結尾的子陣列，經過任意次合併後，滿足非遞減時的**最大長度**。  
要從滿足j<i的索引j轉移過來，把nums[j+1,i]這串全部合併起來，sm=sum(nums[j+1,i])，記做last[i]。  
轉移方程式：dp[i]=max(dp[j]+1 FOR ALL -1<=j<i)，且滿足last[j]<=sm  
base case：為了允許從空陣列轉移，使-1代表空陣列，dp[-1]和last[-1]都為0。  

在dp[i]最大化的前提下，last[i]應該越小越好，這樣更有利於之後接續的新元素。  
例如nums = [2,1,3,..]的情況，合成[3,3..]肯定是比[2,4,..]更有機會變長。  

至於求子陣列和可以用前綴和來優化，只要O(1)求和。ps[i]代表nums[0,i]的加總。  
到目前為止的步驟是：  

1. 枚舉結尾i  
2. 找到須滿足last[j]<=ps[i]-ps[j]，且使dp[i]最大化，再使last[i]最小的轉移轉移來源j  

仔細想想，在我們枚舉i的過程中，需要合併的數不斷增加。但最差情況下也就是直接合併到最尾端的last[i-1]裡面去，得dp[i]=dp[i-1]，所以dp[i]一定是**非遞減**的。  
那對於同一個i來說，當轉移來源j越大，合併到i的數越少，last[i]也會更小。  
正向枚舉j的過程中，只要當前的j滿足last[j]<=sm，那麼他絕對不會比之前的dp[j]更差，然後last[i]一定會更小。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        N=len(nums)
        ps=list(accumulate(nums))+[0]
        dp=[0]*(N+1)
        last=[0]*(N+1)
        
        # O(N^2) TLE
        for i,x in enumerate(nums):
            for j in range(-1,i):
                sm=ps[i]-ps[j]
                if last[j]<=sm:
                    dp[i]=dp[j]+1
                    last[i]=sm
                    
        return dp[N-1]
```

要把nums[j+1,i]做為結尾時，須滿足last[j]<=ps[i]-ps[j]。  
在i改變時，對於每個j的結果都不同，全都要重新計算。  
將式子變形得：last[j]+ps[j]<=ps[i]，那麼last[j]+ps[j]就變成固定的值了。暫且記last[j]+ps[j]為v[j]。  

剛才ps[i]和ps[j]是前綴和，理所當然是非遞減的。那麼last[j]呢？  
在dp[j-1]==dp[j]的時候last[j]是遞增，但是當dp[j-1]>dp[j]時，last[j]就會突然遞減。  
例如nums=[4,3,1,6]：  
> ps=[4,7,8,14]  
> dp=[1,1,2,3]  
> last=[4,7,4,6]  
> v=[8,14,12,20]  

觀察v的變化，大概就像是心電圖。只是右方的波谷不可能低於左方的波谷，畢竟都是正整數。  
雖然i可以從任意合法的j轉移過來，但剛才也說過，j越大，dp[j]推出的dp[i]也越大。  
看到dp[2]不僅大於dp[1]，連v[2]都小於v[1]。只要能選j=2的情形，肯定能選j=1；反之，能選j=1時可不一定能選j=2。  
乾脆把沒用的選項刪掉。這就是**單調堆疊**，堆疊中只保留著遞增的v值。  

刪除掉沒用的選項後，v=[8,14,_,20]。  
如果nums後面再加一個元素3：  
> nums=[4,2,1,6,3], ps[4]=17  
> 在v中找最後一個小於等於17的元素，也就是14，對應的索引j=1  

在單調遞增的集合中查找，當然就是二分搜了。  
找到j之後，以j更新dp[i]和v[i]，並刪掉比v[i]還差的v[j]。最後堆疊頂端元素一定是dp[N-1]，也就是答案。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        N=len(nums)
        ps=list(accumulate(nums))+[0]
        st=[[-1,0,0]] # [j, v[j], dp[j]]
        
        for i,x in enumerate(nums):
            # last[j] <= ps[i]-ps[j]
            # v[j] = last[j]+ps[j] <= ps[i]
            lo=0
            hi=len(st)
            while lo<hi:
                mid=(lo+hi)//2
                if st[mid][1]<=ps[i]: # v[j]<=ps[i]
                    lo=mid+1
                else:
                    hi=mid
                    
            # found j
            j,vj,dpj=st[lo-1]
            lasti=ps[i]-ps[j]
            vi=ps[i]+lasti
            dpi=dpj+1
            while st and vi<=st[-1][1]:
                st.pop()
            st.append([i,vi,dpi])
                    
        return st[-1][2] # dp[N-1]
```

其實單調堆疊已經可以AC了，但還能更快。  

若存在某個索引j，滿足v[j] = last[j]+ps[j] <= ps[i]，隨著i增大，ps[i]也會增加，而v[j]對於更大的i來說永遠也都是合法的。
因此，我們只需要保留一個最大可用的索引i做為轉移來源，非最大的選項都可以刪掉。  
左右兩端都及時刪除無效選項，這就是**單調隊列**。  

注意：至少要保留一個可用的，所以從隊首刪除時，**至少**要兩個合法來源，才能刪掉最小那個。  
因此是檢查隊列中**第二項**，而非隊首。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        N=len(nums)
        ps=list(accumulate(nums))+[0]
        q=deque()
        q.append([-1,0,0]) # [j, v[j], dp[j]]
        for i,x in enumerate(nums):
            # last[j] <= ps[i]-ps[j]
            # v[j] = last[j]+ps[j] <= ps[i]
            while len(q)>1 and q[1][1]<=ps[i]: # at least keep 1 valid 
                q.popleft()
                    
            # found j
            j,vj,dpj=q[0]
            lasti=ps[i]-ps[j]
            vi=ps[i]+lasti
            dpi=dpj+1
            while q and vi<=q[-1][1]:
                q.pop()
            q.append([i,vi,dpi])
            
        return q[-1][2]
```
