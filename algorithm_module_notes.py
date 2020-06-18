



# algorithm module notes:

# find smallest missing element:

lst = [6,7,8,9,11,12]

# answer is 5...

def smallest_missing(arr):
	# edge case: deal with missing value == 0
	# edge case: if no missing elements...
	# loop through the array
	# check adjacent elements
	# make sure that the adjacent element == current +1
	for i in range(len(arr)):
		if arr[i+1] != arr[i]+1:
			return arr[i]+1
		# how do I check the item beside each item?


# arr[i+1] is the index location + 1 so the value at the next index location
# arr[i] + 1 is the current index value + 1


print(smallest_missing(lst))


# arr = [1,2,3,4,8,9,10]

# for i in range(len(arr)):
# 	print (arr[i+1])
# 	print (arr[i] + 1)



def find_middle_node_of_linked_list(ll):
# idea 1:
	# get the lenght of the linked list
		#how do we get the length?
		# traverse the linked list and keep a counter
		# to keep count of how many jumps we make
	# once we know the length, we can calculate the midpoint
	# traverse to that midpoint / start from head, jump until we reach mid
		# use the midpoint formula from the binary search implementation

# idea 2:
	# use two pointers that we'll start at the head of the lsit
	# the two pointers will run at diff speeds:
	# one pointer will run at twice the speed of the other
		# how do we have a pointer run at twice the speed? how do we update the pointers as we traverse?
		# if we iterate our faster pointer twice the speed "self.next.next"
	# once the faster pointer reaces the end of the list,
	# where will the slower pointer be?


