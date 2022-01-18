from datetime import datetime
import os

# TOPIC = '1. Two Sum'
TOPIC = input()

number = TOPIC[:TOPIC.index('.')]
title = '-'.join(TOPIC.split(' ')[1:]).lower()
time = datetime.now().strftime('%Y-%m-%d')
filename = f'{time}-leetcode-{number}-{title}.md'
template = f"""---
layout      : single
title       : LeetCode {TOPIC}
tags 		: LeetCode
---
# 題目

# 解法

```python
code here
```
"""
if not os.path.exists(f'./{filename}'):
    print('file created')
    f = open(filename, 'w', encoding='utf8')
    f.write(template)
