from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)

    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
