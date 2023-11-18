def init_hash_table(capacity=3):
    buckets = [[] for _ in range(capacity)]
    return buckets


def hash_key(key: str, capacity: int) -> int:
    if not key:
        return 0
    return (ord(key[ord(key[0]) % len(key)]) * (ord(key[ord(key[-1]) % len(key)]))) % capacity


def set_value(hash_table, key: str, value: str):
    buckets = hash_table
    hash_index: int = hash_key(key, 3)
    if not buckets:
        return
    for pair in buckets[hash_index]:
        if pair[0] == key:
            pair[1] = value
            return
    buckets[hash_index].append([key, value])
    return


def get_value(hash_table, key):
    buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    for k, v in buckets[key_hash]:
        if k == key:
            return v
    return None


def del_value(hash_table, key):
    buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    for i in range(len(buckets[key_hash])):
        pair = buckets[key_hash][i]
        if pair[0] == key:
            buckets[key_hash].pop(i)
            return True
    return False


def load_factor(hash_table):
    actual_size = sum(len(bucket) for bucket in hash_table if bucket)
    return actual_size / len(hash_table)
