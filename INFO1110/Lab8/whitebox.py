import whiteboxfunct
#testcases
input_nums = [(0, 1, 2),
                (2, 1, 0),
                (0, 0, 0),
                (-2, -1, -3)
                ]
output_index = [2,
                0,
                0,
                1]

i = 0
while i < len(input_nums):
    print("Test case {}".format(i))
    expected_outcome = output_index[i]
    actual_output = whiteboxfunct.maxi(input_nums[i])
    if actual_output != expected_outcome:
        print("Test case failed")
        print("Input:", input_nums[i])
        print("Expected Outcome:", expected_outcome)
        print("Actual Outcome:", actual_output)
    else:
        print("Test case passed")
    print()
    i += 1
