import matplotlib.pyplot as plt
import random
import time

def longest_non_prefix_set_divide_conquer(strings):
    if not strings:
        return 0
    
    if len(strings) == 1:
        return 1
    
    mid = len(strings) // 2
    left_set = strings[:mid]
    right_set = strings[mid:]
    
    left_size = longest_non_prefix_set_divide_conquer(left_set)
    right_size = longest_non_prefix_set_divide_conquer(right_set)
    
    merged_set = left_set + right_set
    merged_set = sorted(merged_set, key=len)
    merged_size = 1
    prev_string = merged_set[0]
    for s in merged_set[1:]:
        if not s.startswith(prev_string):
            merged_size += 1
            prev_string = s
    
    return max(left_size, right_size, merged_size)

def longest_non_prefix_set_dynamic(strings):
    n = len(strings)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if not strings[i].startswith(strings[j]) and not strings[j].startswith(strings[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def longest_non_prefix_set_greedy(strings):
    result = []
    
    for s in sorted(strings, key=len):
        if all(not s.startswith(t) for t in result):
            result.append(s)
    
    return len(result)


def generate_test_cases(n, min_length, max_length):
    strings = []
    for _ in range(n):
        length = random.randint(min_length, max_length)
        strings.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length)))
    return strings

def test_and_plot(n_range, min_length, max_length):
    divide_conquer_times = []
    dynamic_times = []
    greedy_times = []
    
    for n in n_range:
        strings = generate_test_cases(n, min_length, max_length)
        
        # Divide and Conquer
        start_time = time.time()
        longest_non_prefix_set_divide_conquer(strings)
        divide_conquer_times.append(time.time() - start_time)
        
        # Dynamic Programming
        start_time = time.time()
        longest_non_prefix_set_dynamic(strings)
        dynamic_times.append(time.time() - start_time)
        
        # Greedy
        start_time = time.time()
        longest_non_prefix_set_greedy(strings)
        greedy_times.append(time.time() - start_time)
    
    # Plot the results
    plt.figure(figsize=(12, 8))
    plt.plot(n_range, divide_conquer_times, label='Divide and Conquer')
    plt.plot(n_range, dynamic_times, label='Dynamic Programming')
    plt.plot(n_range, greedy_times, label='Greedy')
    plt.xlabel('Number of Strings (n)')
    plt.ylabel('Execution Time (s)')
    plt.title('Longest Non-Prefix Set Algorithms')
    plt.legend()
    plt.grid()
    plt.show()

# Test the algorithms with different input sizes
n_range = [10, 50, 100, 200, 500, 1000]
min_length = 3
max_length = 10
test_and_plot(n_range, min_length, max_length)