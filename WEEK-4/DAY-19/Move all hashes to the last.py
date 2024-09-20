
# Input: k#al#vi#um

# Output: kalvium###


s = input()
n = len(s)
output = ""
hash_count = 0

for i in range(n):
    if s[i] == '#':
        hash_count += 1
    else:
        output += s[i]

output += '#' * hash_count
print(output)
