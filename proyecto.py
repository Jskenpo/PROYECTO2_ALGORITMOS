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
    
    # Recursively find the largest non-prefix set for left and right subsets
    left_size = longest_non_prefix_set_divide_conquer(left_set)
    right_size = longest_non_prefix_set_divide_conquer(right_set)
    
    # Merge and find the largest non-prefix set for the merged set
    merged_set = set(left_set) | set(right_set)
    merged_size = 0
    for s in merged_set:
        if all(not s.startswith(t) for t in merged_set if t != s):
            merged_size += 1
    
    # Return the maximum size among left, right, and merged sets
    return max(left_size, right_size, merged_size)

def longest_non_prefix_set_dynamic(strings):
    strings.sort(key=len)
    n = len(strings)
    dp = [0] * n
    dp[0] = 1
    prefix_set = {strings[0]}

    for i in range(1, n):
        if not any(strings[i].startswith(s) for s in prefix_set):
            dp[i] = dp[i-1] + 1
            prefix_set.add(strings[i])
        else:
            dp[i] = dp[i-1]

    return dp[-1]

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
        strings.append(''.join(random.choices('abcdefghij', k=length)))
    return strings

def test_and_plot(n_range, min_length, max_length):
    divide_conquer_times = []
    dynamic_times = []
    greedy_times = []
    divide_conquer_solutions = []
    dynamic_solutions = []
    greedy_solutions = []
    
    for n in n_range:
        strings = generate_test_cases(n, min_length, max_length)

        # Divide and Conquer
        start_time = time.time()
        divide_conquer_solutions.append(longest_non_prefix_set_divide_conquer(strings))
        divide_conquer_times.append(time.time() - start_time)
        
        # Dynamic Programming
        start_time = time.time()
        dynamic_solutions.append(longest_non_prefix_set_dynamic(strings))
        dynamic_times.append(time.time() - start_time)
        
        # Greedy
        start_time = time.time()
        greedy_solutions.append(longest_non_prefix_set_greedy(strings))
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

    # Save the plot as an image
    plt.savefig('plot.png')

    # Print the execution times and solutions
    print("Divide and Conquer: ", divide_conquer_times)
    print("Divide and Conquer Solutions: ", divide_conquer_solutions)
    print("Dynamic Programming: ", dynamic_times)
    print("Dynamic Programming Solutions: ", dynamic_solutions)
    print("Greedy: ", greedy_times)
    print("Greedy Solutions: ", greedy_solutions)

# Test the algorithms with different input sizes
n_range = [10, 50, 100, 200, 500, 1000, 5000]
min_length = 3
max_length = 5
test_and_plot(n_range, min_length, max_length)
