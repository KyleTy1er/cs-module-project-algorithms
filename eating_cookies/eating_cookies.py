'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# optimized solution (cache)

def eating_cookies(n, cache=None):
    if cache == None:
        cache = [0] * (n + 1)
    if n < 0:
        return 1
    elif n == 0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]



# cache is a dict and keys are n - the value is the answer
    def eating_cookies(n, cache):
    if n < 0:
        return 1
    elif n == 0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        # if cache doesnt contain answer well use recursion
        # and save results for the future:
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
