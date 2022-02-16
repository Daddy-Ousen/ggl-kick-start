def processcase(case_num):
# Iterate through the each case
    num_cases = int(input())
for i in range(num_cases):
    processcase(i + 1)
# Get input from user of number of candy bags and number of kids
num_candy_bags = int(input())
num_candy = ((num_candy_bags*num_candy_bags) + num_candy_bags) // 2
num_kids = int(input())
# Print number of candy remaining after sharing
amount_remaining = (num_candy % num_kids)

print(f"Case #{case_num}: {amount_remaining}")
