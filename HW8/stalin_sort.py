def stalin_sort(lst: list) -> list: return lst if not lst else [lst[x] for x in range(len(lst)) if
                                                                x == 0 or lst[x] >= max(lst[:x])]

