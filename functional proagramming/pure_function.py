wizard = {
    'name': 'Merlin',
    'power': 50
}
def attack(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))
