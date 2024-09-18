from collections import Counter

def find_substring(s, words):
    if not s or not words:
        return []

    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count
    word_map = Counter(words)
    result = []

    for i in range(len(s) - total_length + 1):
        seen = Counter()
        for j in range(0, total_length, word_length):
            word = s[i + j:i + j + word_length]
            if word not in word_map:
                break
            seen[word] += 1
            if seen[word] > word_map[word]:
                break
        if seen == word_map:
            result.append(i)

    return result


s = input("Enter the string: ")
words = input("Enter words separated by spaces: ").split()
print("Starting indices:", find_substring(s, words))
