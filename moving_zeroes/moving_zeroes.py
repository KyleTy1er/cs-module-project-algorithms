'''
Input: a List of integers
Returns: a List of integers
'''


# def moving_zeroes(arr):
# 	# initialize count for iteration:
# 	count = 0
# 	# for item in range of the length of the array
# 	# to iterate per index locations
# 	for i in range(len(arr)):
# 		# if item at index location [i] does not equal zero:
# 		if arr[i] != 0:
# 			# switch the item at index location [i]
# 			# with item at index location [count]
# 			arr[count] = arr[i]
# 			# make count increase by 1 so it moves up
# 			count +=1

# 	# after the for loop iterates through all of the range of length of array
# 	# this while loop will kick in
# 	# while count is less than the length of the array
# 	while count < len(arr):
# 		# value at index location arr[count] gets changed to 0
# 		arr[count] = 0
# 		# count increases by 1 to give the while loop a stopping point
# 		count += 1
# 	return arr


# optimized solution:

def moving_zeroes(arr):
  n = len(arr)
  arr[:] = filter(None, arr)
  arr.extend([0] * (n - len(arr)))
  return arr




arr = [0, 3, 1, 0, -2]

moving_zeroes(arr)

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")