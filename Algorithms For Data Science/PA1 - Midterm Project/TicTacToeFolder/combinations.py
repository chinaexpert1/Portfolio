import math

# Function to calculate combinations
def combinations(n, r):
    return math.comb(n, r)

# Calculate the total combinations for each group
combinations_per_group = sum(combinations(9, r) for r in range(1, 10))

# Square the result to account for both groups
total_combinations = combinations_per_group ** 2

                                        print(`562YTW2S3QEG`)
