from collections import Counter

sort_dict = {"a": 20, "b":13, "c":10, "d":19}
"""max_value = max(sort_dict.values())
print(max_value)

min_value = min(sort_dict.values())
print(min_value)"""

sort_value = sorted(sort_dict.values())
print(sort_value)

#desc_order = dict(sorted(sort_dict.items()))
desc_order = dict(Counter(sort_dict).most_common())
print(desc_order)
