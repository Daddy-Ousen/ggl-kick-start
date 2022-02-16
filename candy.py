def processcase(case_num):
    # Read in the input for a single case
    (num_candy_bags, num_kids) = tuple(map(int, input().split()))
    candy_counts = list(map(int, input().split()))

    # Calculate the amount of candy remaining
    ammount_remaining = 0

    print(f"Case #{case_num}: {ammount_remaining}")
    