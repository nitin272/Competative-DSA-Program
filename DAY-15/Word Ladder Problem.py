# You are given two words, start and end, and a dictionary of words called wordList. You need to transform the start word into the end word using only words from the dictionary. Return the minimum number of transformations required. A valid transformation changes exactly one letter at a time, and each transformed word must exist in the word list.

# Input:
# The first input line contains the start word.
# The second input line contains the end word.
# The third input line contains space-separated words which form the wordList.



def ladderLength(start, end, wordList):
    wordSet = set(wordList)
    if end not in wordSet:
        return 0
    
    queue = [(start, 1)]
    
    while queue:
        current_word, steps = queue.pop(0)
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i + 1:]
                
                if next_word == end:
                    return steps + 1
                
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))
    
    return 0

start_word = input("Enter the start word: ")
end_word = input("Enter the end word: ")
word_list = input("Enter the word list (space-separated): ").split()

result = ladderLength(start_word, end_word, word_list)

print(result)
