d = {

    'lc':  'LeetCode',
    'm':  'Medium',
    'a':  'Array',
    'e':  'Easy',
    'dp':  'DP',
    'h':  'Hard',
    'bs':  'BinarySearch',
    's':  'String',
    'gd':  'Greedy',
    'sort':  'Sorting',
    'tp':  'TwoPointers',
    'dfs':  'DFS',
    'math':  'Math',
    'ht':  'HashTable',
    'mat':  'Matrix',
    'bfs':  'BFS',
    'g':  'Graph',
    'ps':  'PrefixSum',
    'design':  'Design',
    'st':  'Stack',
    'll':  'LinkedList',
    'bit':  'BIT',
    'bm':  'BitManipulation',
    'hp':  'Heap',
    'bintree':  'BinaryTree',
    'sw':  'SlidingWindow',
    'XXXX':  'MonotonicStack',
    'bt':  'Backtracking',
    'segtree':  'SegmentTree',
    'bst':  'BinarySearchTree',
    'trie':  'Trie',
    'sim':  'Simulation',
    'count':  'Counting',
    'geo':  'Geometry',
    'XXXX':  '筆記',
    'daq':  'DevideAndConquer',
    'tree':  'Tree',
    'sl':  'SortedList',
    'XXX':  'Python',
    'mst':  'MST',
    'uf':  'UnionFind'
}


st = []
while True:
    x = input()
    if x == '':
        break
    elif x == '?':
        st.pop()
    elif x in d:
        st.append(d[x])
    else:
        print(x, 'not found')
    print(st)


print('\n\n\n\n\n')
print(' '.join(st))
print('\n\n\n\n\n')
