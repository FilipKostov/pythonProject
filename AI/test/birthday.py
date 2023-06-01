birthdays={'Alexandra': '19/1/2000', 'Stefan': '24/9/2000', 'Filip': '2/2/2001'}
print("We have birthday reservations for:")
for i in birthdays.keys():
    print('\n')
    print(i)
print('\n')
print("\nWhich birthday are you invited to?")
name=input()
print(f'The birthday of {name} is on {birthdays[name]}')
def swap(lista):
    return [(item2, item1) for (item1, item2) in lista]


if __name__ == '__main__':
    print(swap([('a', 1), ('b', 2), ('c', 3)]))