from collections import deque

def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    nums1 = nums.copy()
    output_list = []
    compare_list = []

    #reverse input list
    while nums1:
        for num in nums1:
            compare_list.append(nums1[-1])
            nums1.pop()
              
    print("compare_list", compare_list)
    print("nums", nums)
    # i = 0
    # while i < len(nums):
    #     for num in compare_list:
    #         if nums[i] > compare_list[-1]:
    #             print("in if", nums[i])
    #             choose_num = compare_list[-1]
    #             print("choose_num", choose_num)
    #             compare_list.pop()
    #         else:
    #             print("in else")
    #             choose_num = -1
        
    #     output_list.append(choose_num)
    #     print("Output list", output_list)
    #     i += 1
    
    # print(output_list)

    while len(compare_list)>1:
        if compare_list[-2] > compare_list[-1]:
            choose_num = compare_list[-2]
            print("choose_num", choose_num)
            compare_list.pop()
        else:
            choose_num = -1
            compare_list.pop()

        output_list.append(choose_num)
    output_list.append(-1)
    print(output_list)
nums = [2, 1, 2, 4, 3]
#nums = [2, 5, 2, 4, 3]
next_greater_to_right(nums)

