"""
author:	Julio Ruano
email:	jruano03@gmail.com

Simple function to determine whether there is a sequence of integer
numbers that equal the provided total.
"""
def check_sequence_total(nums, total):
    running_index = 0

    for num in nums:

        # This is the first element of the set
        if running_index == 0:
            running_index += 1
            continue

        # Look for an equal sum for all nums leading up to this index
        index = running_index
        running_total = num
        while index != 0:
            running_total += nums[index - 1]
            if running_total == total:
                return True

            index -= 1

        running_index += 1

    # Sequence sum equal to total was never found
    return False


if __name__ == "__main__":
    nums = [23, 5, 4, 7, 2, 11]
    total = 20

    isSequenceSum = check_sequence_total(nums, total)
    if isSequenceSum:
        print "Why yes it is"
    else:
        print "No it is not"
