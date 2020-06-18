'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    arr.sort()
    f = 0
    s = 1
    for i in range(0, len(arr)):
        if s >= len(arr):
            return arr[f]
        first_val = arr[f]
        second_val = arr[s]
        if first_val != second_val:
            return first_val
        f += 2
        s += 2


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")