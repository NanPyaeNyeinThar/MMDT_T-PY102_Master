N = 0 #table size

#Hash Func 1
#module hash function
def moduleHashFunction(key):
    return key % N

#Hash Func 2
#unicode hash function
def unicodeHashFun(key):
    return ord(key[0])      #index = unicodeHashFun(key)%Table_size

#Hash Func 3
#module hash function 2
def unicodeHashFun2(key):
    return ord(key[0]) - ord('A')   #index = unicodeHashFun2(key)%10

#Hash Func 4
def ascii_sum_hash(key: str) -> int:
    if not isinstance(key, str):
        raise TypeError("key must be a string")
    
    if not (1 <= len(key) <= 4):
        raise ValueError("key must be 1 to 4 characters long")
    
    #Sum ASCII codes
    return sum(ord(ch) for ch in key)   #index = ascii_sum_hash(key)%309

