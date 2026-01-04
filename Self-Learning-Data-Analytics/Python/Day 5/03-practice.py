# ==========================================
# Program 3
# Question:
# Write a function 'common_elements(list1, list2)' that:
# 1. Takes two lists of numbers
# 2. Returns a set of elements common in both lists
# 3. Returns a list of elements only in list1
# 4. Returns a tuple of elements only in list2
# ==========================================
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common = set1 & set2
    only_list1 = [x for x in list1 if x not in set2]
    only_list2 = tuple([x for x in list2 if x not in set1])

    return common, only_list1, only_list2

# Example run
print(common_elements([1,2,3,4], [3,4,5,6]))