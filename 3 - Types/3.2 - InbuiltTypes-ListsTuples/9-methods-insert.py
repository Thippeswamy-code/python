# Describes the insert method of lists

# USAGE
# .insert(index, item)
# inserts an item in place in the list
# self modification function

lists = ['cat', 'dog', 'bat']
lists.insert(1, 'chicken')
print(lists)
lists.insert(-1, 'testsecondlastend')
print(lists)
lists.insert(len(lists), 'testend')
print(lists)