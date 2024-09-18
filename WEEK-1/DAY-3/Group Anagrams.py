from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    
    return list(anagram_map.values())


strs = input("Enter strings separated by spaces: ").split()
grouped = group_anagrams(strs)
print("Grouped anagrams:")
for group in grouped:
    print(group)
