'''
Input: a List of integers
Returns: a List of integers
# '''
# def product_of_all_other_numbers(arr):
#     prod = []
#     val = 1
#     for i in range(0, len(arr)):
#         for x in range(0, len(arr)):
#             if i != x:
#                 val *= arr[x]
#         prod.append(val)
#         val = 1
#     return prod




import math
# optimized solution:
def product_of_all_other_numbers(arr):
    arr1 = [0] * len(arr)
    for i in range(len(arr)):
        arr1[i] = math.prod(list(arr[:i] + arr[i+1]))
    return arr1



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
