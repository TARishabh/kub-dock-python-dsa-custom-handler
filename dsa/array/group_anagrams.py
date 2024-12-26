# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def group_anagrams(strs):
    hashmap = defaultdict(list)

    for i in range(len(strs)):
        actual_string = tuple(sorted(strs[i]))
        hashmap[actual_string].append(strs[i])
    
    return list(hashmap.values())

print(group_anagrams(strs=["eat","tea","tan","ate","nat","bat"]))