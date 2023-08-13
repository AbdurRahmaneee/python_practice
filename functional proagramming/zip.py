my_list = [1,2,3]
your_list = [10,20,38]
their_list = [34,45,6]
def only_odd(item):
    return item % 2 != 0
print(list(zip(my_list, your_list, their_list)))
print(my_list)