def processcase(case_num):
    # Input for cases
    (num_candy_bags, num_kids) = tuple(map(int, input().split()))
    candy_counts = list(map(int, input().split()))

    # Calculate the amount of candy remaining
    num_candy = 0
    for i in range(num_candy_bags):
        num_candy += candy_counts[i]
    # Use module to calculate the remaining candy
    remaining_candy = num_candy % num_kids

    print(f"Case #{case_num}: {remaining_candy}")

# Iterate through the each case
num_cases = int(input())
for i in range(num_cases):
    processcase(i + 1)