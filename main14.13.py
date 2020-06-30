"""
Author: Schilling, Thomas, J
StudentID: 1937109
File: 14.13 ZyLab - CIS2348
"""

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    #  Pick middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h]
        while pivot < user_ids[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        if l >= h:
            done = True
        else:
            """  Swap numbers[l] and numbers[h],
                  update l and h """
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    j = 0
    """  Base case: If there are 1 or zero entries to sort,
          partition is already sorted  """
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """
    j = partition(user_ids, i, k)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    global num_calls
    num_calls += 1
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    num_calls = (num_calls * 2) + 1
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
