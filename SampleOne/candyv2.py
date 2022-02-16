def processcase(case_num):
    # Inputs
    num_candy_bags = int(input())
    num_candy = ((num_candy_bags*num_candy_bags) + num_candy_bags) // 2
    num_kids = int(input())

    # Use module to calculate the remaining candy
    amount_remaining = num_candy % num_kids

    print(f"Case #{case_num}: {amount_remaining}")

# Iterate through each case
num_cases = int(input())
for i in range(num_cases):
    processcase(i + 1)