def twoSum(nums, target):
    lenNums = len(nums)
    for i in range (0,lenNums):
        for index in range (0,lenNums):
            if (((nums[i] + nums[index]) == target) and index!=i):
                return([i, index])

                
