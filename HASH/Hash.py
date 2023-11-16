def init_hash_table(capacity=100):
    size = 0
    buckets = [[] for _ in range(capacity)]
    return size, buckets


def hash_key(key, capacity: int) -> int:
    return (ord(key[ord(key[0]) % len(key)]) * (ord(key[ord(key[-1]) % len(key)]))) % capacity


def set_value(hash_table, key: str, value):
    size, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    key_value = (key, value)
    if buckets[key_hash] is None:
        buckets[key_hash] = [key_value]
        size += 1
        return True
    for i, pair in enumerate(buckets[key_hash]):
        if pair[0] == key:
            buckets[key_hash][i] = key_value
            return True
    buckets[key_hash].append(key_value)
    size += 1
    return True


def get_value(hash_table, key):
    _, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    if buckets[key_hash] is not None:
        for pair in buckets[key_hash]:
            if pair[0] == key:
                return pair[1]
    return None


def del_value(hash_table, key):
    size, buckets = hash_table
    key_hash = hash_key(key, len(buckets))
    if buckets[key_hash] is None:
        return False
    for i, pair in enumerate(buckets[key_hash]):
        if pair[0] == key:
            buckets[key_hash].pop(i)
            size -= 1
            return True
    return False


def load_factor(hash_table):
    size, buckets = hash_table
    actual_size = sum(len(bucket) for bucket in buckets if bucket)
    return actual_size / len(buckets)

