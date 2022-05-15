from pprint import PrettyPrinter


pp = PrettyPrinter().pprint  # for dev use
print('Input orders and enter nothing when done')
print('input form: TYPE (I/F/D) SIZE (S/M/L) ITEM (diet coke, big mac, etc.)\n')

# Item, Fries, Drink
orders = {'I': [], 'F': {'S': [], 'M': [], 'L': []}, 'D': {'S': [], 'M': [], 'L': []}}

order_input = input().strip().lower()

while order_input != '':
    if order_input[0] == 'i':
        order_name = order_input.split(maxsplit=1)[-1]
        orders['I'].append(order_name)
    elif order_input[0] == 'f':
        split_fries = order_input.split(maxsplit=2)
        if len(split_fries) < 3:
            size = split_fries[-1]
            order_name = 'fries'  # fries
        else:  # should be len of 3
            order_name, size, order_name = split_fries
        orders['F'][size.upper()].append(order_name)
    else:  # has to be drink
        # splits only at first 2 spaces so that the item name doesn't split
        order_type, size, order_name = order_input.split(maxsplit=2)
        orders['D'][size.upper()].append(order_name)
    order_input = input().strip().lower()

ex = {
        'D': {
            'L': [],
            'M': ['diet coke'],
            'S': []
        },
        'F': {
            'L': ['fries'],
            'M': ['animal style fries', 'cajun fries'],
            'S': []
        },
        'I': ['mcchicken', 'big mac']
    }

meals = []

while len(orders['I']) > 0:
    found = False
    for sz, drinks in orders['D'].items():
        if len(drinks) > 0:
            if len(orders['F'][sz]) > 0:
                meals.append({
                    'size': sz,
                    'food': orders['I'].pop(0),
                    'drink': drinks.pop(0),
                    'fries':  orders['F'][sz].pop(0)
                })
                found = True
                break
    if not found:
        break

print('Meals Matched:\n')
for m in meals:
    print('size: ' + m['size'])
    print('food: ' + m['food'])
    print('drink: ' + m['drink'])
    print('fries: ' + m['fries'])
    print('--------------------\n')

print('\nItems Remaining:\n')
print('Food:')
for fd in orders['I']:
    print(fd)
print('--------------------\n')
titles = ['Fries', 'Drinks']
order_keys = ['F', 'D']
for ft in range(2):
    print(titles[ft] + ':')
    for sz, things in orders[order_keys[ft]].items():
        for th in things:
            print(f'{sz} {th}')
    print('--------------------\n')
