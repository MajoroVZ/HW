def stalin_sort(lst: list) -> list: return lst if not lst else [lst[0]] + stalin_sort([x for x in lst[1:] if x >= lst[0]])
