def maxi(nums):
    i = 0
    maximum = nums[0]
    maxindex = 0
    while i < len(nums):
        if nums[i] > maximum:
            maxindex = i
            i += 1
        else:
            i += 1

    return maxindex
