def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


intervals = []
print("Enter intervals as pairs of integers (end with an empty line):")
while True:
    try:
        line = input()
        if not line:
            break
        interval = list(map(int, line.split()))
        intervals.append(interval)
    except ValueError:
        print("Invalid input, please enter integers.")
        
merged = merge_intervals(intervals)
print("Merged intervals:")
for interval in merged:
    print(interval)
