# Chaining Code Tracking
def HashInsert(table: list[list[tuple]], key, value) -> None:
    index = hash(key) % len(table)  # 4%3  for (4,A), 1%3 for (1,B)
    bucket = table[index]           # index 1 for (4,A), index 1 for (1,B)
                                    # same index but different key, will append

    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)    # if key and new key same, update the value
            return
    bucket.append((key, value)) # if not same, append the value

def h(key):
    return key % 3

table = [[], [], []]
HashInsert(table, 4, "A")
HashInsert(table, 1, "B")

##################

# Linear probing code tracing

def insert_linear_probing(table: list[int | None], key: int) -> list[int | None]:
    n = len(table)
    idx = key % n

    for _ in range(n):
        if table[idx] is None:
            table[idx] = key
            return table
        idx = (idx + 1) % n
    return table

insert_linear_probing(table, 13)
insert_linear_probing(table, 2)
insert_linear_probing(table, 5)

###################
#Quadratic Probing

def insert_quadratic_probing(table: list[int | None], key: int) -> list[int | None]:
    n = len(table)
    h = key % n

    for i in range(n):
        idx = (h + i * i) % n
        if table[idx] is None:
            table[idx] = key
            return table
        
    return table