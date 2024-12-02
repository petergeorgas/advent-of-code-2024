import heapq

left_list, right_list = [], []

with open("input.txt", "r") as inp:
    count = 0
    for line in inp:
        line = line.strip()

        split_line = line.split("   ") # 3 space width
        if len(split_line) != 2:
            break
        left, right = split_line[0].strip(), split_line[1].strip()
        heapq.heappush(left_list, int(left))
        heapq.heappush(right_list, int(right))
        count += 1
    print(f"Read {count} lines.")

if len(left_list) != len(right_list):
    raise ValueError("Left and Right Lists must have same len")

total_dist = 0
while left_list and right_list:
    left_min, right_min = heapq.heappop(left_list), heapq.heappop(right_list)
    total_dist += abs(left_min - right_min)

print(f"Total Distance: {total_dist}")
