"""
author: Julio Ruano
email: jruano03@gmail.com

Simple function to determine if any 3 numbers can be summed to equal 0
from a provided input.
"""
def check_sum_zero(nums):
    # initialize starting point
    current_index = 0
    inner_index = 1
    outer_index = 2
    outer_bound = len(nums)

    # Total numbers we are checking is 3
    # Xnn pattern
    while current_index < outer_bound - 2:
        for num in nums:
            # nXn pattern
            while inner_index < outer_bound - 1:
                # Check simplest, sequential case
                if num + nums[inner_index] + nums[outer_index] == 0:
                    print str(num) + "," + str(nums[inner_index]) + "," + str(nums[outer_index])
                    return True

                # nnX pattern
                outer_index += 1
                while outer_index < outer_bound:
                    if num + nums[inner_index] + nums[outer_index] == 0:
                        print str(num) + "," + str(nums[inner_index]) + "," + str(nums[outer_index])
                        return True

                    outer_index += 1

                # Update positions
                inner_index += 1
                outer_index = inner_index + 1

            # Update positions
            current_index += 1
            inner_index = current_index + 1
            outer_index = inner_index + 1

    # Didn't find a zero sum
    return False

if __name__ == "__main__":
    nums = [4, 2, -1, 1, 7, -12, -4]

    isZeroSum = check_sum_zero(nums)
    if isZeroSum:
        print "Why yes it is"
    else:
        print "No it is not"
