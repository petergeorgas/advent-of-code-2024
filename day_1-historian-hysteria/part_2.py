import heapq
from collections import Counter

left_list, right_list = [], []

with open("input.txt", "r") as inp:
    count = 0
    for line in inp:
        line = line.strip()

        split_line = line.split("   ") # 3 space width
        if len(split_line) != 2:
            break
        left, right = split_line[0].strip(), split_line[1].strip()
        left_list.append(int(left))
        right_list.append(int(right))
        count += 1
    print(f"Read {count} lines.")

if len(left_list) != len(right_list):
    raise ValueError("Left and Right Lists must have same len")

right_counts = Counter(right_list)

similarity_score = 0
for left_number in left_list:
    if left_number not in right_counts:
        continue
    similarity_score += left_number * right_counts[left_number]

print(f"Similarity Score: {similarity_score}")
