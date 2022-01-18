from datetime import datetime

# TOPIC = '1463. Cherry Pickup II'
TOPIC = input()

number = TOPIC[:TOPIC.index('.')]
title = '-'.join(TOPIC.split(' ')[1:]).lower()
time = datetime.now().strftime('%Y-%m-%d')
filename = f'{time}-leetcode-{number}-{title}.md'
template = f"""---
layout      : single
title       : LeetCode {title}
tags 		: LeetCode
---
# 題目

# 解法

```python
code here
```
"""
f = open(filename, 'w', encoding='utf8')
f.write(template)
