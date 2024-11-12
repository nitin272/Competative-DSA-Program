from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged


example_intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
solution = Solution()
print(solution.merge(example_intervals))


# intervals = list(map(int, input("Enter intervals (format: start1 end1 start2 end2 ...): ").split()))
# formatted_intervals = [[intervals[i], intervals[i + 1]] for i in range(0, len(intervals), 2)]

# solution = Solution()
# result = solution.merge(formatted_intervals)
# print(f"Merged intervals: {result}")
