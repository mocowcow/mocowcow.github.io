from string import Template


# 輸入文章的檔名(不含.md)
# link = '2022-04-26-leetcode-940-distinct-subsequences-ii'
link = input()
try:
    title = link.split('leetcode-')[1].replace('-', ' ').replace(' ', '. ', 1)
except:
    title = 'invalid_title'

template = Template('[$TITLE]({% post_url $LINK %})')
s = template.substitute(TITLE=title, LINK=link)
print('\n\n\n\n\n')
print(s)
print('\n\n\n\n\n')
