"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 14.11 ZyLab - CIS2348
"""


# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for num in numbers:
        num = int(num)
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if int(numbers[j]) > int(numbers[index_largest]):
                index_largest = j

        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        for i in range(len(numbers)):
            print(numbers[i], end=' ')
        print()


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    nums = input()
    nums = nums.split()
    #       selection_sort_descend_trace() to sort the numbers
    for num in nums:
        num = int(num)
    selection_sort_descend_trace(nums)
