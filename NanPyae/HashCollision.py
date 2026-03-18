# Mid Square Hash
# Key Distribution
def mid_square_hash(key, N, R):
    #step 1: square the key
    squared = key * key

    #step 2: convert to string to work with digits
    s = str(squared)
    length = len(s)

    #step 3: compute starting index for middle digits
    start = (length - R) // 2

    #step 4: extract R middle digits
    middle = int(s[start:start + R])

    #step 5: apply modulo to fix table size
    return middle % N