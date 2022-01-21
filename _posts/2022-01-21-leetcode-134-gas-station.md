---
layout      : single
title       : LeetCode 134. Gas Station
tags 		: LeetCode Medium Greedy
---
以前用O(N^2)竟然也能過，真神奇。

# 題目
有個環形的路線，gas[i]表示可以加的油，cost[i]表示開往下一站的耗油量。  
求從哪邊出發，才能夠達成無限循環，只有一個正確答案。若無則回傳-1。

# 解法
要達成循環有個大前提：至少要獲得足夠的油料。  
邊走邊計算當前剩餘油料，如tank<0表示開不下去了，則設下一站為起點。  
最後油料支出若大於收入，則無解。

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = tank = gasSum = costSum = 0
        for i in range(len(gas)):
            gasSum += gas[i]
            costSum += cost[i]
            tank += gas[i]-cost[i]
            if tank < 0:
                start = i+1
                tank = 0

        return -1 if costSum > gasSum else start
```
